from log import LogCall, LogClass

@LogCall()
def test():
    print "x"

@LogClass({"subdecorate": True})
class test1(object):
            
    @LogCall({"subdecorate": True})
    def test(self):
        print "znj"
    

@LogClass()
class test2(test1):
    def __init__(self):
        pass
    
    def test(self):
        print 1/1
    
    
test()
b=test2()
b.test()