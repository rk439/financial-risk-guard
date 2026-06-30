import json
import os

def read_pricing_policy():
    """Simulates a RAG document fetcher reading our contract policies."""
    policy_path = os.path.join("data", "policies", "pricing_policy.txt")
    if os.path.exists(policy_path):
        with open(policy_path, "r") as f:
            return f.read()
    return "Policy file not found."

def get_customer_metrics():
    """Simulates an MCP database tool pulling live metrics."""
    metrics_path = os.path.join("data", "billing_logs", "acme_corp_metrics.json")
    if os.path.exists(metrics_path):
        with open(metrics_path, "r") as f:
            return json.load(f)
    return {}
