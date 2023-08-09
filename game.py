# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import map_manager
from hero import Hero
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = map_manager()
        base.camLens.setFov(90)
        x,y=self.land.Load_Land("land.txt")
        self.hero = Hero((x//2,y//2,2),self.land)

        
game = Game()
game.run()