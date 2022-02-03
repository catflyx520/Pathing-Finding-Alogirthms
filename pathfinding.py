import graph
from queue import PriorityQueue

def default_heuristic(n):
    """
    Default heuristic for A*. Do not change, rename or remove!
    """
    return 0

def bfs(start, goal):
    """
    Breadth-First search algorithm. The function is passed a start graph.Node object and a goal predicate.
    
    The start node can produce neighbors as needed, see graph.py for details.
    
    The goal is represented as a function, that is passed a node, and returns True if that node is a goal node, otherwise False. 
    
    The function should return a 4-tuple (path,distance,visited,expanded):
        - path is a sequence of graph.Edge objects that have to be traversed to reach a goal state from the start
        - distance is the sum of costs of all edges in the path 
        - visited is the total number of nodes that were added to the frontier during the execution of the algorithm 
        - expanded is the total number of nodes that were expanded, i.e. removed from the frontier to add their neighbors
    """
    Frontier = []
    visited = []
    path = []
    Frontier.append(start)
    visited.append(start.get_id())
    dis = 0
    visited_counter = 1
    expanded = 0
    while Frontier:
        current = Frontier.pop()
        if goal(current):
            return path, dis, visited_counter, expanded
        expanded += 1
        for neighbor in current.get_neighbors():
            if neighbor.target.get_id in visited:continue
            dis += neighbor.cost
            visited_counter += 1
            path.append(neighbor)
            #print ("visiting: ", neighbor.target )
            if goal(neighbor.target):
                #print("goal is found ", neighbor.target.name)
                return path, dis, visited_counter, expanded

            Frontier.append(neighbor.target)
            #print("frontier appended ",neighbor.target.name)
            visited.append(neighbor.target.get_id)





def dfs(start, goal):
    """
    Depth-First search algorithm. The function is passed a start graph.Node object, a heuristic function, and a goal predicate.

    The start node can produce neighbors as needed, see graph.py for details.

    The goal is represented as a function, that is passed a node, and returns True if that node is a goal node, otherwise False.

    The function should return a 4-tuple (path,distance,visited,expanded):
        - path is a sequence of graph.Edge objects that have to be traversed to reach a goal state from the start
        - distance is the sum of costs of all edges in the path
        - visited is the total number of nodes that were added to the frontier during the execution of the algorithm
        - expanded is the total number of nodes that were expanded, i.e. removed from the frontier to add their neighbors
    """
    Frontier = []
    visited = []
    path = []
    Frontier.append(start)
    visited.append(start.get_id())
    dis = 0
    visited_counter = 1
    expanded = 0
    while Frontier:

        neighbors = Frontier.pop()

        if neighbors is not start:

            dis += neighbors[2]
            path.append(neighbors[1])
            neighbors=neighbors[0].get_neighbors()

        else:
            neighbors=neighbors.get_neighbors()

        expanded += 1
        for neighbor in neighbors:

            if neighbor.target.get_id() not in visited:

                Frontier.append([neighbor.target,neighbor,neighbor.cost])
                visited.append(neighbor.target.get_id())
                visited_counter += 1
            if goal(neighbor.target):

                dis+=neighbor.cost
                path.append(neighbor)
                visited_counter += 1
                return path,dis,visited_counter,expanded

   # return path, dis, visited, expanded



def greedy(start, heuristic, goal):
    """
    Greedy search algorithm. The function is passed a start graph.Node object, a heuristic function, and a goal predicate.
    
    The start node can produce neighbors as needed, see graph.py for details.
    
    The heuristic is a function that takes a node as a parameter and returns an estimate for how far that node is from the goal.    
    
    The goal is also represented as a function, that is passed a node, and returns True if that node is a goal node, otherwise False. 
    
    The function should return a 4-tuple (path,distance,visited,expanded):
        - path is a sequence of graph.Edge objects that have to be traversed to reach a goal state from the start
        - distance is the sum of costs of all edges in the path 
        - visited is the total number of nodes that were added to the frontier during the execution of the algorithm 
        - expanded is the total number of nodes that were expanded, i.e. removed from the frontier to add their neighbors
    """
    frontier = PriorityQueue()
    priority = heuristic(start)
    expanded = []
    path = []
    visited = []
    expand_counter = 0
    visited_counter = 1
    total_distance = 0
    frontier.put((priority, visited_counter, start))
    expanded.append(start.get_id())
    visited.append(start.get_id())

    while not frontier.empty():

        pop_from_frontier = frontier.get()
        expand_node = pop_from_frontier[2]
        expand_counter += 1

        expanded.append(expand_node.get_id())
        if expand_node is not start:
            path.append(pop_from_frontier[4])
            total_distance += pop_from_frontier[3]

        neighbors = expand_node.get_neighbors()
        for neighbor in neighbors:
            next = neighbor.target
            if goal(next):
                path.append(neighbor)
                total_distance += neighbor.cost
                return path, total_distance, visited_counter, expand_counter

            if next.get_id() not in visited or next.get_id() not in expanded:
                priority = heuristic(next)
                frontier.put((priority, visited_counter, next,neighbor.cost,neighbor))
                visited.append(next.get_id())
                visited_counter += 1

    return path, total_distance, visited_counter, expand_counter

    

def astar(start, heuristic, goal):
    """
    A* search algorithm. The function is passed a start graph.Node object, a heuristic function, and a goal predicate.
    
    The start node can produce neighbors as needed, see graph.py for details.
    
    The heuristic is a function that takes a node as a parameter and returns an estimate for how far that node is from the goal.    
    
    The goal is also represented as a function, that is passed a node, and returns True if that node is a goal node, otherwise False. 
    
    The function should return a 4-tuple (path,distance,visited,expanded):
        - path is a sequence of graph.Edge objects that have to be traversed to reach a goal state from the start
        - distance is the sum of costs of all edges in the path 
        - visited is the total number of nodes that were added to the frontier during the execution of the algorithm 
        - expanded is the total number of nodes that were expanded, i.e. removed from the frontier to add their neighbors
    """
    frontier = PriorityQueue()
    priority = heuristic(start)
    expanded = []
    path = []
    visited = []
    minimal_distance = 0
    expand_counter = 0
    visited_counter = 1
    total_minimal_distance = 0
    frontier.put((priority, 0,start, minimal_distance))
    expanded.append(start.get_id())
    visited.append(start.get_id())

    while not frontier.empty():

        pop_from_frontier = frontier.get()
        expand_node = pop_from_frontier[2]
        expand_counter +=1
        minimal_distance = pop_from_frontier[3] + minimal_distance
        expanded.append(expand_node.get_id())
        if expand_node is not start:
            path.append(pop_from_frontier[4])

        neighbors=expand_node.get_neighbors()
        for neighbor in neighbors:

                next = neighbor.target
                if goal(next):
                    path.append(neighbor)
                    total_minimal_distance=minimal_distance+neighbor.cost
                    return path, total_minimal_distance, visited_counter, expand_counter

                if next.get_id() not in visited or next.get_id() not in expanded:
                    priority = neighbor.cost + heuristic(next)

                    frontier.put((priority,visited_counter, next, neighbor.cost,neighbor))
                    visited.append(next.get_id())
                    visited_counter+=1

    return path,total_minimal_distance,visited_counter,expand_counter
    
def run_all(name, start, heuristic, goal):
    print("running test", name)
    print("Breadth-First Search")

    result = bfs(start, goal)
    print_path(result)

    print("\nDepth-First Search")
    result = dfs(start, goal)
    print_path(result)

    print("\nGreedy Search (default heuristic)")
    result = greedy(start, default_heuristic, goal)
    print_path(result)
    
    print("\nGreedy Search")
    result = greedy(start, heuristic, goal)
    print_path(result)
    
    print("\nA* Search (default heuristic)")
    result = astar(start, default_heuristic, goal)
    print_path(result)


    print("\nA* Search")
    result = astar(start, heuristic, goal)
    print_path(result)




    print("\n\n")

def print_path(result):
    (path,cost,visited_cnt,expanded_cnt) = result
    print("visited nodes:", visited_cnt, "expanded nodes:",expanded_cnt)
    if path:
        print("Path found with cost", cost)
        for n in path:
            print(n.name)
    else:
        print("No path found")
    print("\n")





def main():
    """
    You are free (and encouraged) to change this function to add more test cases.
    
    You are provided with three test cases:
        - pathfinding in Austria, using the map shown in class. This is a relatively small graph, but it comes with an admissible heuristic. Below astar is called using that heuristic, 
          as well as with the default heuristic (which always returns 0). If you implement A* correctly, you should see a small difference in the number of visited/expanded nodes between the two heuristics.
        - pathfinding on an infinite graph, where each node corresponds to a natural number, which is connected to its predecessor, successor and twice its value, as well as half its value, if the number is even.
          e.g. 16 is connected to 15, 17, 32, and 8. The problem given is to find a path from 1 to 2050, for example by doubling the number until 2048 is reached and then adding 1 twice. There is also a heuristic 
          provided for this problem, but it is not admissible (think about why), but it should result in a path being found almost instantaneously. On the other hand, if the default heuristic is used, the search process 
          will take a noticeable amount (a couple of seconds).
        - pathfinding on the same infinite graph, but with infinitely many goal nodes. Each node corresponding to a number greater 1000 that is congruent to 63 mod 123 is a valid goal node. As before, a non-admissible
          heuristic is provided, which greatly accelerates the search process. 
    """
    target = "Bregenz"
    def atheuristic(n):
        return graph.AustriaHeuristic[target][n.get_id()]
    def atgoal(n):
        return n.get_id() == target
    start=graph.Austria["Eisenstadt"]

    def ctheuristic(n):
        return graph.ChinaHeruistic[target][n.get_id()]

    """
    print("\nDepth-First Search")
    result = dfs(graph.Austria["Eisenstadt"], atgoal)
    print_path(result)
    
    print("\nA* Search (default heuristic)")
    result = astar(graph.Austria["Eisenstadt"],default_heuristic,atgoal)
    print_path(result)

    print("\nA* Search")
    result = astar(graph.Austria["Eisenstadt"],atheuristic, atgoal)
    print_path(result)
    
    print("\nA* Search")
    result = astar(graph.China["Changsha"], ctheuristic, atgoal)
    print_path(result)
    """
    run_all("Austria", graph.Austria["Eisenstadt"], atheuristic, atgoal)
    #run_all("China", graph.China["Wuhan"], ctheuristic, atgoal)

    target = 2050
    def infheuristic(n):
        return abs(n.get_id() - target)
    def infgoal(n):
        return n.get_id() == target
    
    #run_all("Infinite Graph (simple)", graph.InfNode(1), infheuristic, infgoal)


    def multiheuristic(n):
        return abs(n.get_id()%123 - 63)
    def multigoal(n):
        return n.get_id() > 1000 and n.get_id()%123 == 63
  
    #run_all("Infinite Graph (multi)", graph.InfNode(1), multiheuristic, multigoal)


if __name__ == "__main__":
    main()