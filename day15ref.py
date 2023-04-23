from collections import namedtuple
from heapq import heappop, heappush
import numpy as np


Node = namedtuple("Node", "x y")
Path = namedtuple("Path", "risk node")


with open("day15.txt", "rt") as file:
    cave_map = []
    for line in file: cave_map.append([int(char) for char in line.rstrip()])
    cave_map = np.array(cave_map)
    print(cave_map)

def path_find(cave_map:np.ndarray, start:Node, goal:Node) -> int:
    """Implementation of the A* algorithm to find the least risk path between
    two nodes in the cave"""

    # Upper boundary of the map
    max_y = len(cave_map) - 1
    max_x = len(cave_map[0]) - 1

    # Risk of the starting position
    start_risk = cave_map[start.y, start.x] #basically the top left cell
    
    # Nodes that are known but weren't visited yet,
    # and their minimum risk to get there
    not_visited:list[Path] = [Path(start_risk, start)]
	# format - a list of Path tuple containing the risk value and the node coor
	#[Path(risk=1, node=Node(x=0, y=0))]
    print("not_visited: ", not_visited)

	
    # Nodes that were already visited
    visited:list[Node] = []


	###############
    while not_visited: # while there not_visited element is not empty
	
        
        # Get the known unvisited node with the least risk
		#heapq.heappop() pop and return the smallest item from the heap so in this case it will return the path with the least risk
        risk, node = heappop(not_visited)

        # Stop if we have arrived at the goal
        if node == goal: return risk - start_risk

        # Do not go to the node if we have already visited it
        if node in visited: continue

        # Coordinates of our current position
        x, y = node

        # Movement choices from our current position
        choices = (x+1, y), (x-1, y), (x, y+1), (x, y-1)
        
        for next_x, next_y in choices: # trials and errors on every direction

            # The destination must be within the map boundaries
            if (0 <= next_x <= max_x) and (0 <= next_y <= max_y):
                
                # Calculate the risk to the next node
                next_risk = risk + cave_map[next_y][next_x]
                next_node = Node(next_x, next_y)
                heappush(not_visited, Path(next_risk, next_node))
            
        visited += [node]

# Part 1

goal_y, goal_x = cave_map.shape #cave_map is a numpy array and therefore .shape() essentially returns the width and height of the matrix (row, column)
risk_part1 = path_find(cave_map, Node(0,0), Node(goal_x-1, goal_y-1))
# Node(0,0) - starting 
# Node(goal_x - 1, goal_y -1) - ending

print(f"Part 1: {risk_part1}")
