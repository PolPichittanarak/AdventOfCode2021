# open file and concert the map into a numpy array
# Make each spot/node a namedtuple - containing the risk and the node coordinates
# Collect Path as a namedtuple - store each node
# define the goal node and the start node
# find boundary
# initialise starting node
# identify the max x and max y
# create a list of unvisited node 
# create a list of visited node
# check of the unvisited node is empty
# if not pass into the main while loop 
# while in the main while loop, heappop the node from the path to get our working node 
# check if it's the goal node 
# check if the node has been visited by checking the presence in the visited array
# initialize 4 directions as a list of tuples
# iterate through each tuple and increment current risk accordingly 
# make sureit stays within the map coordinates 
# then find the next node risk
# then find the next node Node()
# heappush the path into the heap as [Path(nextrisk, Node)]
# add to the node visited






from collections import namedtuple
from heapq import heappop, heappush
import numpy as np

file = open("day15test.txt", "rt")
map = []
for line in file:
	map.append([int(cell) for cell in line.strip()])
map = np.array(map)


Node = namedtuple("Node", "x y")
Path = namedtuple("Path", "node risk")

GoalNode = map.shape
GoalNodeX, GoalNodeY = map.shape[1] - 1, map.shape[0] - 1
StartNodeX, StartNodeY = 0, 0

MaxX, MaxY = len(map[0]) - 1, len(map) - 1

InitialRisk = map[StartNodeY, StartNodeX]
unvisitedNode = [Path(InitialRisk, Node(StartNodeX, StartNodeY))]
visitedNode = []

while unvisitedNode:
	print("check")
	CurrentRisk, CurrentNode = heappop(unvisitedNode)
	if CurrentNode == Node(GoalNodeX, GoalNodeY):
		print("Terminated at", end = " ")
		print(CurrentRisk - InitialRisk)
	if CurrentNode in visitedNode:
		continue

	x, y = CurrentNode
	Moves = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
	# right, down, left, up

	for MoveX, MoveY in Moves:
		if (0 <= MoveX <= MaxX) and (0 <= MoveY <= MaxY):
			NextRisk = CurrentRisk + map[MoveY][MoveX]
			NextNode = Node(MoveX, MoveY)
			heappush(unvisitedNode, Path(NextRisk, NextNode))
		
	visitedNode += [CurrentNode]
	


