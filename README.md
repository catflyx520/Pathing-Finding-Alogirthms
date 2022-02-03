# PathingFiding-Alogirthm
Using python to implment alogrithms of Breadth-First search, Depth-First search, Greedy search, and A* search. A graph function to create graphs (provided by professor) and using path finding function to find the closest path to reach destination. We can see the different results of all the algorithms mentioned above. 
My first Python project and learning Python for the first time. Struggle a lot with the project since it is pretty hard for me as a Python newbee. 

I used lists to implement the BFS algorithm, and I used the stack to implement DFS algorithms. For the DFS algorithm, I used a while loop to check if the frontier is empty or
not, and a for loop to add the neighbors of the expanded node. The BFS algorithm loops are pretty similar to DFS loops except the BFS algorithm expands all the neighbors whereas the DFS algorithm only expands one neighbor at each iteration. Some of the challenges when doing BFS and DFS are that it took me a while to get started since I am new to Python. I spend a while understanding how the graph functions, nodes, and edges are working. It is hard to expand all the nodes at the same time as it causes many errors within the loop. We used PriorityQueue()to implement the Greedy and A* algorithms since they both implemented a heuristic. This resulted in some problems when there were two nodes with the same heuristic because the PriorityQueue would then compare the next argument in our Queue, which was originally the node itself. We would then get an error because we were trying to compare two nodes. To fix this, we added an integer to our queue, so that when the heuristics were the same, the PriorityQueue would then compare the integer instead of the nodes. To avoid loops in the BFS algorithm, before adding the cost and expanding a node we check if we have already expanded that node before (so that the same node won’t keep getting expanded). For testing purposes, we put a time limit for running the algorithm, if it passes a certain time, then we assume we cannot find the path to the target.

2.In the testing for the Austria graph, I found that the DFS and BFS algorithms expanded and visited the same amount of nodes. However, the BFS algorithm ended up with a larger cost because the total cost included the costs of all the neighbors of the nodes that were expanded. The largest cost ended up being the greedy algorithm using the default heuristic. Because the default heuristic was 0, the PriorityQueue compares the integer in Frontier[], which is set to the visited_counter. This meant that the greedy algorithm ended up running somewhat like a BFS which expands all the nodes, hence a large amount of cost visited, and expanded nodes. This was a similar case for the A* algorithm with the default heuristic. However, since there was the factor of minimal cost, while the cost, expanded, and visited nodes were still all higher using the default heuristic, the values were still lower than they were for the greedy search using the default heuristic. Overall, the A* search had the lowest cost, although it visited 1 more node than the greedy search did. As for the infinite graph, it seems the DFS and BFS algorithms are stuck in an end loop. The BFS expands all the nodes which will take a long time, and DFS might just keep going in the wrong direction. When running greedy and A* search for the infinite graph, they are doing pretty well and pretty fast, no problems detected so far for greedy
and A* search algorithms.
