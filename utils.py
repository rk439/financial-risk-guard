import json
import os

# Get the exact folder where this python script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_pricing_policy():
    """Reads contract policies using an absolute cloud path."""
    policy_path = os.path.join(BASE_DIR, "data", "policies", "pricing_policy.txt")
    if os.path.exists(policy_path):
        with open(policy_path, "r") as f:
            return f.read()
    return "Policy file not found."

def get_customer_metrics():
    """Pulls live customer metrics using an absolute cloud path."""
    metrics_path = os.path.join(BASE_DIR, "data", "billing_logs", "acme_corp_metrics.json")
    if os.path.exists(metrics_path):
        with open(metrics_path, "r") as f:
            return json.load(f)
    return {
        "customer_name": "Acme Corp (Fallback)",
        "contract_status": "Pending Renewal",
        "current_month_metrics": {
            "base_storage_allocated_gb": 5000,
            "actual_storage_used_gb": 7200,
            "recent_spike_ratio": 2.5
        }
    }
