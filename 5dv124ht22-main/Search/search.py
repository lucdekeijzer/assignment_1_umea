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

def depthFirstSearch_2(problem: SearchProblem):
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
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    print("Successor test", problem.getSuccessors((5,4)))
    next_node = problem.getSuccessors(problem.getStartState())
    visited = util.Queue()
    fringe = util.Queue()
    visited.push(problem.getStartState())
    next_node = problem.getSuccessors(problem.getStartState())

    # Adding all the possible next coordinate states in the to do list
    for i in range(len(next_node)):
        fringe.push(next_node[i][0])

    for i in fringe.list:
        print(i)
    # current_state = (x,y)
    # problem.getSuccessors(current_state)

    # Printing next direction change
    for i in range(len(next_node)):
        print(f"Next direction: {i}, {next_node[i][1]=}")

    # Printing next coordinates
    for i in range(len(next_node)):
        print(f"Next coordinates (state): {i}, {next_node[i][0]=}")
    

    #util.raiseNotDefined()
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST





def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# General search algorithm based on the example in the lecture
def depthFirstSearch(problem: SearchProblem): #BFS
    from game import Directions

    print("-----------------------------------------------------------------------")
    count = 1
    visited_coor = []
    visited_directions = []
    fringe_coor = util.Queue()
    fringe_directions = util.Queue()
    path = ["South"]
    
    visited_coor.insert(0, problem.getStartState())
    next_node = problem.getSuccessors(problem.getStartState())
    print(f"{next_node=}")
    print(f"{problem.isGoalState(problem.getStartState())=}")
    # for i in range(len(next_node)):
        
    #     fringe_coor.push(next_node[i][0])
    for i in range(len(next_node)):
                        # HERE MAYBE?
                        print(f"{next_node[i][0]=}")
                        if next_node[i][0] not in visited_coor:
                            temp_coor = next_node[i][0]
                            temp_dir = next_node[i][1]
                            print(f"{temp_coor=}, {temp_dir=}")
                            print(f"running for loop check {i=} ,{next_node[i][0]}")
                            fringe_directions.push(temp_dir)
                            fringe_coor.push(temp_coor)
                            # fringe_directions.push(next_node[i][1])
                            # fringe_coor.push(next_node[i][0])    

    
    while True:
        print(f"{visited_coor=}")
        print(f"{visited_directions=}")
        print("fringe coor")
        fringe_coor.print()
        print("fringe directions")
        fringe_directions.print()
        # print(f"{fringe_directions=}")

        if fringe_coor.isEmpty():
            # print("are we getting here?")
            print("Fringe was empty")
            for i in visited_directions:
                if i == "South":
                    path.insert(0, Directions.SOUTH)
                elif i == "North":
                    path.insert(0, Directions.NORTH)
                elif i == "West":
                    path.insert(0, Directions.WEST)
                elif i == "East":
                    path.insert(0, Directions.EAST)
            print("do we get to the end?")
            break         
            # return path
            # break
        
        else:
            try:  
                curr_node = fringe_coor.pop()
                print(f"first else statement: {curr_node=}")
                if problem.isGoalState(curr_node):
                    print("are we getting to the goal?")
                    print("THIS WILL BE PRINTED IF WE FOUND THE GOAL")
                    for i in visited_directions:
                        if i == "South":
                            path.insert(0, Directions.SOUTH)
                        elif i == "North":
                            path.insert(0, Directions.NORTH)
                        elif i == "West":
                            path.insert(0, Directions.WEST)
                        elif i == "East":
                            path.insert(0, Directions.EAST)
                            # return path
                    break
                else:
                    print(f"{curr_node=}")
                    next_node = problem.getSuccessors(curr_node)
                    # Adding all the possible next coordinate states in the to do list
                    print(f"{len(next_node)=}")
                    print(f"{next_node=}")
                    for i in range(len(next_node)):
                        print(f"{next_node[i][0]=}")
                        if next_node[i][0] not in visited_coor:
                            temp_coor = next_node[i][0]
                            temp_dir = next_node[i][1]
                            print(f"{temp_coor=}, {temp_dir=}")
                            print(f"running for loop check {i=} ,{next_node[i][0]}")
                            fringe_directions.push(temp_dir)
                            fringe_coor.push(temp_coor)
                            # fringe_directions.push(next_node[i][1])
                            # fringe_coor.push(next_node[i][0])

                        # print(f"Next coordinates (state): {i}, {next_node[i][0]=}")
                    visited_coor.insert(0, curr_node)
                    last_direction = fringe_directions.pop()
                    visited_directions.insert(0, last_direction)
                    # fringe_coor.push(problem.getSuccessors(curr_node))
                        
            # except Exception:
            #     print("Exception caught")        
            
            except IndexError:
                print(f"We got an indexError")
                for i in visited_directions:
                    if i == "South":
                        path.insert(0, Directions.SOUTH)
                    elif i == "North":
                        path.insert(0, Directions.NORTH)
                    elif i == "West":
                        path.insert(0, Directions.WEST)
                    elif i == "East":
                        path.insert(0, Directions.EAST)
                break
    
        print(f"{count=}")
        count = count + 1
        print("------------------------------------------------------------------")
    print("We should be getting to the end")
    print(f"{type(visited_directions)=}")
    print(f"{visited_directions=}")
    visited_directions = visited_directions.reverse()
    print(f"{path=}")
    path.reverse()
    print(f"{path=}")
 
    return path            


    
    #fringe ← Insert (Make-Node(Initial-Stat e [problem]), fringe)
    # python3 pacman.py -l tinyMaze -p SearchAgent -a fn=depthFirstSearch

def depth_first_search(problem):
    # Initialize the stack with the start state and an empty path
    # stack = [(problem.getStartState(), [])]
    stack = util.Stack()
    stack.push(problem.getStartState())
    # Create a set to keep track of visited states
    visited = []
    
    while stack:
        # Pop the current state and path from the stack
        state, path = stack.pop()
        
        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return path  # Return the path to the goal
        
        # Mark the current state as visited
        visited.append(state)
        
        # Get the successor states and actions
        successors = problem.getSuccessors(state)
        
        for next_state, action, _ in successors:
            if next_state not in visited:
                # Push the successor state and updated path onto the stack
                stack.push((next_state, path + [action]))
    
    return None  # If no path to the goal is found, return None



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
