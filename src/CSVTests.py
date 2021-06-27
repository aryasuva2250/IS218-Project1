import unittest
from CsvReader import CsvReader, ClassFactory
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('src/TestFiles/Addition.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__ )
'''
class MyTestCase2(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('src/TestFiles/Multiplication.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__ )


class MyTestCase3(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('src/TestFiles/Subtraction.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__ )

class MyTestCase4(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('src/TestFiles/Square.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__ )

class MyTestCase5(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('src/TestFiles/SquareRoot.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__ )

class MyTestCase6(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('src/TestFiles/Division.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__ )
'''

if __name__ == '__main__':
    unittest.main()
