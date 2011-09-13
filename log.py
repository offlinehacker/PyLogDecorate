import os
import sys
import logging
import inspect
import traceback

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt='%m-%d %H:%M'
    )

def keyIsTrue(dic, key):
    if not dic:
        return False
    
    if dic.has_key(key) and dic[key]==True:
        return True
    
    return False

def toStr(obj):
    try: 
        return str(obj)
    except:
        return str(type(obj))

def toShortStr(obj, max=20):
    s = toStr(obj)
    if len(s) > max:
        return toStr(type(obj))
    return s

class LogCallBase(object):
    '''
    Base log calls on functions.
    
    If used in connection with LogClass decorator it uses logger 
    object created by that decorator.
    '''
    def __init__(self, args=None):
        self.args= args
        if not self.args: self.args= {}
        
    def __call__(self, fn):
        """Log calls to fn, reporting caller, args, and return value"""
                
        return self.hook(fn)
        
    def hook(self, fn):
        def wrapped_f(*args):
            # Report exceptions before letting them bubble
            err = None
            
            try:
                result = fn(*args)
            except Exception, e:
                result = "CRASHED"
                err = e
        
            try:
                try:
                    frame = sys._getframe(1)
                    
                    # In case we find args and first parameter with class type.
                    if args and inspect.isclass(type(args[0])):
                        if hasattr(args[0], "logger"):
                            logger= args[0].logger
                        else:
                            logger = logging.getLogger(fn.__module__+"."+fn.__class__.__name__)
                    else:
                        # Get a logger named after the module hierarchy      
                        logger = logging.getLogger(fn.__module__)
                        
                    self.log_f(logger, frame, fn, args, {}, result)
        
                except Exception, e:
                    # See http://docs.python.org/library/inspect.html#the-interpreter-stack
                    del frame
                    err= e
                    raise e
        
            finally:
                if err:
                    raise err 
                else:
                    return result
                
        if keyIsTrue(self.args, "subdecorate"):
            wrapped_f.__subdecorate__= self
                
        return wrapped_f
    
    def log_f(self, logger, frame, fn, args, kw, result):
        '''
        This function gets called when we log. Override it.
        @param logger: logger to use for logging.
        @type logger: Logger
        @param frame: Python frame object.
        @type frame: frame
        @param fn: Function which was called.
        @type fn: function
        @param args: Arguments to function.
        @type args: list
        @param kw: Kw aruments to function
        @type kw: dictionary
        @param result: Result from a function.
        @type result: unknown
        '''
        pass
    
class LogCall(LogCallBase):
    '''
    Log calls on functions.
    
    If used in connection with LogClass decorator it uses logger 
    object created by that decorator.
    '''
    def log_f(self, logger, frame, fn, args, kw, result):
        # Format the args and kw args as a comma-separated list
        arglist = ', '.join(map(toShortStr, args))
        if kw:
            arglist += ', ' + ', '.join(map(lambda k: '%s=%s' % (toStr(k), toShortStr(kw[k])), kw.keys()))

        logger.debug("%(file)s %(line)d: %(func)s(%(args)s) -> %(ret)s" % ( 
                        {'file': os.path.relpath(frame.f_code.co_filename),
                         'line': frame.f_lineno,
                         'func': fn.__name__,
                         'args': arglist,
                         'ret': toShortStr(result)
                         }))
    
class LogClass(object):
    '''
    Decorator for logging in classes.
    
    This decorator creates Logger as logger attribute on instance
    in class it is used on. It supports input parameters and has
    support for decorator inheritance if used in connection with
    LogFunction.
    '''
    def __init__(self, args=None):
        '''
        Input parameters for decorator.
        @param args: Dictionary of additional parameters.
                     Currently there are these supported:
                     * subdecorate - Decorate all functions which have
                         LogFunction decorator and subdecorate option
                         in base class on all sub classes.
                     *inherit_logger - Inherit logger from base class or not.
        @type args: Dictionary
        '''
        self.args= args
        
    def __call__(self, klas):
        self.klas= klas
        if hasattr(klas, "__init__"):
            self.original_init= klas.__init__ 
        else: self.original_init= None
        
        if keyIsTrue(self.args, "subdecorate"):
            klas.__subdecorate__= self
        
        parent= inspect.getmro(klas)[1]
        if hasattr(parent,"__subdecorate__"):
            for key in parent.__dict__:
                fn= getattr(parent, key)
                if hasattr(fn, "__subdecorate__"):
                    if hasattr(klas, key):
                        setattr(klas,key,fn.__subdecorate__.hook(getattr(klas,key)))
        
        def _init(instance, *args, **kws):
            # we must check if logger already exists.
            if not( hasattr(instance,"logger") and instance.logger ) \
               or not keyIsTrue(self.args["inherit_logger"]):
                instance.logger= logging.getLogger(instance.__class__.__module__+"."+ \
                                                   instance.__class__.__name__)
            # In case we specific level set level for class.
            if self.args and self.args["level"]:
                instance.logger.setLevel(self.args["level"])
                
            if self.original_init:
                self.original_init(instance, *args, **kws) # call the original __init__
        
        klas.__init__ = _init # set the class' __init__ to the new one
        return klas

