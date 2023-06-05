
class szo:
    def __init__(self,szo):
        self.szo=szo

    def minta(self,szo):
        vissza=""
        for i in range(6):
            if szo[i]==self.szo[i]:
                vissza +=szo[i]

            else:
                vissza+="."
        return vissza
