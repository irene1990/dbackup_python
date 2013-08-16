import sys
sys.path.append(r'/home/irene/Documents/python/Class/System')
import role,storage,user,sequence,warning
class SystemManager:
    def __init__(self):
        pass
    def roleM(self):
        role.Massge()
        role.Setting()
        role.Catalog()
    def storageM(self):
        storage.Check()
        storage.Add()
        storage.Invalid()
    def userM(self):
        user.Check()
        user.Add()
    def sequence(self):
        sequence.Check()
        sequence.AddClient()
        sequence.AddDB()
    def warning(self):
        pass
