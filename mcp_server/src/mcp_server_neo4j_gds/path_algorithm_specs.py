from mcp import types

path_tool_definitions = [
    types.Tool(
        name="find_shortest_path",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "start_node": {
                    "type": "string",
                    "description": "Name of the starting node",
                },
                "end_node": {
                    "type": "string",
                    "description": "Name of the ending node",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "relationship_property": {
                    "type": "string",
                    "description": "Property of the relationship to use for path finding",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Dijkstra on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Dijkstra on on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["start_node", "end_node", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="delta_stepping_shortest_path",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                    "description": "Name of the source node to find shortest paths from.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "delta": {
                    "type": "number",
                    "description": "The bucket width for grouping nodes with the same tentative distance to the source node.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Delta-Stepping on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Delta-Stepping on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="dijkstra_single_source_shortest_path",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                    "description": "Name of the source node to find shortest paths from.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Dijkstra on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Dijkstra on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="a_star_shortest_path",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                    "description": "Name of the source node to find shortest path from.",
                },
                "targetNode": {
                    "type": "string",
                    "description": "Name of the target node to find shortest path to.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "latitudeProperty": {
                    "type": "string",
                    "description": "The node property that stores the latitude value.",
                },
                "longitudeProperty": {
                    "type": "string",
                    "description": "The node property that stores the longitude value.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run A* on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run A* on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": [
                "sourceNode",
                "targetNode",
                "nodeIdentifierProperty",
                "latitudeProperty",
                "longitudeProperty",
            ],
        },
    ),
    types.Tool(
        name="yens_shortest_paths",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                    "description": "Name of the source node to find shortest paths from.",
                },
                "targetNode": {
                    "type": "string",
                    "description": "Name of the target node to find shortest paths to.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "k": {
                    "type": "integer",
                    "description": "The number of shortest paths to compute between source and target node.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Yens on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Yens on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["sourceNode", "targetNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="minimum_weight_spanning_tree",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                    "description": "Name of the starting source node.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "objective": {
                    "type": "string",
                    "enum": ["minimum", "maximum"],
                    "description": "If specified, the parameter dictates whether to find the minimum or the maximum weight spanning tree. By default, a minimum weight spanning tree is returned. Permitted values are 'minimum' and 'maximum'.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Prim on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Prim on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="minimum_directed_steiner_tree",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                    "description": "Name of the starting source node.",
                },
                "targetNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of target node names to connect in the steiner tree.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "delta": {
                    "type": "number",
                    "description": "The bucket width for grouping nodes with the same tentative distance to the source node. Look into the Delta-Stepping documentation for more information.",
                },
                "applyRerouting": {
                    "type": "boolean",
                    "description": "If specified, the algorithm will try to improve the outcome via an additional post-processing heuristic.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Steiner-Tree on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Steiner-Tree on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["sourceNode", "targetNodes", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="prize_collecting_steiner_tree",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "prizeProperty": {
                    "type": "string",
                    "description": "The name of node property that denotes a node's prize.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Prize Collecting Steiner Tree on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Prize Collecting Steiner Tree on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["prizeProperty"],
        },
    ),
    types.Tool(
        name="all_pairs_shortest_paths",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run APSP on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run APSP on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="random_walk",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The list of nodes from which to do a random walk.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "walkLength": {
                    "type": "integer",
                    "description": "The number of steps in a single random walk.",
                },
                "walksPerNode": {
                    "type": "integer",
                    "description": "The number of random walks generated for each node.",
                },
                "inOutFactor": {
                    "type": "number",
                    "description": "Tendency of the random walk to stay close to the start node or fan out in the graph. Higher value means stay local.",
                },
                "returnFactor": {
                    "type": "number",
                    "description": "Tendency of the random walk to return to the last visited node. A value below 1.0 means a higher tendency.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights to influence the probabilities of the random walks. The weights need to be >= 0. If unspecified, the algorithm runs unweighted.",
                },
                "walkBufferSize": {
                    "type": "integer",
                    "description": "The number of random walks to complete before starting training.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Random Walk on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Random Walk on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="breadth_first_search",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                    "description": "Name of the starting source node.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "targetNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Names of target nodes. Traversal terminates when any target node is visited.",
                },
                "maxDepth": {
                    "type": "integer",
                    "description": "The maximum distance from the source node at which nodes are visited.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run BFS on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run BFS on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="depth_first_search",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                    "description": "Name of the starting source node.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "targetNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Names of target nodes. Traversal terminates when any target node is visited.",
                },
                "maxDepth": {
                    "type": "integer",
                    "description": "The maximum distance from the source node at which nodes are visited.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run DFS on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run DFS on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="bellman_ford_single_source_shortest_path",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                    "description": "Name of the starting source node.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Bellman-Ford on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Bellman-Ford on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="longest_path",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "targetNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of target node names to filter results. Only paths ending at these nodes will be returned.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties. Required when targetNodes is specified.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run longest path on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run longest path on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": [],
        },
    ),
]
