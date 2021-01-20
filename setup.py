import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import sdist_upip

setup(name='mojotest-dht.mojotest_dht',
      version='0.1',
      description='Simple test package.',
      long_description='',
      url='https://github.com/bandra123/mojotest-modules',
      author='Rohit Sharma',
      author_email='rohit515000@gmail.com',
      maintainer='Rohit Sharma',
      maintainer_email='rohit515000@gmail.com',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      packages=['mojotest_dht'])
