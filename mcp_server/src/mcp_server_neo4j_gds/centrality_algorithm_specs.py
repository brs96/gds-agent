from mcp import types

centrality_tool_definitions = [
    types.Tool(
        name="article_rank",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "dampingFactor": {
                    "type": "number",
                },
                "maxIterations": {
                    "type": "integer",
                },
                "tolerance": {
                    "type": "number",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "sourceNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "scaler": {
                    "type": "string",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="articulation_points",
        inputSchema={
            "type": "object",
            "properties": {
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="betweenness_centrality",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "samplingSize": {
                    "type": "integer",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="bridges",
        inputSchema={
            "type": "object",
            "properties": {
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="CELF",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "seedSetSize": {
                    "type": "integer",
                },
                "monteCarloSimulations": {
                    "type": "integer",
                },
                "propagationProbability": {
                    "type": "number",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
            },
            "required": ["seedSetSize"],
        },
    ),
    types.Tool(
        name="closeness_centrality",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "useWassermanFaust": {
                    "type": "boolean",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="degree_centrality",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "orientation": {
                    "type": "string",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="eigenvector_centrality",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "maxIterations": {
                    "type": "integer",
                },
                "tolerance": {
                    "type": "number",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "sourceNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "scaler": {
                    "type": "string",
                },
            },
        },
    ),
    types.Tool(
        name="pagerank",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "dampingFactor": {
                    "type": "number",
                },
                "maxIterations": {
                    "type": "integer",
                },
                "tolerance": {
                    "type": "number",
                },
                "sourceNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="harmonic_centrality",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="HITS",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "hitsIterations": {
                    "type": "integer",
                },
                "authProperty": {
                    "type": "string",
                },
                "hubProperty": {
                    "type": "string",
                },
                "partitioning": {
                    "type": "string",
                    "enum": ["AUTO", "RANGE", "DEGREE"],
                },
            },
            "required": [],
        },
    ),
]
