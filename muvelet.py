class muvelet:
    szam1= 1
    szam2= 2
    def __init__(self,szam1,szam2):
        self.szam1=szam1
        self.szam2=szam2
    def osszeadas(self):
        return self.szam1 + self.szam2
    def kivonas(self):
        return self.szam1 - self.szam2
    def szorzas(self):
        return self.szam1 * self.szam2
    def osztas(self):
        return self.szam1 / self.szam2







if __name__=="__main__":
    q=muvelet(2,2)
    print(q.osszeadas())
    
    q=muvelet(2,2)
    print(q.kivonas())

    q=muvelet(2,2)
    print(q.szorzas())

    q=muvelet(2,2)
    print(q.osztas())
"""
class muvelet:
    szam1= 1
    szam2= 2
    def osszeadas(self):
        self.szam1=szam1
        self.szam2=szam2
        vissza=szam1+szam2
        return vissza
    
    def kivonas(self):
        self.szam1=szam1
        self.szam2=szam2
        vissza=szam1 - szam2
        return vissza

    def szorzas(self):
        self.szam1=szam1
        self.szam2=szam2
        vissza=szam1 * szam2
        return vissza
    
    def osztas(self):
        self.szam1=szam1
        self.szam2=szam2
        vissza=szam1 / szam2
        return vissza
        
    
    
muvelet.osszeadas()
"""
