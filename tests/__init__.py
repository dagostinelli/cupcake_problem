from unittest import *
from .cupcake import cupcakeTest

def tests():
	suite = TestSuite()
	suite.addTest(makeSuite(cupcakeTest))
	return suite
