import os
import sys
import string
from setuptools import setup, find_packages

reload(sys)
sys.setdefaultencoding("utf-8")

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a 
# top level
# README file and 2) it's easier to type in the README file than to put 
# a raw
# string in below ...
## {{{ http://code.activestate.com/recipes/66055/ (r1)
def reindent(s, numSpaces):
    s = string.split(s, '\n')
    s = [(numSpaces * ' ') + line for line in s]
    s = string.join(s, '\n')
    return s
## end of http://code.activestate.com/recipes/66055/ }}}

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyLogDecorate",
    version = "0.333",
    author = "Jaka Hudoklin",
    author_email = "jakahudoklin@gmail.com",
    description = ("Advanced python logging decorators."),
    license = "BSD",
    keywords = "python logging decorators",
    url = "https://github.com/offlinehacker/PyLogDecorate",
    packages=find_packages(),
    long_description=read('README.rst')+"\n- Example code:\n\n ::\n\n"+reindent(read("PyLogDecorate/logtest.py"),4),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License"
    ]
)
