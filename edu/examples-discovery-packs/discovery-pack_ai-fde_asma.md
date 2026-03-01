# Senior FDE Discovery Matrix

## Focus: Questions a Senior FDE Would Ask

  -------------------------------------------------------------------------------------------------------------
  \#   Senior-Level       Primary KAF      Secondary KAF    Red Flags        Assumptions /     3 KPI Proposals
       Question                                                              Risks             
  ---- ------------------ ---------------- ---------------- ---------------- ----------------- ----------------
  1    What decision in   Core             Interop +        Vendor lock-in;  Irreversible      1️⃣ % modular
       this project would                  Policy-as-Code   tightly coupled  platform choice;  components 2️⃣
       be the most                                          architecture     costly            Vendor
       expensive to                                                          re-architecture   dependency ratio
       reverse in 12                                                                           3️⃣
       months?                                                                                 Re-platforming
                                                                                               cost estimate

  2    If the AI system   Run Safe         Core             No failover      Large blast       1️⃣ System
       fails during a                                       plan; shared     radius during     isolation
       major outage, what                                   infra            outages           coverage % 2️⃣
       systems must                                         dependencies                       Failover test
       continue operating                                                                      frequency 3️⃣
       independently, and                                                                      Recovery Time
       how is isolation                                                                        Objective (RTO)
       guaranteed?                                                                             

  3    Who owns model     Policy-as-Code   Run Safe         No clear         Model drift       1️⃣ Model review
       versioning,                                          lifecycle owner; unmanaged;        cadence 2️⃣ %
       monitoring, and                                      informal updates compliance gaps   models with
       retirement                                                                              lifecycle owner
       decisions                                                                               3️⃣ Drift
       post--Phase 1?                                                                          detection
                                                                                               coverage

  4    What is the        Core             Run Safe         Budget focused   OPEX              1️⃣ Total cost of
       12-month                                             only on build    underestimated;   ownership (TCO)
       operational cost                                     phase (€180K)    sustainability    2️⃣ Infra
       of running this                                                       risk              utilization rate
       on-prem AI                                                                              3️⃣ Cost per
       platform?                                                                               resolved ticket

  5    Whose KPIs might   HITL             Core             Organizational   Adoption          1️⃣ Adoption rate
       worsen if this                                       resistance;      sabotage; shadow  % 2️⃣ Manual
       system succeeds?                                     hidden           processes emerge  override
                                                            incentives                         frequency 3️⃣
                                                                                               Employee
                                                                                               sentiment score

  6    Have you           Run Safe         Policy-as-Code   Never tested     Compliance        1️⃣ Audit
       stress-tested your                                   audit scenario   readiness         simulation
       ability to defend                                                     overstated        frequency 2️⃣
       an automated                                                                            Mean Time to
       decision under                                                                          Evidence (MTTE)
       regulatory                                                                              3️⃣ % decisions
       scrutiny?                                                                               fully traceable

  7    What percentage of Ingestion        Core             No KB            Model answers     1️⃣ KB refresh
       your knowledge                                       governance;      degrade over time rate % 2️⃣ Drift
       base becomes                                         outdated                           detection rate
       outdated each                                        documentation                      3️⃣ Answer
       quarter, and who                                                                        accuracy trend
       prevents model                                                                          
       drift from stale                                                                        
       content?                                                                                

  8    What prevents this Policy-as-Code   Interop          Business units   Governance        1️⃣ % agents
       agent from                                           deploy agents    fragmentation;    centrally
       expanding beyond                                     independently    shadow AI growth  registered 2️⃣
       IT without                                                                              Unauthorized
       centralized                                                                             agent detection
       governance                                                                              rate 3️⃣
       approval?                                                                               Governance
                                                                                               approval cycle
                                                                                               time

  9    At what measurable HITL             Run Safe         No defined       Over-automation   1️⃣ Error rate
       error rate would                                     kill-switch      damages CSAT      threshold % 2️⃣
       you suspend AI                                       threshold        (3.2/5 baseline)  CSAT delta (3.2
       auto-resolution?                                                                        → 4.0+) 3️⃣ Human
                                                                                               escalation rate

  10   If a better        Core             Interop          Hard-coded       Platform lock-in; 1️⃣ Component
       model/platform                                       integrations;    costly future     modularity index
       appears next year,                                   monolithic       migration         2️⃣ API
       how easily can                                       design                             abstraction
       components be                                                                           coverage % 3️⃣
       swapped without                                                                         Swap test
       full                                                                                    frequency
       re-architecture?                                                                        
  -------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Senior-Level KPI Themes

1.  Architectural reversibility\
2.  Regulatory defensibility\
3.  Long-term economic sustainability
