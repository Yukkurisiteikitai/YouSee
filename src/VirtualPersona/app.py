class VirtualPersonaData():
    def __init__(self):
        self.action_now = Actions()
        pass



class Actions():

    def __init__(self):
        self.activiery = 1
        self.__doc__ = 2

    def rec(self):
        print("recording")
    
    def adaptation(self):
        print('adaptation')
    
    def delete(self):
        print("delete")


person = VirtualPersonaData()
person.action_now.rec()