import warnings
from time import sleep

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pulp import value

from content import solve_diet_exists, solve_diet_min_calorie, products, requirements
from test_content import TestRunner


def print_results(problem, objective, title):
    names = list()
    amounts = list()

    if objective is not None:
        print(f'Calorie = {value(objective)}')
        title += f' = {round(value(objective), 1)}'

    for v in problem.variables():
        if v.varValue is not None:
            print(v.name, "=", v.varValue)
            names.append(v.name)
            amounts.append(v.varValue)

    amounts = np.array(amounts)
    amounts = np.reshape(amounts, newshape=(len(names), 1))
    dataframe = pd.DataFrame(amounts, columns=['Products'])
    plt.figure()
    ax = sns.barplot(x=names, y="Products", data=dataframe)
    ax.set_title(title)
    for index, row in dataframe.iterrows():
        ax.text(index, row.Products, round(row.Products, 3), color='black', ha="center")
    plt.draw()
    plt.waitforbuttonpress(1)


if __name__ == "__main__":
    # Ignore warnings
    warnings.filterwarnings("ignore")

    # Run tests
    test_runner = TestRunner()
    results = test_runner.run()

    if results.failures:
        exit()
    sleep(0.1)

    product_values = products()
    requirement_values = requirements()

    print('Selected products:')
    for prod_num, prod in enumerate(product_values.keys()):
        print(f'Product: {prod_num+1}, {prod}')
        print('\n'.join([f'{key} : {value}' for key, value in product_values[prod].items()]))
        print('')

    print('Requirements:')
    for req_name, req in requirement_values.items():
        print(f'{req_name} : {req[0]} - {req[1]}')
    print('')

    print('Does diet exist?')
    problem, objective, status = solve_diet_exists(product_values, requirement_values)
    if status == 1:
        print_results(problem, objective, 'Diet exists')
    else:
        print('Diet does not exist.')
    print('')

    print('Min calorie diet:')
    problem, objective, status = solve_diet_min_calorie(product_values, requirement_values)
    if status == 1:
        print_results(problem, objective, 'Min calorie')
    else:
        print('Diet does not exist.')

    plt.waitforbuttonpress(0)


