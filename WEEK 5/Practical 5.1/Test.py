class Player():

    def __init__(self, num):
        self.num = num

    def __contains__(self, substring):
        if substring in self.num:
            return True
        else:
            return False

obj1 = Player("101")
print ('0' in obj1)
print ('ami' in obj1)