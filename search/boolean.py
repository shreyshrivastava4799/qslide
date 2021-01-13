
class boolRet:

    def __init__(self, InvPosIdx):
        self.InvPosIdx = InvPosIdx

    def simpleIntersection(self, q_words):
        position = []
        print(self.InvPosIdx.keys())
        for word in q_words:
            if word in self.InvPosIdx.keys():
                position.append(self.InvPosIdx[word])
            # elif:
            # in case of spelling mistake check using soundex
            # else:
            # try a similar word present in vocabulary 
        return set.intersection(*position)