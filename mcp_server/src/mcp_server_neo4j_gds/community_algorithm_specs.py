from mcp import types

community_tool_definitions = [
    types.Tool(
        name="conductance",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "communityProperty": {
                    "type": "string",
                    "description": "The node property that holds the community ID as an integer for each node. "
                    "Note that only non-negative community IDs are considered valid and will have their conductance computed.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "The relationship property that holds the weight of the relationships. "
                    "If not provided, all relationships are considered to have a weight of 1.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run conductance on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run conductance on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["communityProperty"],
        },
    ),
    types.Tool(
        name="HDBSCAN",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodeProperty": {
                    "type": "string",
                    "description": "A node property corresponding to an array of floats used by HDBSCAN to compute clusters",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "minClusterSize": {
                    "type": "integer",
                    "description": "The minimum number of nodes that a cluster should contain.",
                },
                "samples": {
                    "type": "integer",
                    "description": "The number of neighbours to be considered when computing the core distances of a node.",
                },
                "leafSize": {
                    "type": "integer",
                    "description": "The number of leaf nodes of the supporting tree data structure.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run HDBSCAN on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
            },
            "required": ["nodeProperty"],
        },
    ),
    types.Tool(
        name="k_core_decomposition",
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
                    "description": "The node labels used to project and run K Core decomposition on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run K Core decomposition on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="k_1_coloring",
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
                    "description": "The node labels used to project and run K-1 Coloring on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run K-1 Coloring on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
                "maxIterations": {
                    "type": "integer",
                    "description": "The maximum number of iterations to run the coloring algorithm.",
                },
                "minCommunitySize": {
                    "type": "integer",
                    "description": "Only nodes inside communities larger or equal the given value are returned.",
                },
            },
            "required": [],
        },
    ),
    types.Tool(
        name="k_means_clustering",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "nodeProperty": {
                    "type": "string",
                    "description": "A node property corresponding to an array of floats used by K-Means to cluster nodes into communities.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "Property name to use for identifying nodes (e.g., 'name', 'Name', 'title'). Use get_node_properties_keys to find available properties.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run K-Means on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "k": {
                    "type": "integer",
                    "description": "The number of clusters to create.",
                },
                "maxIterations": {
                    "type": "integer",
                    "description": "The maximum number of iterations the algorithm will run.",
                },
                "deltaThreshold": {
                    "type": "number",
                    "description": "Value as a percentage to determine when to stop early. If fewer than 'deltaThreshold * |nodes|' nodes change their cluster , the algorithm stops. Value must be between 0 (exclusive) and 1 (inclusive).",
                },
                "numberOfRestarts": {
                    "type": "integer",
                    "description": "Number of times to execute K-Means with different initial centers. The communities returned are those minimizing the average node-center distances.",
                },
                "initialSampler": {
                    "type": "string",
                    "enum": ["uniform", "kmeans++"],
                    "description": "The method used to sample the first k centroids. 'uniform' and 'kmeans++', both case-insensitive, are valid inputs.",
                },
                "seedCentroids": {
                    "type": "array",
                    "items": {"type": "array", "items": {"type": "number"}},
                    "description": "Parameter to explicitly give the initial centroids. It cannot be enabled together with a non-default value of the numberOfRestarts parameter.",
                },
                "computeSilhouette": {
                    "type": "boolean",
                    "description": "If set to true, the silhouette scores are computed once the clustering has been determined. Silhouette is a metric on how well the nodes have been clustered.",
                },
            },
            "required": ["nodeProperty"],
        },
    ),
    types.Tool(
        name="label_propagation",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "maxIterations": {
                    "type": "integer",
                    "description": "The maximum number of iterations to run.",
                },
                "nodeWeightProperty": {
                    "type": "string",
                    "description": "The name of a node property that contains node weights.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "seedProperty": {
                    "type": "string",
                    "description": "The name of a node property that defines an initial numeric label.",
                },
                "consecutiveIds": {
                    "type": "boolean",
                    "description": "Flag to decide whether component identifiers are mapped into a consecutive id space (requires additional memory).",
                },
                "minCommunitySize": {
                    "type": "integer",
                    "description": "Only nodes inside communities larger or equal the given value are returned.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Label Propagation on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Label Propagation on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="leiden",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "maxLevels": {
                    "type": "integer",
                    "description": "The maximum number of levels in which the graph is clustered and then condensed.",
                },
                "gamma": {
                    "type": "number",
                    "description": "Resolution parameter used when computing the modularity. Internally the value is divided by the number of relationships for an unweighted graph, or the sum of weights of all relationships otherwise.",
                },
                "theta": {
                    "type": "number",
                    "description": "Controls the randomness while breaking a community into smaller ones.",
                },
                "tolerance": {
                    "type": "number",
                    "description": "Minimum change in modularity between iterations. If the modularity changes less than the tolerance value, the result is considered stable and the algorithm returns.",
                },
                "includeIntermediateCommunities": {
                    "type": "boolean",
                    "description": "Indicates whether to write intermediate communities. If set to false, only the final community is persisted.",
                },
                "seedProperty": {
                    "type": "string",
                    "description": "Used to set the initial community for a node. The property value needs to be a non-negative number.",
                },
                "minCommunitySize": {
                    "type": "integer",
                    "description": "Only nodes inside communities larger or equal the given value are returned.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Leiden on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Leiden on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="local_clustering_coefficient",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "triangleCountProperty": {
                    "type": "string",
                    "description": "Node property that contains pre-computed triangle count.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of node names to filter results. Only nodes whose names (based on nodeIdentifierProperty) contain any of these values will be included in the results. Requires nodeIdentifierProperty to be specified.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Local Clustering Coefficient on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Local Clustering Coefficient on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="louvain",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "seedProperty": {
                    "type": "string",
                    "description": "Used to set the initial community for a node. The property value needs to be a non-negative number.",
                },
                "maxLevels": {
                    "type": "integer",
                    "description": "The maximum number of levels in which the graph is clustered and then condensed.",
                },
                "maxIterations": {
                    "type": "integer",
                    "description": "The maximum number of iterations that the modularity optimization will run for each level.",
                },
                "tolerance": {
                    "type": "number",
                    "description": "Minimum change in modularity between iterations. If the modularity changes less than the tolerance value, the result is considered stable and the algorithm returns.",
                },
                "includeIntermediateCommunities": {
                    "type": "boolean",
                    "description": "Indicates whether to write intermediate communities. If set to false, only the final community is persisted.",
                },
                "consecutiveIds": {
                    "type": "boolean",
                    "description": "Flag to decide whether component identifiers are mapped into a consecutive id space (requires additional memory). Cannot be used in combination with the includeIntermediateCommunities flag.",
                },
                "minCommunitySize": {
                    "type": "integer",
                    "description": "Only nodes inside communities larger or equal the given value are returned.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Louvain on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Louvain on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="modularity_metric",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "communityProperty": {
                    "type": "string",
                    "description": "The node property that holds the community ID as an integer for each node. Note that only non-negative community IDs are considered valid and will have their modularity score computed.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Modularity on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Modularity on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
            "required": ["communityProperty"],
        },
    ),
    types.Tool(
        name="modularity_optimization",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "maxIterations": {
                    "type": "integer",
                    "description": "The maximum number of iterations to run.",
                },
                "tolerance": {
                    "type": "number",
                    "description": "Minimum change in modularity between iterations. If the modularity changes less than the tolerance value, the result is considered stable and the algorithm returns.",
                },
                "seedProperty": {
                    "type": "string",
                    "description": "Used to define initial set of labels.",
                },
                "consecutiveIds": {
                    "type": "boolean",
                    "description": "Flag to decide whether component identifiers are mapped into a consecutive id space (requires additional memory).",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "minCommunitySize": {
                    "type": "integer",
                    "description": "Only nodes inside communities larger or equal the given value are returned.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run modularity optimization on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run modularity optimization on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="strongly_connected_components",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "consecutiveIds": {
                    "type": "boolean",
                    "description": "Flag to decide whether component identifiers are mapped into a consecutive id space (requires additional memory).",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run SCC on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run SCC on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="triangle_count",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "maxDegree": {
                    "type": "integer",
                    "description": "If a node has a degree higher than this it will not be considered by the algorithm. The triangle count for these nodes will be -1.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of node names to filter results. Only nodes whose names (based on nodeIdentifierProperty) contain any of these values will be included in the results. Requires nodeIdentifierProperty to be specified.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Triangle Count on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Triangle Count on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="weakly_connected_components",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "Name of the relationship property to use as weights. If unspecified, the algorithm runs unweighted.",
                },
                "seedProperty": {
                    "type": "string",
                    "description": "Used to set the initial component for a node. The property value needs to be a number.",
                },
                "threshold": {
                    "type": "number",
                    "description": "The value of the weight above which the relationship is considered in the computation.",
                },
                "consecutiveIds": {
                    "type": "boolean",
                    "description": "Flag to decide whether component identifiers are mapped into a consecutive id space (requires additional memory).",
                },
                "minComponentSize": {
                    "type": "integer",
                    "description": "Only nodes inside communities larger or equal the given value are returned.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run WCC on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run WCC on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="approximate_maximum_k_cut",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "k": {
                    "type": "integer",
                    "description": "The number of disjoint communities the nodes will be divided into.",
                },
                "iterations": {
                    "type": "integer",
                    "description": "The number of iterations the algorithm will run before returning the best solution among all the iterations.",
                },
                "vnsMaxNeighborhoodOrder": {
                    "type": "integer",
                    "description": "The maximum number of nodes VNS will swap when perturbing solutions.",
                },
                "relationshipWeightProperty": {
                    "type": "string",
                    "description": "If set, the values stored at the given property are used as relationship weights during the computation. If not set, the graph is considered unweighted.",
                },
                "minCommunitySize": {
                    "type": "integer",
                    "description": "Only nodes inside communities larger or equal the given value are returned.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run Max-K-Cut  on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run Max-K-Cut on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
    types.Tool(
        name="speaker_listener_label_propagation",
        description="",
        inputSchema={
            "type": "object",
            "properties": {
                "maxIterations": {
                    "type": "integer",
                    "description": "Maximum number of iterations to run.",
                },
                "minAssociationStrength": {
                    "type": "number",
                    "description": "Minimum influence required for a community to retain a node.",
                },
                "partitioning": {
                    "type": "string",
                    "enum": ["AUTO", "RANGE", "DEGREE"],
                    "description": "The partitioning scheme used to divide the work between threads. Available options are AUTO, RANGE, DEGREE.",
                },
                "nodeIdentifierProperty": {
                    "type": "string",
                    "description": "The name of a node property to use as node identifier in the result. If provided, the result will include a 'nodeName' column with values from this property.",
                },
                "nodeLabels": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The node labels used to project and run SLLPA on. Nodes with different node labels will be ignored. Do not specify to run for all nodes",
                },
                "relTypes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The relationships types used to project and run SLLPA on. Relationship types of different type will be ignored. Do not specify to run for all relationship types",
                },
            },
        },
    ),
]
