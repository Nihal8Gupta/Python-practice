class Player:
    def __init__(self,n,c,a,m,r,w):
        self.Pname=n
        self.Pcontry=c
        self.Page=a
        self.Pmatch=m
        self.Prun=r
        self.Pwicket=w

class Team:
    Tname='India'
    
    def __init__(self,n):
        self.Tnum=n
        self.Tplayerlist=[]
        for i in range(1,self.Tnum+1):
            pn=input(f'{i} Player name:')
            pc=input(f'{i} Player Country:')
            pa=input(f'{i} Player Age:')
            pm=int(input(f'{i} Number of Matches:'))
            pr=int(input(f'{i} Player runs:'))
            pw=int(input(f'{i} Player wickets:'))
            obj=Player(pn,pc,pa,pm,pr,pw)
            self.Tplayerlist.append(obj)
    
    def team_score(self):
        score=0
        for i in self.Tplayerlist:
            score+=i.Prun
        print('Total Runs:',score)
    def max_run(self):
        self.m=self.Tplayerlist[0]
        for i in self.Tplayerlist:
            if i.Prun>self.m.Prun:
                self.m=i

        print(f'Max Runs {self.m.Prun} by {self.m.Pname}')
    def max_wicket(self):
        self.w=self.Tplayerlist[0]
        for i in self.Tplayerlist:
            if i.Pwicket>self.w.Pwicket:
                self.w=i
        print(f'Max wicket {self.w.Pwicket} by {self.w.Pname}:')
        
ind=Team(2)
ind.team_score()
ind.max_run()
ind.max_wicket()         