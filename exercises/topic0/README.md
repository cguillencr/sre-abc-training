# **Understanding SLO, SLI, SLA, and Error Budgets in SRE**

## **Table of Contents**
- [Overview](#overview)
- [Definitions and Proper Order](#definitions-and-proper-order)
  - [Service Level Indicator (SLI)](#service-level-indicator-sli)
  - [Service Level Objective (SLO)](#service-level-objective-slo)
  - [Service Level Agreement (SLA)](#service-level-agreement-sla)
  - [Error Budget](#error-budget)
- [Applying SLIs, SLOs, SLAs, and Error Budgets](#applying-slis-slos-slas-and-error-budgets)
  - [Greenfield Project Example](#greenfield-project-example)
  - [Mature Product Example](#mature-product-example)
- [Error Budget and SLO Miss Policy](#error-budget-and-slo-miss-policy)
- [Continuous Improvement of SLO Targets](#continuous-improvement-of-slo-targets)
- [Why 100% SLO Is Unrealistic](#why-100-slo-is-unrealistic)
- [Defining SLOs for Services](#defining-slos-for-services)

---

## **Overview**
In **Site Reliability Engineering (SRE)**, the concepts of **Service Level Indicators (SLIs)**, **Service Level Objectives (SLOs)**, **Service Level Agreements (SLAs)**, and **Error Budgets** are fundamental in defining, measuring, and maintaining system reliability. 

By implementing these concepts effectively, organizations can:
- Balance reliability with feature development.
- Set realistic expectations for customers.
- Create structured responses when reliability goals are missed.
- Maintain an efficient trade-off between system stability and innovation.

---

## **Definitions and Proper Order**
To effectively set up reliability metrics, it’s essential to define SLIs, SLOs, SLAs, and Error Budgets in the correct sequence.

### **Service Level Indicator (SLI)**
- **Definition**: SLIs are quantitative measurements that track system performance and user experience.
- **Examples**: Availability percentage, request latency, error rate, successful queries per second.
- **Use Case**: If **99% of API requests** complete successfully within **200ms**, then **99%** is the **SLI** for request latency.

### **Service Level Objective (SLO)**
- **Definition**: SLOs are reliability goals based on SLIs that define acceptable performance levels.
- **Examples**: 
  - **Availability SLO**: 99.9% uptime.
  - **Latency SLO**: 95% of requests complete within 100ms.
- **Use Case**: If an SLI shows **99.8% availability**, and the target SLO is **99.9%**, then reliability efforts must improve.

### **Service Level Agreement (SLA)**
- **Definition**: SLAs are contractual agreements with customers that specify expected service reliability and penalties for failing to meet targets.
- **Examples**: 
  - **"Service must be available 99.9% of the time, or customers receive credits."**
  - **"If request latency exceeds 200ms for 5% of requests, a financial penalty applies."**
- **Use Case**: An SLA guarantees compensation for breaches, ensuring accountability.

### **Error Budget**
- **Definition**: The amount of allowable unreliability before corrective actions are taken.
- **Example**: If an SLO defines **99.9% availability**, the **error budget allows 0.1% downtime** (about **43.2 minutes per month**).
- **Use Case**: If a service has already failed for **35 minutes**, only **8.2 minutes** remain before **new deployments** are frozen.

### **Proper Order for Implementation**
1. **Define SLIs** → Decide what system behaviors need measurement.
2. **Set SLOs** → Establish reliability targets based on SLIs.
3. **Establish SLAs** → Create legal commitments aligned with SLOs.
4. **Allocate an Error Budget** → Define acceptable failure limits before corrective action is needed.

---

## **Applying SLIs, SLOs, SLAs, and Error Budgets**
SLI, SLO, SLA, and Error Budget implementations vary between **newly developed applications (Greenfield)** and **established services (Mature Products).** The table below illustrates the differences:

| **Criteria**          | **Greenfield Project**                 | **Mature Product**                   |
|-----------------------|---------------------------------------|---------------------------------------|
| **Define SLIs**       | Basic metrics: availability, latency, errors. | Advanced SLIs: geographic availability, detailed latency percentiles. |
| **Set SLOs**         | Initial target: 99.9% availability.   | Fine-tuned targets: 99.95% availability. |
| **Establish SLAs**    | SLAs postponed until stability is proven. | Customer-driven SLAs with penalties for breaches. |
| **Allocate Error Budget** | Allows 0.1% downtime for rapid iteration. | Smaller error budget (e.g., 0.05%) to maintain reliability. |
| **SLO Miss Policy**   | Delay deployments if budget is exceeded. | Freeze features, require incident reviews. |
| **Continuous Improvement** | Quarterly review of SLOs. | Adjust SLOs based on system performance trends. |

---

## **Error Budget and SLO Miss Policy**
If an **SLO is breached**, the **Error Budget** determines how teams respond.

### **Greenfield Project**
- **Policy**: Restrict feature releases if the error budget is exceeded.
- **Action**: If the budget is fully consumed, **freeze deployments** for **one week** and focus on stability.

### **Mature Product**
- **Policy**: Immediate intervention required if an SLO breach occurs.
- **Action**: **All new features are paused**, an **incident review is mandatory**, and **reliability improvements take priority**.

---

## **Continuous Improvement of SLO Targets**
SLOs should evolve based on:
- **Historical data**: If an SLO is always exceeded (e.g., 99.99% uptime for a 99.9% SLO), it may be time to **raise the SLO**.
- **Customer expectations**: Business needs may require tighter SLAs and more stringent SLOs.
- **System architecture improvements**: As infrastructure matures, more aggressive SLOs may be feasible.

### **Example**
A service initially targets **99.9% availability**, but internal monitoring consistently shows **99.95% uptime**. The SLO is then **increased to 99.95%**, aligning expectations with actual performance.

---

## **Why 100% SLO Is Unrealistic**
Perfect reliability is **impossible** due to:
1. **Cost**: 100% availability is **expensive** and **over-engineering**.
2. **Human Error**: Mistakes will occur, making perfection unattainable.
3. **Third-Party Dependencies**: External services introduce unpredictability.
4. **Diminishing Returns**: Improving uptime from 99.99% to 99.999% increases cost exponentially.

### **Real-World Example**
A **99.99% uptime** goal allows for brief, **non-disruptive downtimes**, balancing cost and reliability.

---

## **Defining SLOs for Services**
The table below provides **examples of well-defined SLOs** for common service metrics.

| **SLO Category** | **Objective**                                      | **Target**                                     | **SLI (Service Level Indicator)**                                                        | **Error Budget**                                 |
|------------------|--------------------------------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------|
| **Latency**      | REST API should respond within **100ms**.        | **95% of requests** complete within 100ms.  | Percentage of requests completing within 100ms (**measured via Prometheus**).           | **5% of requests** may exceed the 100ms limit.   |
| **Availability** | Ensure high uptime.                              | **99.95% availability** per month.          | Percentage of requests without failures (**measured via HTTP 2xx response codes**).     | **0.05% downtime allowed per month.**            |
| **Traffic**      | Monitor network stability.                       | Keep transmission rate within normal range.  | Rate of bytes transmitted (**measured via Prometheus network metrics**).                | **5% above expected transmission before scaling.** |

---

This document provides **SRE fundamentals** for defining reliability goals, **balancing uptime and development speed**, and **managing system risk effectively**.

---