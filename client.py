"""
Dynamic Tool Parameter Dependency Resolver and Context Injector.
Zero external dependencies, standard library only.
"""

import os
from typing import Dict, List, Any, Optional

class ToolParameterDependencyResolverClient:
    """
    Resolves dynamic parameters for tool execution:
    - Resolves environment variable placeholders ($ENV:KEY)
    - Injects session context variables ($SESSION:USER_ID)
    - Maps parameter cascades from prior step results
    """

    def __init__(self, session_context: Optional[Dict[str, Any]] = None):
        self.session = session_context or {}

    def resolve_parameters(self, raw_params: Dict[str, Any], step_outputs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Resolves all placeholders in raw_params dictionary."""
        outputs = step_outputs or {}
        resolved = {}

        for k, v in raw_params.items():
            if isinstance(v, str):
                if v.startswith("$ENV:"):
                    env_key = v[5:]
                    resolved[k] = os.environ.get(env_key, f"<MISSING_ENV:{env_key}>")
                elif v.startswith("$SESSION:"):
                    sess_key = v[9:]
                    resolved[k] = self.session.get(sess_key, f"<MISSING_SESSION:{sess_key}>")
                elif v.startswith("$STEP:"):
                    # Format $STEP:step_1.result_key
                    parts = v[6:].split(".", 1)
                    s_id = parts[0]
                    if s_id in outputs:
                        s_data = outputs[s_id]
                        if len(parts) > 1 and isinstance(s_data, dict):
                            resolved[k] = s_data.get(parts[1])
                        else:
                            resolved[k] = s_data
                    else:
                        resolved[k] = None
                else:
                    resolved[k] = v
            else:
                resolved[k] = v

        return resolved
