from PyLogDecorate.log import LogCall, LogClass

@LogCall()
def test():
    print "x"

@LogClass({"subdecorate": True})
class test1(object):
            
    @LogCall({"subdecorate": True, "tracename": "tracetest"})
    def test(self):
        print "znj"
    

@LogClass()
class test2(test1):
    def __init__(self):
        pass
    
    def test(self):
        self.logger.debug("Inside funtion.")
    
    
test()
b=test2()
b.test()