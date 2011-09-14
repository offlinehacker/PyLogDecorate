from log import LogCall, LogClass

@LogCall()
def test():
    print "x"

@LogClass({"subdecorate": True})
class test1(object):
    name="kekec" 
    name2="kekec2"
    @LogCall({"subdecorate": True, "tracename": "tracetest", "traceattr": "name"})
    def test(self):
        pass
    
    @LogCall({"subdecorate": True, "tracename": "tracetest", "traceattr": "name2"})  
    def test2(self):
        self.logger.debug("Inside base class!")

@LogClass()
class test2(test1):
    def __init__(self):
        pass
    
    def test(self):
        self.logger.debug("Inside funtion.")
        self.test2()
        
@LogClass()   
class test3(test2):
    def __init__(self):
        pass
    
    def test(self):
        self.logger.debug("Inside funtion2.")
        self.test2()
    
    
test()
b=test3()
c=test2()
b.test()
c.test()
