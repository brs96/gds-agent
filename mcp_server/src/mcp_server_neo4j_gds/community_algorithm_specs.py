from mcp import types

community_tool_definitions = [
    types.Tool(
        name="conductance",
        inputSchema={
            "type": "object",
            "properties": {
                "communityProperty": {
                    "type": "string",
                },
                "relationshipWeightProperty": {
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
            "required": ["communityProperty"],
        },
    ),
    types.Tool(
        name="HDBSCAN",
        inputSchema={
            "type": "object",
            "properties": {
                "nodeProperty": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "minClusterSize": {
                    "type": "integer",
                },
                "samples": {
                    "type": "integer",
                },
                "leafSize": {
                    "type": "integer",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
            "required": ["nodeProperty"],
        },
    ),
    types.Tool(
        name="k_core_decomposition",
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
        name="k_1_coloring",
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
                "maxIterations": {
                    "type": "integer",
                },
                "minCommunitySize": {
                    "type": "integer",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="k_means_clustering",
        inputSchema={
            "type": "object",
            "properties": {
                "nodeProperty": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "k": {
                    "type": "integer",
                },
                "maxIterations": {
                    "type": "integer",
                },
                "deltaThreshold": {
                    "type": "number",
                },
                "numberOfRestarts": {
                    "type": "integer",
                },
                "initialSampler": {
                    "type": "string",
                    "enum": ["uniform", "kmeans++"],
                },
                "seedCentroids": {
                    "type": "array",
                    "items": {"type": "array", "items": {"type": "number"}},
                },
                "computeSilhouette": {
                    "type": "boolean",
                },
            },
            "required": ["nodeProperty"],
        },
    ),
    types.Tool(
        name="label_propagation",
        inputSchema={
            "type": "object",
            "properties": {
                "maxIterations": {
                    "type": "integer",
                },
                "nodeWeightProperty": {
                    "type": "string",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "seedProperty": {
                    "type": "string",
                },
                "consecutiveIds": {
                    "type": "boolean",
                },
                "minCommunitySize": {
                    "type": "integer",
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
            },
        },
    ),
    types.Tool(
        name="leiden",
        inputSchema={
            "type": "object",
            "properties": {
                "maxLevels": {
                    "type": "integer",
                },
                "gamma": {
                    "type": "number",
                },
                "theta": {
                    "type": "number",
                },
                "tolerance": {
                    "type": "number",
                },
                "includeIntermediateCommunities": {
                    "type": "boolean",
                },
                "seedProperty": {
                    "type": "string",
                },
                "minCommunitySize": {
                    "type": "integer",
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
            },
        },
    ),
    types.Tool(
        name="local_clustering_coefficient",
        inputSchema={
            "type": "object",
            "properties": {
                "triangleCountProperty": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
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
            },
        },
    ),
    types.Tool(
        name="louvain",
        inputSchema={
            "type": "object",
            "properties": {
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "seedProperty": {
                    "type": "string",
                },
                "maxLevels": {
                    "type": "integer",
                },
                "maxIterations": {
                    "type": "integer",
                },
                "tolerance": {
                    "type": "number",
                },
                "includeIntermediateCommunities": {
                    "type": "boolean",
                },
                "consecutiveIds": {
                    "type": "boolean",
                },
                "minCommunitySize": {
                    "type": "integer",
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
            },
        },
    ),
    types.Tool(
        name="modularity_metric",
        inputSchema={
            "type": "object",
            "properties": {
                "communityProperty": {
                    "type": "string",
                },
                "relationshipWeightProperty": {
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
            "required": ["communityProperty"],
        },
    ),
    types.Tool(
        name="modularity_optimization",
        inputSchema={
            "type": "object",
            "properties": {
                "maxIterations": {
                    "type": "integer",
                },
                "tolerance": {
                    "type": "number",
                },
                "seedProperty": {
                    "type": "string",
                },
                "consecutiveIds": {
                    "type": "boolean",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "minCommunitySize": {
                    "type": "integer",
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
            },
        },
    ),
    types.Tool(
        name="strongly_connected_components",
        inputSchema={
            "type": "object",
            "properties": {
                "consecutiveIds": {
                    "type": "boolean",
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
            },
        },
    ),
    types.Tool(
        name="triangle_count",
        inputSchema={
            "type": "object",
            "properties": {
                "maxDegree": {
                    "type": "integer",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
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
            },
        },
    ),
    types.Tool(
        name="weakly_connected_components",
        inputSchema={
            "type": "object",
            "properties": {
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "seedProperty": {
                    "type": "string",
                },
                "threshold": {
                    "type": "number",
                },
                "consecutiveIds": {
                    "type": "boolean",
                },
                "minComponentSize": {
                    "type": "integer",
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
            },
        },
    ),
    types.Tool(
        name="approximate_maximum_k_cut",
        inputSchema={
            "type": "object",
            "properties": {
                "k": {
                    "type": "integer",
                },
                "iterations": {
                    "type": "integer",
                },
                "vnsMaxNeighborhoodOrder": {
                    "type": "integer",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "minCommunitySize": {
                    "type": "integer",
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
            },
        },
    ),
    types.Tool(
        name="speaker_listener_label_propagation",
        inputSchema={
            "type": "object",
            "properties": {
                "maxIterations": {
                    "type": "integer",
                },
                "minAssociationStrength": {
                    "type": "number",
                },
                "partitioning": {
                    "type": "string",
                    "enum": ["AUTO", "RANGE", "DEGREE"],
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
            },
        },
    ),
]
