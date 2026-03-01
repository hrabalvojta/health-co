"""
EuroHealth AI Helpdesk — Policy Engine (PDP/PEP)
=================================================

PDP (Policy Decision Point): Reads policy YAML files, evaluates rules.
PEP (Policy Enforcement Point): Sits in the pipeline, enforces decisions.

This is a simplified implementation for educational purposes.
A production system would use OPA (Open Policy Agent) or similar.
"""

import yaml
import os
import json
from datetime import datetime, timezone


class PolicyDecisionPoint:
    """
    PDP — The Brain.
    Loads policy YAML files and evaluates queries/responses against rules.
    Returns a decision: allow, block, redirect, or escalate.
    """

    def __init__(self, policies_dir="policies"):
        self.policies = []
        self.load_policies(policies_dir)

    def load_policies(self, policies_dir):
        """Load all YAML policy files from directory."""
        if not os.path.exists(policies_dir):
            print(f"Warning: policies directory '{policies_dir}' not found")
            return

        for filename in os.listdir(policies_dir):
            if filename.endswith(".yaml") or filename.endswith(".yml"):
                filepath = os.path.join(policies_dir, filename)
                with open(filepath) as f:
                    policy = yaml.safe_load(f)
                    self.policies.append(policy)
                    print(f"  Loaded policy: {policy['policy']['name']} "
                          f"({len(policy['policy']['rules'])} rules)")

    def evaluate(self, query: str, response: str, confidence: float = 1.0) -> dict:
        """
        Evaluate a query/response pair against all loaded policies.
        Returns the first matching rule's decision.
        """
        for policy in self.policies:
            for rule in policy["policy"]["rules"]:
                # Simplified matching — production would use proper NLP
                if self._rule_matches(rule, query, response, confidence):
                    return {
                        "decision": rule["then"],
                        "policy": policy["policy"]["name"],
                        "rule_id": rule["id"],
                        "reason": rule.get("log", "Policy rule matched"),
                        "substitute": rule.get("respond", rule.get("substitute", None)),
                        "escalate_to": rule.get("escalate_to", None),
                    }

        return {"decision": "allow", "policy": None, "rule_id": None}

    def _rule_matches(self, rule, query, response, confidence):
        """Check if a rule matches. Simplified keyword matching."""
        rule_if = rule.get("if", "").lower()

        # Check response content rules
        if "response.contains" in rule_if:
            keywords = rule_if.split("(")[1].rstrip(")").split(",")
            keywords = [k.strip() for k in keywords]
            return any(kw in response.lower() for kw in keywords)

        # Check confidence rules
        if "confidence" in rule_if and "<" in rule_if:
            threshold = float(rule_if.split("<")[1].strip())
            return confidence < threshold

        return False


class PolicyEnforcementPoint:
    """
    PEP — The Muscle.
    Sits in the pipeline between generation and response delivery.
    Calls PDP for decision, enforces it, logs everything.
    """

    def __init__(self, pdp: PolicyDecisionPoint, audit_log_path="audit.log"):
        self.pdp = pdp
        self.audit_log_path = audit_log_path

    def enforce(self, query: str, response: str, confidence: float = 1.0) -> dict:
        """
        Check response against policies before delivering to user.
        Returns the final response (original or substitute).
        """
        decision = self.pdp.evaluate(query, response, confidence)

        # Log every decision (allow or block)
        self._write_audit_log(query, response, decision)

        if decision["decision"] == "allow":
            return {
                "response": response,
                "blocked": False,
                "policy_action": "allow",
            }
        else:
            return {
                "response": decision.get("substitute", "Request blocked by policy."),
                "blocked": True,
                "policy_action": decision["decision"],
                "policy": decision["policy"],
                "rule_id": decision["rule_id"],
                "reason": decision["reason"],
                "escalated_to": decision.get("escalate_to"),
            }

    def _write_audit_log(self, query, response, decision):
        """Write structured audit log entry."""
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "query_hash": hash(query) % 10**8,  # Don't log raw PII
            "decision": decision["decision"],
            "policy": decision.get("policy"),
            "rule_id": decision.get("rule_id"),
            "reason": decision.get("reason"),
        }

        with open(self.audit_log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")


# ═══════════════════════════════════════════════════════
#  Example usage (for instructor demo)
# ═══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n  Loading Policy Engine...\n")

    pdp = PolicyDecisionPoint("policies")
    pep = PolicyEnforcementPoint(pdp)

    # Test query
    query = "What is the salary of John Smith?"
    unsafe_response = "John Smith's monthly salary is 10,000 EUR. His ID is 123456/7890."

    print(f"\n  Query: {query}")
    print(f"  Generated response: {unsafe_response}\n")

    result = pep.enforce(query, unsafe_response)

    if result["blocked"]:
        print(f"  ⛔ BLOCKED by {result['policy']} / {result['rule_id']}")
        print(f"  Reason: {result['reason']}")
        print(f"  Safe response: {result['response']}")
    else:
        print(f"  ✓ ALLOWED — response delivered")
