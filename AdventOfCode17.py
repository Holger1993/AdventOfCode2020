
class PosState:
    def __init__(self,x,y,z,act):
        self.xpos = x
        self.ypos = y
        self.zpos = z
        if act == '.':
            self.on = False
        else:
            self.on = True
    def stateOf(self,x,y,z):
        return self.on

cube = [['.','#','.'],['.','.','#'],['#','#','#']]

a = PosState(0,0,0,'.')
append(PosState(0,1,0,'#'))
print(a.stateOf(0,0,0))