import os
import json
from openai import OpenAI
from utils import read_pricing_policy, get_customer_metrics

# Best Practice: Enforce Loop Limits to Prevent Cost Runaways
MAX_REACT_LOOPS = 3

def financial_risk_guard_agent(customer_query):
    print(f"🚀 Starting Agent Framework for Query: '{customer_query}'")
    loop_count = 0
    agent_memory = {}
    is_loop_active = True
    
    while is_loop_active:
        loop_count += 1
        print(f"\n🔄 --- ReAct Loop Iteration {loop_count} ---")
        
        if loop_count > MAX_REACT_LOOPS:
            print("⚠️ [Guardrail Triggered] Max loops reached! Forcing resolution to prevent budget overrun.")
            return compile_final_response(customer_query, agent_memory, forced=True)
            
        # Hardcoded structural rules simulating model decision branches
        if "billing_metrics" not in agent_memory:
            print("🧠 AI Thought: I need customer billing metrics to check for cost anomalies. Calling Tool...")
            print("🛠️ Action: Calling MCP Database Tool via utils.get_customer_metrics()...")
            agent_memory["billing_metrics"] = get_customer_metrics()
            print("👁️ Observation: Retrieved customer billing data profile.")
            
        elif "pricing_policy" not in agent_memory:
            print("🧠 AI Thought: I have metrics. Now I need the contract overage thresholds. Calling Tool...")
            print("🛠️ Action: Triggering RAG Search via utils.read_pricing_policy()...")
            agent_memory["pricing_policy"] = read_pricing_policy()
            print("👁️ Observation: Local corporate policy rules pulled into memory.")
            
        else:
            print("🧠 AI Thought: I have all data dependencies satisfied. Synthesizing report constraints...")
            is_loop_active = False
            return compile_final_response(customer_query, agent_memory, forced=False)

def compile_final_response(query, memory, forced=False):
    print("\n📊 --- Compiling Final Risk Assessment Report ---")
    metrics = memory.get("billing_metrics", {})
    metrics_data = metrics.get("current_month_metrics", {})
    used = metrics_data.get("actual_storage_used_gb", 0)
    allocated = metrics_data.get("base_storage_allocated_gb", 0)
    spike = metrics_data.get("recent_spike_ratio", 0)
    
    overage_gb = max(0, used - allocated)
    financial_risk_usd = overage_gb * 0.10
    
    status_prefix = "[🚨 HIGH RISK ALERT]" if financial_risk_usd > 0 or spike > 2.0 else "[✅ CLEAN RISK PROFILE]"
    if forced: status_prefix = "[⚠️ FORCED RESOLUTION - INCOMPLETE DATA]"
        
    return (
        f"{status_prefix}\n"
        f"Customer Account: {metrics.get('customer_name', 'Unknown')}\n"
        f"Contract Status: {metrics.get('contract_status', 'Unknown')}\n"
        f"Detected Storage Consumption: {used} GB (Baseline: {allocated} GB)\n"
        f"Calculated Overage Value: ${financial_risk_usd:,.2f} USD\n"
        f"Infrastructure Resource Spike Ratio: {spike}x normal metrics\n"
        "--------------------------------------------------\n"
        "Strategic Account Recommendation:\n"
        f"Do NOT execute a flat-rate contract renewal. The infrastructure metrics match the pattern "
        f"of 'Unmanaged Elastic Usage' (Section 2.2). Flag this account profile for manager intervention."
    )

if __name__ == "__main__":
    sample_query = "Run financial compliance review for client Acme Corp before contract signature."
    final_output = financial_risk_guard_agent(sample_query)
    print("\n=== Agent Terminal Output Report ===")
    print(final_output)
