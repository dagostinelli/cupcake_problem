from setuptools import setup

setup(
	name='cupcake',
	version='1.0',
	package_dir={'cupcake': 'cupcake', 'cupcake.tests': 'tests'},
	packages=['cupcake', 'cupcake.tests']
)
