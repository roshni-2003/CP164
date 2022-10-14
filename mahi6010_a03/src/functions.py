"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-05-27"
-------------------------------------------------------
"""
from Stack_array import Stack


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    left = True
    while not source.is_empty():
        if left:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    array = []
    for value in source:
        array.insert(0, value)
    source = []
    for value in array:
        source.append(value)
    return


# Constants
OPERATORS = "*/+-"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    lst = string.split(" ")
    for value in lst:
        if value in OPERATORS:
            if not stack.is_empty():
                num2 = stack.pop()
                if not stack.is_empty():
                    num1 = stack.pop()
                    if value == OPERATORS[0]:
                        num = num1 * num2
                        stack.push(num)
                    elif value == OPERATORS[1]:
                        num = num1 / num2
                        stack.push(num)
                    elif value == OPERATORS[2]:
                        num = num1 + num2
                        stack.push(num)
                    elif value == OPERATORS[3]:
                        num = num1 - num2
                        stack.push(num)
        else:
            stack.push(float(value))
    if not stack.is_empty():
        answer = stack.pop()
    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()
    key = list(maze)[0]
    stack.push(maze[key][0])
    path = []
    ext = False

    while not stack.is_empty():
        node = stack.pop()
        if node in path:
            continue
        path.append(node)

        if node in maze:
            for child in maze[node]:
                stack.push(child)
                if child in maze:
                    if len(maze[child]) == 0:
                        stack.pop()
                else:
                    break
        else:
            ext = True
            break
    if ext is False:
        path = None

    return path
