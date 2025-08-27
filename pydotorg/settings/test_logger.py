import logging
import unittest
from django.test.runner import DiscoverRunner


class LoggingTestResult(unittest.TextTestResult):
    def startTest(self, test):
        # Called for every test just before it runs
        with open("test_order.log", "at") as f:
            f.write("%s\n" % test.id())
        super().startTest(test)


class LoggingTestRunner(unittest.TextTestRunner):
    # Ensure our result gets used
    resultclass = LoggingTestResult


class LoggingDiscoverRunner(DiscoverRunner):
    """
    Custom Django test runner that logs the order of test execution to a file.
    NOTE: The important bit is setting `test_runner` to our custom runner class.
    """
    test_runner = LoggingTestRunner
