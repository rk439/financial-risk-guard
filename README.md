# Financial Risk Guard Portfolio
# Customer Financial Risk Guard Copilot (Agentic RAG)

An enterprise-ready AI compliance agent that uses a **ReAct (Reason + Act)** loop framework to analyze live customer cloud metrics against corporate legal contracts. 

This project demonstrates production-ready AI governance by applying explicit cost and safety constraints to autonomous agent behaviors.

---

## 💼 Business Use Case & Problem Statement
When Account Managers (AMs) execute enterprise renewals, they often lack immediate visibility into a client's real-time cloud resource consumption. If a flat-rate contract is closed while a client is experiencing an unbilled cloud usage spike, the company suffers severe margin loss and revenue leakage.

**The Solution:** This agent acts as an automated operational gatekeeper. It dynamically:
1. Orchestrates a **ReAct loop** to determine what information is missing.
2. Queries live database structures via an abstracted data interface (**Model Context Protocol / Tool concept**).
3. Evaluates semantic business constraints by extracting data from legal text policies (**Retrieval-Augmented Generation / RAG concept**).
4. Generates an immediate risk flag and financial calculation before a contract is finalized.

---

## 🛠️ System Architecture & Framework Data Flow

```text
    [ User Audit Prompt ] 
              │
              ▼
    ┌──────────────────┐
    │    ReAct Loop    │ ◄─── (Brain: Processes Thought, Action, and Observation)
    └─────────┬────────┘
              │
              ├──► Action A: Triggers RAG Tool ──────► Reads 'pricing_policy.txt'
              │
              └──► Action B: Triggers DB/MCP Tool ───► Reads 'acme_corp_metrics.json'
              │
              ▼
    [ Guardrail Checks ] ◄─── Enforces Loop Limit Threshold (MAX_LOOPS = 3)
              │
              ▼
    [ Final Risk Report ] ──► Flags 2.5x infrastructure spikes and isolates overage value.
```

---

## 📈 Applied AI PM Best Practices

### 1. Financial Guardrails (Loop Limit Engine)
Because ReAct agents possess autonomous loop execution capabilities, they are highly susceptible to infinite loop sequences if data interfaces fail or return unexpected formats. This results in exponential API token depletion. This architecture mitigates this financial vulnerability by enforcing a strict framework check: `MAX_REACT_LOOPS = 3`.

### 2. Strategic Separation of Tools (Data Freshness vs. Latency)
- **Legal Context (RAG Component):** Corporate pricing documentation changes infrequently, making it highly suited for static, context-mined storage pipelines.
- **Operational Logs (MCP/DB Component):** Client infrastructure performance spikes alter by the minute. This application bypasses outdated cache vectors by querying live client JSON records directly through an active tool connector, balancing data accuracy against system performance requirements.

### 3. Least-Privilege Data Schemas
To ensure compliance boundaries, the client metric tool abstracts deep system infrastructure layers. The LLM is restricted from viewing underlying code logic, exposing only the minimum business variables necessary to complete a risk calculation.
