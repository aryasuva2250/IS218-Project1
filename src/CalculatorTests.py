import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self): #tests the instanstiation of the calculator object
        self.assertIsInstance(self.calculator, Calculator)
    '''
    def test_addition(self):
        testData = CsvReader("src/Addition.csv").data
        for row in testData:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)
    '''
    '''
    def test_multiplication(self):
        testData = CsvReader("src/Multiplication.csv").data
        for row in testData:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)
    '''
    '''
    def test_subtraction(self):
        testData = CsvReader("src/Subtraction.csv").data
        for row in testData:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)
    '''
    '''
    def test_square(self):
        testData = CsvReader("src/Square.csv").data
        for row in testData:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squaring(row['Value 1']), result)
            pprint(row)
    '''
    def test_square_root(self):
        testData = CsvReader("src/SquareRoot.csv").data
        for row in testData:
            result = round(float(row['Result']), 8)
            self.assertEqual(self.calculator.sqrt(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)

    '''
    def test_division(self):
        testData = CsvReader("src/Division.csv").data
        for row in testData:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)
    '''

   # def test_results_property_calculator(self):
    #    self.assertEqual(self.calculator.result, 0)
   # def test_add_method_calculator(self):
    #    self.assertEqual(self.calculator.add(2, 2), 4)
    #    self.assertEqual(self.calculator.result, 4)
   # def test_subtract_method_calculator(self):
    #    self.testData = CsvReader('datafileaddition.csv').data
     #   self.assertEqual(self.calculator.subtract(2, 2), 0)
      #  self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
