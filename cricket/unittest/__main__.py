'''
This is the main entry point for running unittest test suites.
'''
from cricket.app import main as cricket_main
from cricket.unittest.model import UnittestTestSuite


def main():
    return cricket_main(UnittestTestSuite)


if __name__ == "__main__":
    main().main_loop()
