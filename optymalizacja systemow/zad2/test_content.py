from unittest import TestCase, TestSuite, TextTestRunner, makeSuite

from pulp import LpVariable, LpProblem, LpAffineExpression, LpConstraint

from content import *


class TestRunner:
    def __init__(self):
        self.runner = TextTestRunner(verbosity=2)

    def run(self):
        test_suite = TestSuite(tests=[
            makeSuite(TestRequirements),
            makeSuite(TestProducts),
            makeSuite(TestVariables),
            makeSuite(TestConstraintsExists),
            makeSuite(TestProblem),
            makeSuite(TestSolveLinearProblem),
            makeSuite(TestObjective),
            makeSuite(TestConstraintsMinCalorie),
        ])
        return self.runner.run(test_suite)


class TestRequirements(TestCase):
    def test_result_type(self):
        function_result = requirements()
        self.assertTrue(isinstance(function_result, dict))

    def test_result_size(self):
        function_result = requirements()
        self.assertGreater(len(function_result.keys()), 1)

    def test_result_dict_keys(self):
        function_result = requirements()
        self.assertTrue(all(isinstance(key, str) for key in function_result.keys()))

    def test_result_dict_values(self):
        function_result = requirements()
        self.assertTrue(all(isinstance(value, tuple) for value in function_result.values()))

    def test_result_dict_values_structure(self):
        function_result = requirements()
        self.assertTrue(all(len(value) == 2 for value in function_result.values()))


class TestProducts(TestCase):
    def test_result_type(self):
        function_result = products()
        self.assertTrue(isinstance(function_result, dict))

    def test_result_size(self):
        function_result = products()
        self.assertGreater(len(function_result.keys()), 1)

    def test_result_dict_keys(self):
        function_result = products()
        self.assertTrue(all(isinstance(key, str) for key in function_result.keys()))

    def test_result_dict_values(self):
        function_result = products()
        self.assertTrue(all(isinstance(value, dict) for value in function_result.values()))

    def test_result_dict_values_keys(self):
        function_result = products()
        self.assertTrue(all(all(isinstance(key, str) for key in sub_dict.keys())
                            for sub_dict in function_result.values()))

    def test_result_dict_values_values(self):
        function_result = products()
        self.assertTrue(all(all(isinstance(value, int) or isinstance(value, float)
                                for value in sub_dict.values())
                            for sub_dict in function_result.values()))

    def test_result_nutrient_content(self):
        expected_nutrients = ['calorie', 'proteins', 'carbs', 'sugar', 'fat']
        function_result = products()
        self.assertTrue(all(all(key in expected_nutrients for key in sub_dict.keys())
                            for sub_dict in function_result.values()))


class TestVariables(TestCase):
    def test_result_type(self):
        function_result = create_linear_programming_variables(dict())
        self.assertTrue(isinstance(function_result, dict))

    def test_result_size(self):
        function_result = create_linear_programming_variables(products())
        self.assertGreater(len(function_result.keys()), 0)

    def test_result_dict_keys(self):
        function_result = create_linear_programming_variables(products())
        self.assertTrue(all(isinstance(key, str) for key in function_result.keys()))

    def test_result_dict_values(self):
        function_result = create_linear_programming_variables(products())
        self.assertTrue(all(isinstance(value, LpVariable) for value in function_result.values()))


class TestConstraintsExists(TestCase):
    def test_result_type(self):
        prod_values = products()
        req_values = requirements()
        linear_variables = create_linear_programming_variables(prod_values)
        function_result = create_linear_constraints_diet_exists(
            linear_variables, prod_values, req_values)
        self.assertTrue(isinstance(function_result, list))

    def test_result_size(self):
        prod_values = products()
        req_values = requirements()
        linear_variables = create_linear_programming_variables(prod_values)
        function_result = create_linear_constraints_diet_exists(
            linear_variables, prod_values, req_values)
        self.assertGreater(len(function_result), 0)


class TestProblem(TestCase):
    def test_result_type(self):
        function_result = create_linear_programming_problem(None, list())
        self.assertTrue(isinstance(function_result, LpProblem))


class TestSolveLinearProblem(TestCase):
    def test_result_type(self):
        function_result = solve_linear_problem(LpProblem())
        self.assertTrue(isinstance(function_result, tuple))

    def test_result_size(self):
        function_result = solve_linear_problem(LpProblem())
        self.assertEqual(len(function_result), 3)

    def test_result_subtypes_1(self):
        function_result = solve_linear_problem(LpProblem())
        self.assertTrue(isinstance(function_result[0], LpProblem))
        self.assertTrue(function_result[1] is None)
        self.assertTrue(isinstance(function_result[2], int))

    def test_result_subtypes_2(self):
        problem = LpProblem()
        variable = LpVariable('x')
        problem += variable
        problem += (variable >= 0.0)
        function_result = solve_linear_problem(problem)
        self.assertTrue(isinstance(function_result[0], LpProblem))
        self.assertTrue(isinstance(function_result[1], LpAffineExpression))
        self.assertTrue(isinstance(function_result[2], int))


class TestObjective(TestCase):
    def test_result_type(self):
        prod_values = products()
        linear_variables = create_linear_programming_variables(prod_values)
        function_result = create_linear_objective_min_calorie(linear_variables, prod_values)
        self.assertTrue(isinstance(function_result, LpAffineExpression))


class TestConstraintsMinCalorie(TestCase):
    def test_result_type(self):
        prod_values = products()
        req_values = requirements()
        linear_variables = create_linear_programming_variables(prod_values)
        function_result = create_linear_constraints_min_calorie(
            linear_variables, prod_values, req_values)
        self.assertTrue(isinstance(function_result, list))

    def test_result_size(self):
        prod_values = products()
        req_values = requirements()
        linear_variables = create_linear_programming_variables(prod_values)
        function_result = create_linear_constraints_min_calorie(
            linear_variables, prod_values, req_values)
        self.assertGreater(len(function_result), 0)

    def test_result_types(self):
        prod_values = products()
        req_values = requirements()
        linear_variables = create_linear_programming_variables(prod_values)
        function_result = create_linear_constraints_min_calorie(
            linear_variables, prod_values, req_values)
        self.assertTrue(all(isinstance(elem, LpConstraint) for elem in function_result))
