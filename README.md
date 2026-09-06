# GenPark AI Agent Skill - Dynamic Tool Parameter Resolver

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Dynamic parameter dependency resolver and secret injector for composite agent workflows.

```mermaid
flowchart LR
    A[Raw Tool Parameter Template] --> B[Resolver Engine]
    B -->|Fetch Environment| C[$ENV:API_KEY]
    B -->|Fetch Session State| D[$SESSION:USER_ID]
    B -->|Fetch Prior Step Output| E[$STEP:prior.field]
    C & D & E --> F[Fully Materialized Tool Arguments]
```

## Features
- **Context Placeholders**: Resolves `$ENV:`, `$SESSION:`, and `$STEP:` tokens cleanly.
- **Zero External Dependencies**: Standard library Python 3.9+.

## Quickstart
```python
from client import ToolParameterDependencyResolverClient

resolver = ToolParameterDependencyResolverClient({"user": "alice"})
params = resolver.resolve_parameters({"user": "$SESSION:user"})
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
