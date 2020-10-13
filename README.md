# Dijkstra

### Description:

an efficient algorithm for finding the shortest path from `source` node to `dest` node in a graph.
The run of the algorithm is portrayed via GUI interface that displays a minimum path from source node to destination node, and all the visited nodes

-------------------------------------------------------------------------------

### Main logic:
we run Dijkstra on a weighted graph, where each vertex is a "square" on the screen, an edge is a connection between two adjacent squared, and the weight is 1.
as an example, consider a 3x3 pixel grid:

![Capture](https://user-images.githubusercontent.com/45313790/95910432-bd81cf80-0da8-11eb-9c98-c9be880a2b4e.JPG)

a graph G=<V,E>, that represents the grid, is comprised of the following edges and vertexes (starting from (0,0)):

`V = ['(0,0)', '(0,1)', '(0,2)', '(1,0)', '(1,1)', '(1,2)', '(2,0)', '(2,1)', '(2,2)']`

`E = [('(0,0)', '(1,0)', 1), ('(0,0)', '(0,1)', 1), ('(0,1)', '(0,0)', 1),...,('(2,2)', '(2,1)', 1)]`

where `('(0,0)', '(1,0)', 1)`, for example, means that node (0,0) is connected to node (1,0) with an edge weighing 1.

also:

- the source and destination nodes are chosen by the user (two right clicks with the mouse)
- the user can "draw" (left mouse click) on the screen pixels that represents a node that doesnt exist, and therefore the algorithm wont use in runtime (these can be thought of as barriers, and they are colored black) 
  
 -------------------------------------------------------------------------------

### Running the Visuals :
under `Dijkstra.Main` execute `main()`

   example:
    
   ![rsz_95909766-b6a68d00-0da7-11eb-8727-a042ad20cb2e](https://user-images.githubusercontent.com/45313790/95911645-6bda4480-0daa-11eb-8856-638577e496d2.jpg)


- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `Minimum Path`
- ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) `Source Node`
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) `Destination Node`
- ![#000000](https://via.placeholder.com/15/000000/000000?text=+) `Blocked Nodes`
- ![#F18E14](https://via.placeholder.com/15/F18E14/000000?text=+) `Visited Nodes`
    
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
  
### Notes
- there are a few bugs, that I havent fixed yet. some of which may cause the algorithm to fail, while other will crash the screen when clicking on some certain position.


