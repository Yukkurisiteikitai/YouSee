class VirtualPersonaData():
    def __init__(self):
        self.action_now = Actions()
        pass



class Actions():

    def __init__(self):
        self.activiery = 1
        self.__doc__ = 2

    def resistance(self):
        print("resistance")
    
    def adaptation(self):
        print('adaptation')
    
    def worry(self):
        print("attack")


person = VirtualPersonaData()
person.action_now.resistance()