from pulp import LpMinimize, LpProblem, LpVariable


def requirements():
    """
    Function returns dictionary of pairs containing requirements for nutrients, for example
    {'name': (min, max), ...}.
    :return: dictionary of pairs containing requirements for nutrients
    """
    requirement_values = dict()
    requirement_values['calorie'] = (2600, 3600)
    requirement_values['proteins'] = (0, 120)
    requirement_values['carbs'] = (0, 360)
    requirement_values['sugar'] = (0, 110)
    requirement_values['fat'] = (0, 80)
    return requirement_values


def products():
    """
    Function returns 10 products as dictionary of dictionaries containing name and nutrients values.
    :return: dictionary of dictionaries containing name and nutrients values
    """
    product_values = dict()
    product_values['Cheeseburger'] = {
        'calorie': 2700,
        'proteins': 130,
        'carbs': 330,
        'sugar': 60,
        'fat': 150,
    }

    product_values['Lasagne'] = {
        'calorie': 174,
        'proteins': 8,
        'carbs': 12,
        'sugar': 2,
        'fat': 10,
    }

    product_values['Spagetti'] = {
        'calorie': 596,
        'proteins': 53,
        'carbs': 17,
        'sugar': 4,
        'fat': 34,
    }
    product_values['Nugget'] = {
        'calorie': 188,
        'proteins': 18,
        'carbs': 8,
        'sugar': 1,
        'fat': 9,
    }
    product_values['Risotto'] = {
        'calorie': 62,
        'proteins': 2,
        'carbs': 9,
        'sugar': 2,
        'fat': 2,
    }
    product_values['Pizza'] = {
        'calorie': 161,
        'proteins': 9,
        'carbs': 20,
        'sugar': 1,
        'fat': 5,
    }
    product_values['Egg'] = {
        'calorie': 142,
        'proteins': 12,
        'carbs': 1,
        'sugar': 0,
        'fat': 10,
    }
    product_values['Subway_sandwich'] = {
        'calorie': 128,
        'proteins': 9,
        'carbs': 19,
        'sugar': 4,
        'fat': 2,
    }
    product_values['Nuts'] = {
        'calorie': 677,
        'proteins': 19,
        'carbs': 18,
        'sugar': 2,
        'fat': 60,
    }
    product_values['Yogurt'] = {
        'calorie': 78,
        'proteins': 6,
        'carbs': 9,
        'sugar': 9,
        'fat': 2,
    }

    return product_values


def create_linear_programming_variables(prod_values):
    """
    Function creates dictionary of LpVariable objects. Every product should have LpVariable with
    the same name.
    :param prod_values: dictionary of dictionaries containing name and nutrients values
    :return: dictionary containing names and LpVariables
    """
    variables = dict()
    product_names = prod_values.keys()
    for name in product_names:
        variables[name] = LpVariable(name, 0)
    return variables


def create_linear_constraints_diet_exists(variables, prod_values, req_values):
    """
    Function returns list of linear constraints needed to satisfy requirements. Every constraint
    should include min and max for nutrient and all variables multiplied by amount of nutrient in
    given product.
    :param variables: dictionary containing names and LpVariables
    :param prod_values: dictionary of dictionaries containing name and nutrients values
    :param req_values: dictionary of pairs containing requirements for nutrients
    :return: list of linear constraints
    """
    constraints = list()
    for nutrion in req_values:
        temp_sum = 0
        for prod_val in prod_values.keys():
            temp_sum += prod_values[prod_val][nutrion] * variables[prod_val]
        constraints.append(temp_sum <= req_values[nutrion][1])
        constraints.append(temp_sum >= req_values[nutrion][0])


    return constraints


def create_linear_programming_problem(linear_objective, linear_constraints):
    """
    Function creates linear programming problem in Pulp.
    :param linear_objective: linear objective to be minimized or None (implement appropriately!)
    :param linear_constraints: list of linear constraints
    :return: LpProblem object
    """
    problem = LpProblem('diet',LpMinimize)
    if linear_objective is None:
        pass
    else:
        problem += linear_objective
    for con in linear_constraints:
        problem += con

    return problem


def solve_linear_problem(linear_problem):
    """
    Solves linear problem and returns problem, objective and status.
    :param linear_problem: LpProblem object
    :return: (LpProblem, LpObjective, LpStatus)
    """
    linear_problem.solve()
    return linear_problem, linear_problem.objective, linear_problem.status


def solve_diet_exists(prod_values, req_values):
    """
    Function creates and sets up linear programming problem for satisfiability problem.
    Returns problem, objective value and solver status.
    and finds its solution
    :param prod_values: dictionary of dictionaries containing name and nutrients values
    :param req_values: dictionary of pairs containing requirements for nutrients
    :return: (LpProblem, LpObjective, LpStatus)
    """
    variables = create_linear_programming_variables(prod_values)
    constr = create_linear_constraints_diet_exists(variables,prod_values, req_values)
    problem = create_linear_programming_problem(None, constr)
    return  solve_linear_problem(problem)


def create_linear_objective_min_calorie(variables, prod_values):
    """
    Function returns linear objective to be minimized.
    :param variables: dictionary containing names and LpVariables
    :param prod_values: dictionary of dictionaries containing name and nutrients values
    :return: linear objective to be minimized
    """
    sums = 0

    for prod in prod_values:
        sums += prod_values[prod]['calorie'] * variables[prod]

    return sums


def create_linear_constraints_min_calorie(variables, prod_values, req_values):
    """
    Function returns list of linear constraints needed to satisfy requirements. Every constraint
    should include min and max for nutrient and all variables multiplied by amount of nutrient in
    given product.
    :param variables: dictionary containing names and LpVariables
    :param prod_values: dictionary of dictionaries containing name and nutrients values
    :param req_values: dictionary of pairs containing requirements for nutrients
    :return: list of linear constraints
    """
    constraints = list()
    for nutrion in req_values:
        temp_sum = 0
        for prod_val in list(prod_values.keys())[1:]:
            temp_sum += prod_values[prod_val][nutrion] * variables[prod_val]
        constraints.append(temp_sum <= req_values[nutrion][1])
        constraints.append(temp_sum >= req_values[nutrion][0])

    return constraints


def solve_diet_min_calorie(prod_values, req_values):
    """
    Function creates and sets up linear programming problem for calorie minimization.
    Returns problem, objective value and solver status.
    :param prod_values: dictionary of dictionaries containing name and nutrients values
    :param req_values: dictionary of pairs containing requirements for nutrients
    :return: (LpProblem, LpObjective, LpStatus)
    """
    variables = create_linear_programming_variables(prod_values)
    constr = create_linear_constraints_min_calorie(variables, prod_values, req_values)
    obj = create_linear_objective_min_calorie(variables,prod_values)
    problem = create_linear_programming_problem(obj, constr)
    return solve_linear_problem(problem)

