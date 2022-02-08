class Player:
    def __init__(self,turn,piece):
        self._turn=turn
        self._piece=piece
        self.score=0


    def getTurn(self):
        return self._turn    


    def getPiece(self):  
      return self._piece

    def getScore(self):
            return self.score




        