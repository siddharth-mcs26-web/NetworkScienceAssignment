# Network Science Assignment

The function Calculate_eccentricity(nodes, edges, node=None) is the main function for calculating the eccentricity centrality

### Function inputs are : nodes, edges, node

#### nodes -> a list of nodes should be provided i.e [1,2,3,4]
#### edges -> a list containing nodes which have edge between them i.e [(1,2),(2,3)]
#### node -> if want to calculate the eccentricity of a single then provide the argument otherwise all nodes centrality and eccentricity will be provided

### Function output are eccentricity_centrality, eccentricity
#### eccentricity_centrality -> for all nodes (without node argument) it is dictionary having nodes as key and values as centrality, for a single node (with node argument) it is a value centrality of that node
#### eccentricity -> for all nodes (without node argument) it is dictionary having nodes as key and values as eccentricity, for a single node (with node argument) it is a value centrality of that node


### Assumptions
#### 1. The network is a connected network

### Execution instructions
#### 1. Call the function Calculate_eccentricity(nodes, edges, node) with required arguments
#### 2. The function provides two return values eccentricity_centrality, eccentricity
#### 3. To capture output of the function call the function like eccentricity_centrality, eccentricity = Calculate_eccentricity(node, edges, node)

