# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    game GENERATESUCCESSOR

    """
    "*** YOUR CODE HERE ***"
    # Instantiate stack, the directions list, the visited coordinates list and the cost (used in later algorithms)
    fringe = util.Stack()
    dir = []
    visited = []
    cost = 0

    # Add start node to stack
    start_node = problem.getStartState()
    fringe.push((start_node, dir, cost))    

    # While the fringe is not empty, take an element out of the fringe (depending on the strategy)
    while not fringe.isEmpty():

        popped_node = fringe.pop()
        curr_node = popped_node[0]
        dir = popped_node[1]
        cost = popped_node[2]

        # Check if that node is the goal state, if it is, we can stop the search and return the directions
        if problem.isGoalState(curr_node):
            print(f"End dir: {dir=}")
            return dir
        
        # Else, we will add the current node coordinates to the visited coordinates list for future reference
        else:
            visited.append(curr_node)

        # The next nodes will be determined by calling the getSuccesors method on the current node.
        # If the next node's coordinates are not yet visited, we will push them into the fringe.
        next_nodes = problem.getSuccessors(curr_node)
        for node, next_dir, cost in next_nodes:
            if node not in visited:
                fringe.push((node, dir + [next_dir], cost))

    # if all else fails, we return None
    return None





def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Instantiate queue, the directions list, the visited coordinates list and the cost (used in later algorithms)
    fringe = util.Queue()
    dir = []
    visited = []
    cost = 0

    # Add start node to stack
    start_node = problem.getStartState()
    fringe.push((start_node, dir, cost))
    visited.append(start_node)    

    # While the fringe is not empty, take an element out of the fringe (depending on the strategy)
    while not fringe.isEmpty():
        popped_node = fringe.pop()
        curr_node = popped_node[0]
        dir = popped_node[1]
        cost = popped_node[2]

        # Check if that node is the goal state, if it is, we can stop the search and return the directions
        if problem.isGoalState(curr_node):
            print(f"End dir: {dir=}")
            return dir
        
        # Else, we will add the current node coordinates to the visited coordinates list for future reference
        else:
            # visited.append(curr_node)

        # The next nodes will be determined by calling the getSuccesors method on the current node.
        # If the next node's coordinates are not yet visited, we will push them into the fringe.
            next_nodes = problem.getSuccessors(curr_node)
            for node, next_dir, cost in next_nodes:
                if node not in visited:
                    visited.append(node)
                    fringe.push((node, dir + [next_dir], cost))

    # if all else fails, we return None
    return None

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Instantiate stack, the directions list, the visited coordinates list and the cost (used in later algorithms)
    fringe = util.PriorityQueue()
    # dir = []
    visited = []
    # cost = 0

    # Add start node to stack
    start_node = problem.getStartState()
    # visited.append(start_node)
    fringe.push((start_node, [], 0), 0)
        
    # While the fringe is not empty, take an element out of the fringe (depending on the strategy)
    while not fringe.isEmpty():
        
        curr_node, dir, cost = fringe.pop()
        if curr_node in visited:
            continue
        # dir = popped_node[1]
        visited.append(curr_node)
        # Check if that node is the goal state, if it is, we can stop the search and return the directions
        if problem.isGoalState(curr_node):
            print(f"End dir: {dir=}")
            return dir
        
        # Else, we will add the current node coordinates to the visited coordinates list for future reference
        # The next nodes will be determined by calling the getSuccesors method on the current node.
        # If the next node's coordinates are not yet visited, we will push them into the fringe.      
        else:
            next_nodes = problem.getSuccessors(curr_node)
            for node, next_dir, next_cost in next_nodes:
                if node not in visited:
                    
                    new_cost = cost + next_cost
                    new_dir = dir  + [next_dir]
                    # priority_queue.push((next_state, new_path, new_cost), new_cost)
                    fringe.push((node, new_dir, new_cost), new_cost)
    # if all else fails, we return None
    return None

def uniformCostSearch_2(problem: SearchProblem):
    priority_queue = util.PriorityQueue() 
    start_state = problem.getStartState() 
    priority_queue.push((start_state, [], 0), 0) 
    visited = set() 
    while not priority_queue.isEmpty(): 
        state, path, cost = priority_queue.pop() 
        if state in visited: 
            continue 
        visited.add(state) 
        if problem.isGoalState(state): 
            return path 
        successors = problem.getSuccessors(state) 
        for next_state, action, step_cost in successors: 
            if next_state not in visited: 
                new_cost = cost + step_cost 
                new_path = path + [action] 
                priority_queue.update((next_state, new_path, new_cost), new_cost) 
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []  
    start_state = problem.getStartState() 
    priorityQueue = util.PriorityQueueWithFunction(lambda item: item[2] + heuristic(item[0], problem)) 
    priorityQueue.push((start_state, [], 0))
    
    if problem.isGoalState(start_state): 
        return [] 
     
    while not priorityQueue.isEmpty(): 
        current_state, path, cost = priorityQueue.pop() 
        if current_state in visited: 
            continue 
        visited.append(current_state) 
        if problem.isGoalState(current_state): 
            return path 
        for next_state, action, step_cost in problem.getSuccessors(current_state): 
            if next_state not in visited: new_cost = cost + step_cost 
            new_path = path + [action] 
            priorityQueue.push((next_state, new_path, new_cost))
    return []
    

""" THIS IS THE TEMPLATE TO USE FOR ANY OF THE SEARCH ALGORITHMS USED IN THIS ASSIGNMENT"""

# General search algorithm based on the example in the lecture
def generalSearch(problem: SearchProblem):

    # Instantiate stack, the directions list, the visited coordinates list and the cost (used in later algorithms)
    fringe = util.Stack()
    dir = []
    visited = []
    cost = 0

    # Add start node to stack
    start_node = problem.getStartState()
    fringe.push((start_node, dir, cost))    

    # While the fringe is not empty, take an element out of the fringe (depending on the strategy)
    while not fringe.isEmpty():
        curr_node, dir, cost  = fringe.pop()

        # Check if that node is the goal state, if it is, we can stop the search and return the directions
        if problem.isGoalState(curr_node):
            print(f"End dir: {dir=}")
            return dir
        
        # Else, we will add the current node coordinates to the visited coordinates list for future reference
        else:
            visited.append(curr_node)

        # The next nodes will be determined by calling the getSuccesors method on the current node.
        # If the next node's coordinates are not yet visited, we will push them into the fringe.
        next_nodes = problem.getSuccessors(curr_node)
        for node, next_dir, cost in next_nodes:
            if node not in visited:
                fringe.push((node, dir + [next_dir], cost))

    # if all else fails, we return None
    return None



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
