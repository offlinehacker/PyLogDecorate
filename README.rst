Have you ever wanted to have logging decorators for logging function calls and for automatic creation of logger object in class, based on class hierarchy.

If your answer is true, here is my implementation https://github.com/offlinehacker/PyLogDecorate. There is very nice option i’ve implemented called subdecorate, enabling for functions in derived classes being logged, even if decorator is only applied on base class function.

This logging decorator implementation can be easily extended.

- Install:
    python setup.py install or easy_install PyLogDecorate.

