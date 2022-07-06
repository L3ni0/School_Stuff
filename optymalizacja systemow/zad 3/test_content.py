from unittest import TestCase, TestSuite, TextTestRunner, makeSuite

from pulp import LpVariable, LpProblem, LpAffineExpression, LpConstraint

from content import *


class TestRunner:
    def __init__(self):
        self.runner = TextTestRunner(verbosity=2)

    def run(self):
        test_suite = TestSuite(tests=[
            makeSuite(TestInitialValues),
            makeSuite(TestCreateLinearVariables),
            makeSuite(TestColConstraints),
            makeSuite(TestRowConstraints),
            makeSuite(TestCellConstraints),
            makeSuite(TestUniqueConstraints),
            makeSuite(TestInitialConstraints),
            makeSuite(TestProblem),
            makeSuite(TestSolveLinearProblem),
            makeSuite(TestSolveSudoku),
        ])
        return self.runner.run(test_suite)


class TestInitialValues(TestCase):
    def test_result_type(self):
        function_result = initial_values()
        self.assertTrue(isinstance(function_result, list))

    def test_result_size(self):
        function_result = initial_values()
        self.assertGreater(len(function_result), 0)

    def test_result_dict_values(self):
        function_result = initial_values()
        self.assertTrue(all(isinstance(elem, tuple) for elem in function_result))

    def test_result_dict_values_structure(self):
        function_result = initial_values()
        self.assertTrue(all(len(elem) == 3 for elem in function_result))


class TestCreateLinearVariables(TestCase):
    def test_result_type(self):
        function_result = create_linear_programming_variables()
        self.assertTrue(isinstance(function_result, dict))

    def test_result_size(self):
        function_result = create_linear_programming_variables()
        self.assertGreater(len(function_result.keys()), 0)

    def test_result_dict_keys(self):
        function_result = create_linear_programming_variables()
        self.assertTrue(all(isinstance(key, tuple) for key in function_result.keys()))

    def test_result_dict_keys_structure(self):
        function_result = create_linear_programming_variables()
        self.assertTrue(all(len(key) == 3 for key in function_result.keys()))

    def test_result_dict_values(self):
        function_result = create_linear_programming_variables()
        self.assertTrue(all(isinstance(value, LpVariable) for value in function_result.values()))


class TestRowConstraints(TestCase):
    def test_result_type(self):
        function_result = create_row_constraints(create_linear_programming_variables())
        self.assertTrue(isinstance(function_result, list))

    def test_result_size(self):
        function_result = create_row_constraints(create_linear_programming_variables())
        self.assertEqual(len(function_result), 81)

    def test_result_values(self):
        function_result = create_row_constraints(create_linear_programming_variables())
        self.assertTrue(all(isinstance(elem, LpConstraint) for elem in function_result))


class TestColConstraints(TestCase):
    def test_result_type(self):
        function_result = create_col_constraints(create_linear_programming_variables())
        self.assertTrue(isinstance(function_result, list))

    def test_result_size(self):
        function_result = create_col_constraints(create_linear_programming_variables())
        self.assertEqual(len(function_result), 81)

    def test_result_values(self):
        function_result = create_col_constraints(create_linear_programming_variables())
        self.assertTrue(all(isinstance(elem, LpConstraint) for elem in function_result))


class TestCellConstraints(TestCase):
    def test_result_type(self):
        function_result = create_cell_constraints(create_linear_programming_variables())
        self.assertTrue(isinstance(function_result, list))

    def test_result_size(self):
        function_result = create_cell_constraints(create_linear_programming_variables())
        self.assertEqual(len(function_result), 81)

    def test_result_values(self):
        function_result = create_cell_constraints(create_linear_programming_variables())
        self.assertTrue(all(isinstance(elem, LpConstraint) for elem in function_result))


class TestUniqueConstraints(TestCase):
    def test_result_type(self):
        function_result = create_unique_constraints(create_linear_programming_variables())
        self.assertTrue(isinstance(function_result, list))

    def test_result_size(self):
        function_result = create_unique_constraints(create_linear_programming_variables())
        self.assertEqual(len(function_result), 81)

    def test_result_values(self):
        function_result = create_unique_constraints(create_linear_programming_variables())
        self.assertTrue(all(isinstance(elem, LpConstraint) for elem in function_result))


class TestInitialConstraints(TestCase):
    def test_result_type(self):
        function_result = create_initial_constraints(
            create_linear_programming_variables(), initial_values())
        self.assertTrue(isinstance(function_result, list))

    def test_result_size(self):
        function_result = create_initial_constraints(
            create_linear_programming_variables(), initial_values())
        self.assertEqual(len(function_result), len(initial_values()))

    def test_result_values(self):
        function_result = create_initial_constraints(
            create_linear_programming_variables(), initial_values())
        self.assertTrue(all(isinstance(elem, LpConstraint) for elem in function_result))


class TestProblem(TestCase):
    def test_result_type(self):
        function_result = create_linear_programming_problem(list())
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


class TestSolveSudoku(TestCase):
    def test_result_type(self):
        function_result = solve_sudoku(initial_values())
        self.assertTrue(isinstance(function_result, tuple))

    def test_result_size(self):
        function_result = solve_sudoku(initial_values())
        self.assertEqual(len(function_result), 4)

    def test_result_subtypes(self):
        function_result = solve_sudoku(initial_values())
        self.assertTrue(isinstance(function_result[0], dict))
        self.assertTrue(isinstance(function_result[1], LpProblem))
        self.assertTrue(function_result[2] is None)
        self.assertTrue(isinstance(function_result[3], int))

