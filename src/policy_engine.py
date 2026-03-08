"""
EuroHealth AI Helpdesk — Policy Engine (PDP/PEP)
=================================================
PDP = reads policy YAML files, evaluates rules, returns decision
PEP = sits in the pipeline, calls PDP, enforces the decision

Architecture:
    User Query → Retriever → LLM → [PEP] → Response
                                      ↑
                                    [PDP] ← policies/*.yaml
"""

import yaml
import logging
from pathlib import Path
from dataclasses import dataclass
from typing import Literal

logger = logging.getLogger("policy_engine")


@dataclass
class PolicyDecision:
    action: Literal["allow", "block", "redirect", "escalate", "redact"]
    policy_name: str | None = None
    rule_id: str | None = None
    substitute_response: str | None = None
    escalate_to: str | None = None


class PolicyDecisionPoint:
    """Reads YAML rules, evaluates, decides. Does NOT enforce."""

    def __init__(self, policies_dir: str = "policies/"):
        self.policies = self._load_policies(policies_dir)

    def _load_policies(self, policies_dir: str) -> list[dict]:
        policies = []
        for f in Path(policies_dir).glob("*.yaml"):
            with open(f) as fh:
                policies.append(yaml.safe_load(fh))
        return policies

    def evaluate(self, query: str, response: str, confidence: float) -> PolicyDecision:
        # TODO: Real rule evaluation logic
        return PolicyDecision(action="allow")


class PolicyEnforcementPoint:
    """Sits in pipeline. Calls PDP. Enforces. Logs."""

    def __init__(self, pdp: PolicyDecisionPoint):
        self.pdp = pdp

    def enforce(self, query: str, response: str, confidence: float) -> str:
        decision = self.pdp.evaluate(query, response, confidence)
        self._log(query, decision)

        if decision.action == "allow":
            return response
        elif decision.action == "block":
            if decision.escalate_to:
                self._escalate(query, decision.escalate_to)
            return decision.substitute_response or "I cannot process this request."
        elif decision.action == "escalate":
            self._escalate(query, decision.escalate_to or "human_agent")
            return decision.substitute_response or "Connecting you with a human agent."
        else:
            return "I cannot process this request. Please contact IT support."

    def _log(self, query, decision):
        logger.info(f"AUDIT: action={decision.action} policy={decision.policy_name} rule={decision.rule_id}")

    def _escalate(self, query, target):
        logger.info(f"ESCALATION: routing to {target}")
