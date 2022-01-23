import random as random

INT_SIZE = 4

RECORD_SIZE = 3*INT_SIZE

class record:
    
    Q = 0.0
    c = 0.0  
    m = 0.0
    dT = 0.0

    def __init__(self, c, m, dT):
        self.c = c
        self.m = m
        self.dT = dT
        self.Q = m*c*dT
    
    def getKey(self):
        return self.Q
    
    def __str__(self):
        return("Record "+str(self.Q)+": "+str(self.c)+" "+str(self.m)+" "+str(self.dT))

    def __bytes__(self):
        c_bytes = self.c.to_bytes(INT_SIZE, byteorder = "big")
        m_bytes = self.m.to_bytes(INT_SIZE, byteorder = "big")
        dT_bytes = self.dT.to_bytes(INT_SIZE, byteorder = "big")
        return c_bytes + m_bytes + dT_bytes

    @staticmethod
    def to_bytes(self):
        return bytes(self)

    @classmethod
    def from_bytes(cls, record_bytes):
        c = int.from_bytes(record_bytes[:INT_SIZE], byteorder = "big")
        m = int.from_bytes(record_bytes[INT_SIZE+1:2*INT_SIZE], byteorder = "big")
        dT = int.from_bytes(record_bytes[2*INT_SIZE:], byteorder = "big")
        return cls(c, m, dT)


def createRandomRecords(quantity):
    recordsList = []
    for i in range(quantity):
        c = random.randrange(1,20)
        m = random.randrange(1,20)
        dT = random.randrange(1,20)
        recordsList.append(record(c,m,dT))
    return recordsList

