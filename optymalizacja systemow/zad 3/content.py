import itertools

from pulp import LpProblem, LpMinimize, LpVariable, LpInteger


def initial_values():
    """
    Function returns list of tuples, [(x, y, v), ...],
    indicating that in coordinates [x, y] (counting from 0) should be number v (counting from 1).
    :return: list of tuples
    """
    initial = list()
    initial.append((0,8,1))
    initial.append((7,4,2))
    initial.append((3,2,4))
    initial.append((6,1,6))
    initial.append((0, 3, 1))
    return initial

def create_linear_programming_variables():
    """
    Function creates dictionary of LpVariable objects. Every coordinate and value
    should have LpVariable. Key for dictionary should be tuple in format (x,y,v).
    For convinience, name in LpVariable should be str((x,y,v))
    :return: dict with LpVariables
    """
    variables = dict()
    for x in range(9):
        for y in range(9):
            for v in range(1, 10):
                variables[(x,y,v)] = LpVariable(str((x,y,v)), cat="Binary")
    return variables


def create_row_constraints(variables):
    """
    Creates constraints ensuring every row contain one of every value.
    :param variables: dict with LpVariables
    :return: list of constraints
    """
    constraints = list()
    for i in range(9):
        for k in range(1, 10):
            temp_sum = 0
            for j in range(9):
                temp_sum += variables[(i,j,k)]
            constraints.append(temp_sum == 1)

    return constraints


def create_col_constraints(variables):
    """
    Creates constraints ensuring every column contain one of every value.
    :param variables: dict with LpVariables
    :return: list of constraints
    """
    constraints = list()
    for j in range(9):
        for k in range(1, 10):
            temp_sum = 0
            for i in range(9):
                temp_sum += variables[(i, j, k)]
            constraints.append(temp_sum == 1)

    return constraints


def create_cell_constraints(variables):
    """
    Creates constraints ensuring every 3x3 cell contain one of every value.
    :param variables: dict with LpVariables
    :return: list of constraints
    """
    constraints = list()
    for u in range(0,7,3):
        for v in range(0,7,3):
            for k in range(1,10):
                temp_sum = 0
                for i in range(3):
                    for j in range(3):
                        temp_sum += variables[(i+u, j+v, k)]
                constraints.append(temp_sum == 1)

    return constraints


def create_unique_constraints(variables):
    """
    Creates constraints ensuring every field contains one value.
    :param variables: dict with LpVariables
    :return: list of constraints
    """
    constraints = list()
    for j in range(9):
        for i in range(9):
            temp_sum = 0
            for k in range(1, 10):
                temp_sum += variables[(i, j, k)]
            constraints.append(temp_sum == 1)

    return constraints


def create_initial_constraints(variables, initial_values):
    """
    Creates constraints ensuring that initial values are not changed.
    :param variables: dict with LpVariables
    :param initial_values: list of tuples
    :return: list of constraints
    """
    constraints = list()
    for i,j,k in initial_values:
        constraints.append(variables[i,j,k] == 1)

    return constraints


def create_linear_programming_problem(linear_constraints):
    """
    Function creates linear programming problem in Pulp. Returns LpProblem object
    :param linear_constraints: list of constraints
    :return: LpProblem object
    """
    problem = LpProblem('sudoku', LpMinimize)

    for con in linear_constraints:
        problem += con

    return problem


def solve_linear_problem(linear_problem):
    """
    Solves linear problem, returns problem, objective and solver status
    :param linear_problem: LpProblem object
    :return: linear problem, objective, solver status
    """
    linear_problem.solve()
    return linear_problem, linear_problem.objective, linear_problem.status



def solve_sudoku(initial_values):
    """
    Function creates and sets up linear programming problem for satisfiability problem.
    Returns variables, problem, objective value and solver status.
    and finds its solution
    :param initial_values: list of tuples
    :return: list of variables, linear problem, objective, solver status
    """
    variables = create_linear_programming_variables()
    con = create_col_constraints(variables)
    con += create_row_constraints(variables)
    con += create_cell_constraints(variables)
    con += create_initial_constraints(variables,initial_values)
    con += create_unique_constraints(variables)
    problem = create_linear_programming_problem(con)
    l_p, l_obj, l_status = solve_linear_problem(problem)

    return variables,l_p, l_obj, l_status
