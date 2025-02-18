"""Runs your code against a local version of the assignment database
to let you test locally before you submit to the autograder.

This code will check the number of rows in your output as well as the
first and last row. While passing these tests is a good indicator,
it's possible that you might have an error in your query and still pass these
tests. Your local copy of the assignment database is different from
the copy the autograder uses, so the autograder will look for 
different results than what you see checked here. 
"""
import unittest
import sqlite3
from sql_lab import LabSuite


class LabTestMethods(unittest.TestCase):
    def setUp(self):
        self.lab = LabSuite()
        self.conn = sqlite3.connect('./assignment.db')
    
    def tearDown(self):
        self.conn.close()

    def test_five_year_rangers(self):
        # Tests the pre-written five_year_rangers function.
        # If you haven't modified that function, you should 
        # always pass this test.
        cursor = self.conn.cursor()
        cursor.execute("""SELECT firstname, lastname
                            FROM Ranger
                            WHERE years_worked = 5
                            ORDER BY lastname, firstname""")
        results = cursor.fetchall()
        output = self.lab.five_year_rangers()
        self.assertEqual(results,output,"five_year_rangers() does not produce expected output; be sure you didn't modify the function.")

    def test_find_overlooks(self):
        # Tests the find_overlooks function.
        # On the test database, this should return six rows.
        # The first row should be ('Overlook Estrada',)
        # and the last should be ('Overlook Zimmerman',).
        expected_rows, expected_first, expected_last = 6, ('Overlook Estrada',), ('Overlook Zimmerman',)
        output = self.lab.find_overlooks()
        self.assertEqual(expected_rows, len(output), "Incorrect output length; expected {} rows.".format(expected_rows))
        self.assertEqual(expected_first,output[0],"Incorrect first row; expected {}.".format(expected_first))
        self.assertEqual(expected_last,output[-1],"Incorrect last row; expected {}.".format(expected_last))

    def test_find_station_elevation(self):
        # Tests the find_station_elevation function.
        # On the test database, this should return eleven rows.
        # The first row should be ('Overlook Estrada', 0.575)
        # and the last should be ('Station Vaughan', 0.428219696969697).
        expected_rows, expected_first, expected_last = 11, ('Overlook Estrada', 0.575), ('Station Vaughan', 0.428219696969697)
        output = self.lab.find_station_elevation()
        self.assertEqual(expected_rows, len(output), "Incorrect output length; expected {} rows.".format(expected_rows))
        self.assertEqual(expected_first,output[0],"Incorrect first row; expected {}.".format(expected_first))
        self.assertEqual(expected_last,output[-1],"Incorrect last row; expected {}.".format(expected_last))

    def test_find_average_deer(self):
        # Tests the find_average_deer function.
        # On the test database, this should return one row.
        # The only row produced should be (3.5806451612903225,).
        expected_rows, expected_first, expected_last = 1, (3.5806451612903225,), None
        output = self.lab.find_average_deer()
        self.assertEqual(expected_rows, len(output), "Incorrect output length; expected {} rows.".format(expected_rows))
        self.assertEqual(expected_first,output[0],"Incorrect first row; expected {}.".format(expected_first))

    def test_find_station_seven_animals(self):
        # Tests the find_station_seven_animals function.
        # On the test database, this should return ten rows.
        # The first row should be ('Bear', 9)
        # and the last should be ('Skunk', 22).
        expected_rows, expected_first, expected_last = 10, ('Bear', 9), ('Skunk', 22)
        output = self.lab.find_station_seven_animals()
        self.assertEqual(expected_rows, len(output), "Incorrect output length; expected {} rows.".format(expected_rows))
        self.assertEqual(expected_first,output[0],"Incorrect first row; expected {}.".format(expected_first))
        self.assertEqual(expected_last,output[-1],"Incorrect last row; expected {}.".format(expected_last))
    
    def test_find_birdwatchers(self):
        # Tests the find_birdwatchers function.
        # On the test database, this should return eleven rows.
        # The first row should be ('Tiffany', 'Abbott')
        # and the last should be ('Courtney', 'Price').
        expected_rows, expected_first, expected_last = 11, ('Tiffany', 'Abbott'), ('Courtney', 'Price')
        output = self.lab.find_birdwatchers()
        self.assertEqual(expected_rows, len(output), "Incorrect output length; expected {} rows.".format(expected_rows))
        self.assertEqual(expected_first,output[0],"Incorrect first row; expected {}.".format(expected_first))
        self.assertEqual(expected_last,output[-1],"Incorrect last row; expected {}.".format(expected_last))

    def test_find_distant_stations(self):
        # Tests the find_distant_stations function.
        # On the test database, this should return two rows.
        # The first row should be ('Point Taylor', 14643)
        # and the last should be ('Courtney', 'Price').
        expected_rows, expected_first, expected_last = 2, ('Point Taylor', 14643), ('Overlook Zimmerman', 14842)
        output = self.lab.find_distant_stations()
        self.assertEqual(expected_rows, len(output), "Incorrect output length; expected {} rows.".format(expected_rows))
        self.assertEqual(expected_first,output[0],"Incorrect first row; expected {}.".format(expected_first))
        self.assertEqual(expected_last,output[-1],"Incorrect last row; expected {}.".format(expected_last))
    
    def test_find_wild_stations(self):
        # Tests the find_wild_stations function.
        # On the test database, this should return eleven rows.
        # The first row should be ('Overlook Estrada', 9)
        # and the last should be ('Station Vaughan', 10).
        expected_rows, expected_first, expected_last = 11, ('Overlook Estrada', 9), ('Station Vaughan', 10)
        output = self.lab.find_wild_stations()
        self.assertEqual(expected_rows, len(output), "Incorrect output length; expected {} rows.".format(expected_rows))
        self.assertEqual(expected_first,output[0],"Incorrect first row; expected {}.".format(expected_first))
        self.assertEqual(expected_last,output[-1],"Incorrect last row; expected {}.".format(expected_last))
    
    def test_find_first_worker(self):
        # Tests the find_first_worker function.
        # On the test database, this should return one row.
        # The only row produced should be ('Carrie', 'Brooks').
        expected_rows, expected_first, expected_last = 1, ('Carrie', 'Brooks'), None
        output = self.lab.find_first_worker()
        self.assertEqual(expected_rows, len(output), "Incorrect output length; expected {} rows.".format(expected_rows))
        self.assertEqual(expected_first,output[0],"Incorrect first row; expected {}.".format(expected_first))
    
if __name__ == '__main__':
    unittest.main()