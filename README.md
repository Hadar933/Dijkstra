# Dijkstra

### Description:

an efficient algorithm for finding the shortest path from `source` node to the rest of the nodes in a graph
as well as a GUI interface that displays a minimum path from source node to destination node, and all the visited nodes

-------------------------------------------------------------------------------

### Running the algorithm (example) :

    edges = [("A", "B", 1), ("A", "C", 1),
             ("B", "A", 1), ("B", "C", 2), ("B", "D", 3), ("B", "E", 4),
             ("C", "A", 1), ("C", "B", 2), ("C", "D", 1),
             ("D", "C", 1), ("D", "B", 3), ("D", "E", 2), ("D", "F", 2),
             ("E", "B", 4), ("E", "D", 2), ("E", "F", 1),
             ("F", "E", 1), ("F", "D", 2)]

    graph = Graph(edges)
    source_node = graph.get_vertexes()["A"]
    dijkstra(graph, source_node)
    print_min_distances(graph, source_node.name)
  
-------------------------------------------------------------------------------
  
### complexity analysis
  (not rigorously):
  ![Capture](https://user-images.githubusercontent.com/45313790/95630833-36bcb200-0a8b-11eb-8417-f91872504541.JPG)

    
    
    Dijkstra:
    source.set_dist_from_source(0)
    Q = build_min_heap(graph)  # O(V)
    while Q:  # O(V)
        u = heapq.heappop(Q)  # pops the min val (get value and remove from heap) O(logV)
        neighbors_of_u = graph.get_neighbors()[u.name]
        for v in neighbors_of_u:  # O(E)
            weight_u_v = graph.get_edge_weight(u.name, v.name)
            v_dist = v.dist_from_source
            u_dist = u.dist_from_source
            if v_dist > u_dist + weight_u_v:
                v.set_dist_from_source(u_dist + weight_u_v)
                heapq.heappush(Q, v)  # O(logV)
 -------------------------------------------------------------------------------

### Running the Visuals :
    under `Dijkstra.Main` execute `main()`
    example:
    
   
 -------------------------------------------------------------------------------

### Notes

a visualization of the graph is available:
given variable `edges` from above, use `visualize_graph(edges)`
![Webp net-resizeimage (1)](https://user-images.githubusercontent.com/45313790/95631881-20175a80-0a8d-11eb-8d27-86c6ffe04451.jpg)


