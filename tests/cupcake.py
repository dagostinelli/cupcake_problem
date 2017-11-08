from unittest import TestCase

from cupcake import cupcake

class cupcakeTest(TestCase):
	def setup(self):
		self.x = 1

	def test_nothing(self):
		self.assertEquals(True, True)

	def test_hello_world(self):
		cupcake.hello_world()
		self.assertEquals(True, True)
