from mcp import types

centrality_tool_definitions = [
    types.Tool(
        name="article_rank",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of node to filter return the ArticleRank for.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "dampingFactor": {
                    "type": "number",
                    "description": "The damping factor of the ArticleRank calculation. Must be in [0, 1).",
                },
                "maxIterations": {
                    "type": "integer",
                    "description": "Maximum number of iterations for ArticleRank",
                },
                "tolerance": {
                    "type": "number",
                    "description": "Minimum change in scores between iterations.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Property of the relationship to use for weighting. If not specified, all relationships are treated equally.",
                },
                "sourceNodes": {
                    "description": "The nodes to use for computing Personalized Article Rank.",
                    "type": "array",
                    "items": {"type": "string"},
                },
                "scaler": {
                    "type": "string",
                    "description": "The name of the scaler applied for the final scores. "
                    "Supported values are None, MinMax, Max, Mean, Log, and StdScore. "
                    "To apply scaler-specific configuration, use the Map syntax: {scaler: 'name', ...}.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run the article rank on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run article rank on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="articulation_points",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Articulation points on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Articulation Points on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="betweenness_centrality",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of node names to filter betweenness centrality results for.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Betweenness Centrality on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Betweenness Centrality on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "samplingSize": {
                    "type": "integer",
                    "description": "The number of source nodes to consider for computing centrality scores.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Property of the relationship to use for weighting. If not specified, all relationships are treated equally.",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="bridges",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Bridges on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Bridges on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
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
                    "description": "The node labels used to project and run CELF on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run CELF on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "seedSetSize": {
                    "type": "integer",
                    "description": "The number of nodes that maximize the expected spread in the network.",
                },
                "monteCarloSimulations": {
                    "type": "integer",
                    "description": "The number of Monte Carlo simulations to run for estimating the expected spread.",
                },
                "propagationProbability": {
                    "type": "number",
                    "description": "The probability of propagating influence from a node to its neighbors.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
            },
            "required": ["seedSetSize"],
        },
    ),
    types.Tool(
        name="closeness_centrality",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of node names to filter closeness centrality results for.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run closeness centrality on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run closeness centrality on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "useWassermanFaust": {
                    "type": "boolean",
                    "description": "If true, uses the Wasserman-Faust formula for closeness centrality. ",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="degree_centrality",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of node names to filter degree centrality results for.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Degree Centrality on. This is used to filter the graph to run the algorithm on. Nodes with other node labels will be hidden and ignored. Include all node labels for nodes that you want to run the algorithm on.",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Degree Centrality on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "orientation": {
                    "type": "string",
                    "description": "The orientation used to compute node degrees. Supported orientations are NATURAL (for out-degree), REVERSE (for in-degree) and UNDIRECTED (for both in-degree and out-degree) ",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Property of the relationship to use for weighting. If not specified, all relationships are treated equally.",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="eigenvector_centrality",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of node names to filter eigenvector centrality results for.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run eigenvector centrality on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run eigenvector centrality on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "maxIterations": {
                    "type": "integer",
                    "description": "Maximum number of iterations for Eigenvector Centrality",
                },
                "tolerance": {
                    "type": "number",
                    "description": "Minimum change in scores between iterations. If all scores change less than the tolerance value the result is considered stable and the algorithm returns.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Property of the relationship to use for weighting. If not specified, all relationships are treated equally.",
                },
                "sourceNodes": {
                    "description": "The nodes to use for computing Personalized Eigenvector Centrality.",
                    "type": "array",
                    "items": {"type": "string"},
                },
                "scaler": {
                    "type": "string",
                    "description": "The name of the scaler applied for the final scores. "
                    "Supported values are None, MinMax, Max, Mean, Log, and StdScore. "
                    "To apply scaler-specific configuration, use the Map syntax: {scaler: 'name', ...}.",
                },
            },
        },
    ),
    types.Tool(
        name="pagerank",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of node names to filter PageRank results for.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run PageRank on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run PageRank on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "dampingFactor": {
                    "type": "number",
                    "description": "The damping factor of the Page Rank calculation. Must be in [0, 1).",
                },
                "maxIterations": {
                    "type": "integer",
                    "description": "Maximum number of iterations for PageRank",
                },
                "tolerance": {
                    "type": "number",
                    "description": "Minimum change in scores between iterations. If all scores change less than the tolerance value the result is considered stable and the algorithm returns.",
                },
                "sourceNodes": {
                    "description": "The nodes to use for computing Personalized PageRank.",
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="harmonic_centrality",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of node names to filter harmonic centrality results for.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run harmonic centrality on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run harmonic centrality on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="HITS",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of node names to filter HITS results for.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run hits on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run hits on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "hitsIterations": {
                    "type": "integer",
                    "description": "The number of hits iterations to run. The number of pregel iterations will be equal to hitsIterations * 4.",
                },
                "authProperty": {
                    "type": "string",
                    "description": "The name of the auth property to use.",
                },
                "hubProperty": {
                    "type": "string",
                    "description": "The name of the hub property to use.",
                },
                "partitioning": {
                    "type": "string",
                    "enum": ["AUTO", "RANGE", "DEGREE"],
                    "description": "The partitioning scheme used to divide the work between threads. Available options are AUTO, RANGE, DEGREE.",
                },
            },
            "required": [],
        },
    ),
]
