def log(func):
    def wrapper(*args,**kw):
        # print('call %s():'%func.__name__)
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper 
@log
def now():
    print('2018-03-25') 
now()