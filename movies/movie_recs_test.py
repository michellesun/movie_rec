import unittest
import movie_recs

class TestSequenceFunctions(unittest.TestCase):

    def movie_details(self): 
        self.assertEqual(movie_recs.movie_details(1), 'Toy Story (1995)')

if __name__ == '__main__':
    unittest.main()