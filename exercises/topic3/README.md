# **Operational Readiness Review (ORR) Checklist**

## **Table of Contents**

1. [Introduction](#introduction)  
2. [Why is an ORR Checklist Important?](#why-is-an-orr-checklist-important)  
3. [When Should an ORR Checklist Be Conducted?](#when-should-an-orr-checklist-be-conducted)  
4. [Key ORR Checklist Items](#key-orr-checklist-items)  
   - [Monitoring & Alerting](#monitoring--alerting)  
   - [Standardized Logging & Log Storage](#standardized-logging--log-storage)  
   - [Distributed Tracing](#distributed-tracing)  
   - [Runbooks & Incident Response Procedures](#runbooks--incident-response-procedures)  
   - [Disaster Recovery & Failover](#disaster-recovery--failover)  
5. [Post-ORR Actions & Continuous Improvement](#post-orr-actions--continuous-improvement)

---

## **Introduction**

In Site Reliability Engineering (SRE), an **Operational Readiness Review (ORR)** checklist is a structured approach to assessing a system’s **production readiness**. The ORR checklist ensures that applications and infrastructure meet **key reliability, observability, and operational** standards before they are deployed into a live environment.

> Example: An SRE team at an e-commerce company prevented an outage during a high-traffic sale event by conducting an ORR. They discovered that a missing database index would have caused slow queries under heavy load.

By following an ORR checklist, teams can **identify risks**, **reduce deployment failures**, and **improve system resilience**.

---

## **Why is an ORR Checklist Important?**
The ORR checklist is a proactive approach to **preventing operational issues**. It helps teams answer critical questions such as:
- **Is the system observable?** (Are logs, traces, and metrics collected correctly?)
- **Is there a plan for failures?** (Do we have monitoring, alerts, and recovery plans in place?)
- **Is documentation complete?** (Are runbooks available for troubleshooting?)
- **Can we recover from incidents?** (Are backups, disaster recovery, and failover tested?)

Without a proper ORR, teams risk **shipping unreliable systems** that lead to incidents, downtime, and customer impact.

---

## **When Should an ORR Checklist Be Conducted?**
An ORR checklist should be conducted in the following scenarios:

✅ **Before deploying a new service or major feature**  
✅ **After significant architectural changes or migrations**  
✅ **Before scaling an application to handle increased load**  
✅ **After a major incident to improve reliability**  
✅ **During periodic operational audits** (e.g., quarterly reliability reviews)

For mature SRE practices, **ORRs should be a recurring process** that evolves alongside the system.

---

## **Key ORR Checklist Items**

### **1. Monitoring & Alerting**
✔ **Check**: Is a monitoring and alerting system in place?  
✔ **Check**: Are SLIs (Service Level Indicators) defined and monitored?  
✔ **Check**: Are alerts configured for **critical system failures**?  

**Best Practices:**
- Use **Prometheus** to collect system metrics.  
- Define **SLO-based alerts** in **Grafana** or **Alertmanager**.  
- Ensure alert **notifications are routed** correctly (Slack, PagerDuty, etc.).

🔹 *Example:* If the application latency exceeds 200ms (SLO), an alert should trigger with severity levels (warning/critical).

---

### **2. Standardized Logging & Log Storage**
✔ **Check**: Do all services follow a **structured logging format** (e.g., JSON logs)?  
✔ **Check**: Are logs stored in a **centralized location** (e.g., Elasticsearch, Loki)?  
✔ **Check**: Are **log retention policies** defined?  

**Best Practices:**
- Implement **JSON logging** for consistency.  
- Use **Fluentd or Logstash** to ship logs to **Elasticsearch**.  
- Define a **log rotation policy** to prevent excessive storage costs.  

🔹 *Example:* Logs should include **trace IDs** to correlate events across microservices.

---

### **3. Distributed Tracing**
✔ **Check**: Is **end-to-end tracing** enabled for user requests?  
✔ **Check**: Are **trace IDs propagated across all microservices**?  
✔ **Check**: Can traces be **visualized in a UI** (e.g., Jaeger, OpenTelemetry)?  

**Best Practices:**
- Use **OpenTelemetry** to standardize tracing.  
- Ensure all requests carry a **trace ID** in headers.  
- Store traces in **Jaeger** for query and analysis.  

🔹 *Example:* Tracing should show how long a request spends in each microservice, identifying **bottlenecks**.

---

### **4. Runbooks & Incident Response Procedures**
✔ **Check**: Are **runbooks available** for common failure scenarios?  
✔ **Check**: Are **incident response steps** clearly documented?  
✔ **Check**: Are **automated runbooks** implemented where possible?  

**Best Practices:**
- Document **step-by-step remediation actions** in **GitHub Wiki or Confluence**.  
- Automate remediation tasks using **Ansible AWX**.  
- Conduct **regular incident response drills** to train teams.  

🔹 *Example:* If a database connection pool is exhausted, the runbook should describe:
  1. How to identify the issue in logs.
  2. Temporary workarounds (restart services).
  3. Long-term solutions (increase connection pool size).

---

### **5. Disaster Recovery & Failover**
✔ **Check**: Are **backups tested** for data recovery?  
✔ **Check**: Can the system **failover** to a secondary region?  
✔ **Check**: Has a **disaster recovery test** been conducted recently?  

**Best Practices:**
- Implement **daily backups** and test **automated restoration**.  
- Use **multi-region failover** for critical services (e.g., AWS RDS Multi-AZ).  
- Define **Recovery Time Objective (RTO)** and **Recovery Point Objective (RPO)**.  

🔹 *Example:* A **failover test** should validate that when the primary database goes down, the secondary database takes over within **30 seconds**.

---

## **Post-ORR Actions & Continuous Improvement**

After completing the ORR checklist:

### **1️⃣ Document Findings & Report Issues**  
- Record **pass/fail criteria** for each checklist item.  
- Identify **gaps** and **areas of improvement**.  

### **2️⃣ Prioritize & Implement Fixes**  
- **Critical issues:** Must be fixed before production deployment.  
- **Medium priority:** Address within the next sprint.  
- **Low priority:** Track for future improvements.  

### **3️⃣ Schedule Regular ORRs**  
- Conduct ORRs **quarterly** or **before major changes**.  
- Keep **historical records** to measure improvements over time.  

### **4️⃣ Automate ORR Processes**  
- Use **GitHub Actions** or **Terraform Compliance Tests** to enforce ORR checks.  
- Automate **alerts** and **self-healing mechanisms** to address common failures.  

---

## **Final Thoughts**
An **Operational Readiness Review (ORR)** is not just a checklist—it’s a **reliability strategy**.  
By proactively identifying risks **before production**, teams can prevent downtime, improve system resilience, and build a **culture of reliability**.

---

### **Next Steps**
📌 **Apply this ORR checklist to your project and document the results.**  
📌 **Create a historical record of ORRs to track system improvements.**  
📌 **Discuss ORR findings with your SRE team and prioritize key improvements.**  

---