from collections import deque
from nodeclass import  *
class Agent:
    def __init__(self,sizex,sizey):
        ##TODO: Put the variables you need for your agents here.
        self.board=[]
        self.nextmoves=deque()
        self.sizex=sizex
        self.sizey=sizey
        self.x=0
        self.y=0
    def move(self,state):
        ##TODO: Implement your algorithm here
        if len(self.nextmoves)!=0:
            return self.nextmoves.popleft()
        self.parsemessage(state[0])


        if self.ivegotyouinmysight():
            self.itshighnoon()
            return self.nextmoves.popleft()

        if self.checkgold():
            self.tovictory()
            return self.nextmoves.popleft()        

        nextx,nexty=self.checknextpos()
        x=self.x
        y=self.y
        history=set()
        path=deque()
        thepath=self.dfs(x,y,nextx,nexty,history,path)
        self.nextmoves=thepath
        self.x=nextx
        self.y=nexty
        print(self.x)
        print(self.y)
        return self.nextmoves.popleft()    