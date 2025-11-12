from mcp import types

path_tool_definitions = [
    types.Tool(
        name="find_shortest_path",
        inputSchema={
            "type": "object",
            "properties": {
                "start_node": {
                    "type": "string",
                },
                "end_node": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "relationship_property": {
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
            "required": ["start_node", "end_node", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="delta_stepping_shortest_path",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "delta": {
                    "type": "number",
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
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="dijkstra_single_source_shortest_path",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
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
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="a_star_shortest_path",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                },
                "targetNode": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "latitudeProperty": {
                    "type": "string",
                },
                "longitudeProperty": {
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
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                },
                "targetNode": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "k": {
                    "type": "integer",
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
            "required": ["sourceNode", "targetNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="minimum_weight_spanning_tree",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "objective": {
                    "type": "string",
                    "enum": ["minimum", "maximum"],
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
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="minimum_directed_steiner_tree",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                },
                "targetNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "delta": {
                    "type": "number",
                },
                "applyRerouting": {
                    "type": "boolean",
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
            "required": ["sourceNode", "targetNodes", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="prize_collecting_steiner_tree",
        inputSchema={
            "type": "object",
            "properties": {
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "prizeProperty": {
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
            "required": ["prizeProperty"],
        },
    ),
    types.Tool(
        name="all_pairs_shortest_paths",
        inputSchema={
            "type": "object",
            "properties": {
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
            "required": [],
        },
    ),
    types.Tool(
        name="random_walk",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "walkLength": {
                    "type": "integer",
                },
                "walksPerNode": {
                    "type": "integer",
                },
                "inOutFactor": {
                    "type": "number",
                },
                "returnFactor": {
                    "type": "number",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                },
                "walkBufferSize": {
                    "type": "integer",
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
        name="breadth_first_search",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "targetNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "maxDepth": {
                    "type": "integer",
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
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="depth_first_search",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                },
                "targetNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "maxDepth": {
                    "type": "integer",
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
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="bellman_ford_single_source_shortest_path",
        inputSchema={
            "type": "object",
            "properties": {
                "sourceNode": {
                    "type": "string",
                },
                "nodeIdentifierProperty": {
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
            "required": ["sourceNode", "nodeIdentifierProperty"],
        },
    ),
    types.Tool(
        name="longest_path",
        inputSchema={
            "type": "object",
            "properties": {
                "targetNodes": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "nodeIdentifierProperty": {
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
            "required": [],
        },
    ),
]
