import os
import sys
from setuptools import setup, find_packages

reload(sys)
sys.setdefaultencoding("utf-8")

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a 
# top level
# README file and 2) it's easier to type in the README file than to put 
# a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyLogDecorate",
    version = "0.1",
    author = "Jaka Hudoklin",
    author_email = "jakahudoklin@gmail.com",
    description = ("Advanced python logging decorators."),
    license = "BSD",
    keywords = "python logging decorators",
    url = "https://github.com/offlinehacker/PyLogDecorate",
    packages=find_packages(),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License"
    ]
)
