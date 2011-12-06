import os
import sys
import string
from setuptools import setup, find_packages

reload(sys)
sys.setdefaultencoding("utf-8")

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
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License"
    ]
)
