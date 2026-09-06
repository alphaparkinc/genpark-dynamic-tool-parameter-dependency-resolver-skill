"""
Demonstration of genpark-dynamic-tool-parameter-dependency-resolver-skill
"""

import os
from client import ToolParameterDependencyResolverClient

def main():
    os.environ["API_GATEWAY_TOKEN"] = "token_xyz999"

    resolver = ToolParameterDependencyResolverClient(session_context={"account_id": "acc_7741"})

    prior_outputs = {
        "step_auth": {"auth_ticket": "ticket_abc123", "expires_in": 3600}
    }

    raw_tool_params = {
        "api_key": "$ENV:API_GATEWAY_TOKEN",
        "account": "$SESSION:account_id",
        "ticket": "$STEP:step_auth.auth_ticket",
        "timeout": 30
    }

    resolved = resolver.resolve_parameters(raw_tool_params, prior_outputs)
    print("=== RESOLVED PARAMETERS ===")
    for k, v in resolved.items():
        print(f"{k} -> {v}")

if __name__ == "__main__":
    main()
