'''
Created on Nov 5, 2018

@author: skanda
'''
#from ctypes.test.test_pickling import name



class Vehicle(object):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
    
    def reveal_identity(self):
        print("I am a {}".format(self.name))

# Inherit Make from the Super Class Vehicle
class Make(Vehicle):
    def __init__(self,parentattr, myattr):
        super(Make,self).__init__(parentattr)
        self.myattr = myattr
    def reveal_identity(self):
        super(Make,self).reveal_identity()
        print("...and am manufactured by {}".format(self.myattr))

a = Vehicle("cycle")
a.reveal_identity()

b = Make("car","Mercedes")
b.reveal_identity()



