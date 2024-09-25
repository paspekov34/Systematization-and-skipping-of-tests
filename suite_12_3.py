import unittest
import metod_unittest_2
import Prostoy_unittest

run_test = unittest.TestSuite()
tour_test = unittest.TestSuite()
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Prostoy_unittest.RunnerTest))
tour_test.addTest(unittest.TestLoader().loadTestsFromTestCase(metod_unittest_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_test)
runner.run(tour_test)
