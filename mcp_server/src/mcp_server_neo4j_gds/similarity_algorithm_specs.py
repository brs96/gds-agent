from mcp import types

similarity_tool_definitions = [
    types.Tool(
        name="node_similarity",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNodeFilter": {
                    "anyOf": [
                        {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        {
                            "type": "string",
                        },
                    ],
                },
                "targetNodeFilter": {
                    "anyOf": [
                        {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        {
                            "type": "string",
                        },
                    ],
                },
                "similarityCutoff": {
                    "type": "number",
                },
                "degreeCutoff": {
                    "type": "integer",
                },
                "upperDegreeCutoff": {
                    "type": "integer",
                },
                "topK": {
                    "type": "integer",
                },
                "bottomK": {
                    "type": "integer",
                },
                "topN": {
                    "type": "integer",
                },
                "bottomN": {
                    "type": "integer",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "similarityMetric": {
                    "type": "string",
                    "enum": ["JACCARD", "OVERLAP", "COSINE"],
                },
                "useComponents": {
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
        name="k_nearest_neighbors",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNodeFilter": {
                    "anyOf": [
                        {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        {
                            "type": "string",
                        },
                    ],
                },
                "targetNodeFilter": {
                    "anyOf": [
                        {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        {
                            "type": "string",
                        },
                    ],
                },
                "nodeProperties": {
                    "type": "object",
                },
                "topK": {
                    "type": "integer",
                },
                "sampleRate": {
                    "type": "number",
                },
                "deltaThreshold": {
                    "type": "number",
                },
                "maxIterations": {
                    "type": "integer",
                },
                "randomJoins": {
                    "type": "integer",
                },
                "initialSampler": {
                    "type": "string",
                    "enum": ["uniform", "randomWalk"],
                },
                "similarityCutoff": {
                    "type": "number",
                },
                "perturbationRate": {
                    "type": "number",
                },
                "seedTargetNodes": {
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
            "required": ["nodeProperties"],
        },
    ),
]
