# напиши здесь код создания и управления картой Loadland
class map_manager():
    def __init__(self):
        self.model = 'block'
        self.texture ='block.png'
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.color = (0.2,0.2,0.35,1)
        self.startNew()
        self.addBlock((0,10,0))
    def startNew(self):
        self.land = render.attachNewNode("land")
    def addBlock(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    #def get_color(self):
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def Load_Land(self,filename):
        self.clear()
        with open(filename) as file:
            y=0
            for line in file:
                x=0
                line=line.split(' ')
                for z in line:
                    for z1 in range(int(z)+1):
                        block = self.addBlock((x,y,z1))
                    x +=1
                y+=1
            return x,y 
    def findBlock(self,pos):
        return self.land.fundAllMatches("=at=",str(pos))
    def isEmpty(self,pos):
        blocks=self.findBlock(pos)
        if blocks:
            return False
        else:
            return True
    def findHigiestEmpty(self,pos):
        x,y,z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)
