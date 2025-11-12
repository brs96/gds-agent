from mcp import types

similarity_tool_definitions = [
    types.Tool(
        name="node_similarity",
        description="",
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
                    "description": "The source node filter to apply. Accepts a List of node names, or a single label.",
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
                    "description": "The target node filter to apply. Accepts a List of node names, or a single label.",
                },
                "similarityCutoff": {
                    "type": "number",
                    "description": "Lower limit for the similarity score to be present in the result. Values must be between 0 and 1.",
                },
                "degreeCutoff": {
                    "type": "integer",
                    "description": "Inclusive lower bound on the node degree for a node to be considered in the comparisons. This value can not be lower than 1.",
                },
                "upperDegreeCutoff": {
                    "type": "integer",
                    "description": "Inclusive upper bound on the node degree for a node to be considered in the comparisons. This value can not be lower than 1.",
                },
                "topK": {
                    "type": "integer",
                    "description": "Limit on the number of scores per node. The K largest results are returned. This value cannot be lower than 1. Use this instead of topN whenever the sourceNode consists of a single node, or it is specifically stated that results are to be computed for each source node",
                },
                "bottomK": {
                    "type": "integer",
                    "description": "Limit on the number of scores per node. The K smallest results are returned. This value cannot be lower than 1.",
                },
                "topN": {
                    "type": "integer",
                    "description": "Global limit on the number of scores computed. The N largest total results are returned. This value cannot be negative, a value of 0 means no global limit.",
                },
                "bottomN": {
                    "type": "integer",
                    "description": "Global limit on the number of scores computed. The N smallest total results are returned. This value cannot be negative, a value of 0 means no global limit.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "similarityMetric": {
                    "type": "string",
                    "enum": ["JACCARD", "OVERLAP", "COSINE"],
                    "description": "The metric used to compute similarity.",
                },
                "useComponents": {
                    "type": "boolean",
                    "description": "If enabled, Node Similarity will use components to improve the performance of the computation, skipping comparisons of nodes in different components. Set to false (Default): the algorithm does not use components, but computes similarity across the entire graph. Set to true: the algorithm uses components, and will compute these components before computing similarity. Set to String: use pre-computed components stored in graph, String is the key for a node property representing components.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Node Similarity on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Node Similarity on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="k_nearest_neighbors",
        description="",
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
                    "description": "The source node filter to apply. Accepts a List of node names, or a single label.",
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
                    "description": "The target node filter to apply. Accepts a List of node names, or a single label.",
                },
                "nodeProperties": {
                    "type": "object",
                    "description": "The node properties to use for similarity computation along with their selected similarity metrics. Accepts a Map of property keys to metrics. For example: {embedding: 'COSINE',age: 'DEFAULT',lotteryNumbers: 'OVERLAP'}. DEFAULT refers to COSINE.",
                },
                "topK": {
                    "type": "integer",
                    "description": "The number of neighbors to find for each node. The K-nearest neighbors are returned. This value cannot be lower than 1.",
                },
                "sampleRate": {
                    "type": "number",
                    "description": "Sample rate to limit the number of comparisons per node. Value must be between 0 (exclusive) and 1 (inclusive).",
                },
                "deltaThreshold": {
                    "type": "number",
                    "description": "Value as a percentage to determine when to stop early. If fewer updates than the configured value happen, the algorithm stops. Value must be between 0 (exclusive) and 1 (inclusive).",
                },
                "maxIterations": {
                    "type": "integer",
                    "description": "Hard limit to stop the algorithm after that many iterations.",
                },
                "randomJoins": {
                    "type": "integer",
                    "description": "The number of random attempts per node to connect new node neighbors based on random selection, for each iteration.",
                },
                "initialSampler": {
                    "type": "string",
                    "enum": ["uniform", "randomWalk"],
                    "description": 'The method used to sample the first k random neighbors for each node. "uniform" and "randomWalk", both case-insensitive, are valid inputs.',
                },
                "similarityCutoff": {
                    "type": "number",
                    "description": "Filter out from the list of K-nearest neighbors nodes with similarity below this threshold.",
                },
                "perturbationRate": {
                    "type": "number",
                    "description": "The probability of replacing the least similar known neighbor with an encountered neighbor of equal similarity.",
                },
                "seedTargetNodes": {
                    "type": "boolean",
                    "description": "Enable seeding of target nodes. If seeded, every node picks some of the target nodes initially. This guarantees that for every node we can avoid empty result (when the algorithm did not find for it any similar neighbors from the target set). Can only be used if targetNodeFilter is set.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run k-nearest neighbors on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run k-nearest neighbors on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["nodeProperties"],
        },
    ),
]
