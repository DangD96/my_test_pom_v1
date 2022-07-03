# import sys
# sys.path.append("/Users/daviddang/python/my_test_pom_v1") #add my prj directory path to PATH so I can import stuff

from unittest import TestLoader, TestSuite, TextTestRunner, TestCase
from Tests.Scripts.test_Home_Page import DemoHomePage
from Tests.Scripts.test_Contact_Us_Page import DemoContactPage

load1 = TestLoader().loadTestsFromTestCase(DemoHomePage)
load2 = TestLoader().loadTestsFromTestCase(DemoContactPage)

# Test Suite is used since there are multiple test cases
# Passing in tuple because TestSuite argument has to be one
test_suite = TestSuite((load1,load2))

test_runner = TextTestRunner(verbosity=2)
test_runner.run(test_suite)

# https://docs.python.org/3/library/unittest.html#classes-and-functions
# Refer https://testtools.readthedocs.io/en/latest/api.html for more information
# parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
# parallel_suite.run(testtools.StreamResult())
# self.driver.set_page_load_timeout(30))
# view raw FileName - Search_Test_TestSuite_TestRunner.py hosted with ❤ by GitHub
