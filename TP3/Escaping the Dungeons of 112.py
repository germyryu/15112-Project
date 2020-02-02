import module_manager
module_manager.review()
import pygame,sys
import random
import os
import math
import copy

#all object images were from opengameart.org
class Objects(pygame.sprite.Sprite):
    def __init__ (self,x,y,image):
        self.x=x
        self.y=y
        self.image=image
    def draw(self,surface):
        surface.blit(self.image,(self.x,self.y))

class BigTable(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","bigtable.png"))
        image=pygame.transform.rotozoom(image,0,0.8)
        super().__init__ (x,y,image)
class SmallTable(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","smalltable.png"))
        image=pygame.transform.rotozoom(image,0,0.8)
        super().__init__ (x,y,image)
class TV(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","tv.png"))
        image=pygame.transform.rotozoom(image,0,1.1)
        super().__init__ (x,y,image)
class Sofa(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","sofa.png"))
        image=pygame.transform.rotozoom(image,0,0.08)
        super().__init__ (x,y,image)
class Cupboard(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","cupboard.png"))
        image=pygame.transform.rotozoom(image,0,0.8)
        super().__init__ (x,y,image)
class Fridge(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","fridge.png"))
        image=pygame.transform.rotozoom(image,0,0.5)
        super().__init__ (x,y,image)
class Oven(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","oven.png"))
        image=pygame.transform.rotozoom(image,0,0.6)
        super().__init__ (x,y,image)
class Microwave(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","microwave.png"))
        image=pygame.transform.rotozoom(image,0,0.95)
        super().__init__ (x,y,image)
class Key(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","key.png"))
        image=pygame.transform.rotozoom(image,0,0.5)
        super().__init__ (x,y,image)
        self.rect=image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
class Fireplace(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","fireplace.png"))
        image=pygame.transform.rotozoom(image,0,0.15)
        super().__init__ (x,y,image)
class Coin(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        self.frame=0
        self.img=[]
        for i in range(1,9):
            img=pygame.image.load(os.path.join("objects","coin"+str(i)+".png"))
            self.img.append(img)
        image=self.img[0]
        super().__init__ (x,y,image)
        self.rect=image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
    def update(self):
        self.frame+=1
        self.image=self.img[self.frame%8]
class Torch(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        self.frame=0
        self.img=[]
        for i in range(1,10):
            img=pygame.image.load(os.path.join("objects","torch"+str(i)+".png"))
            img=pygame.transform.rotozoom(img,0,0.8)
            self.img.append(img)
        image=self.img[0]
        super().__init__ (x,y,image)
    def update(self):
        self.frame+=1
        self.image=self.img[self.frame%9]
class Shelf1(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","shelf1.png"))
        image=pygame.transform.rotozoom(image,0,0.2)
        super().__init__ (x,y,image)
class Shelf2(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load(os.path.join("objects","shelf2.png"))
        image=pygame.transform.rotozoom(image,0,0.2)
        super().__init__ (x,y,image)
class Scorecoin(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load("scorecoin.png")
        image=pygame.transform.rotozoom(image,0,0.5)
        super().__init__ (x,y,image)
class Door(Objects):
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        image=pygame.image.load("door.png")
        image=pygame.transform.scale(image,(76,80))
        super().__init__ (x,y,image)
        self.rect=image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

class Maze(object):
    def __init__(self):
        self.col = 29
        self.row = 17
        self.walls=[]
        self.maze =[\
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1],
[1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1],
[1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,1,0,0,1],
[1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1],
[1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1],
[1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0,1],
[1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1],
[1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1],
[1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
    def getMazeRect(self,image):
        for i in range(self.row):
            for j in range(self.col):
                if self.maze[i][j]==1:
                    self.rect=image.get_rect()
                    self.rect.x=j*44
                    self.rect.y=i*44
                    self.walls.append(self.rect)
    
    def draw(self,surface,image,floor):
        for i in range(self.row):
            for j in range(self.col):
                if self.maze[i][j]==1:
                    surface.blit(image,(j*44,i*44))
                elif self.maze[i][j]==0:
                    surface.blit(floor,(j*44,i*44))

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        self.x=x
        self.y=y
        self.image=image
    def draw(self,surface):
        surface.blit(self.image,(self.x,self.y))

class Student(Player):
    def __init__(self,screenWidth,screenHeight):
        x=0
        y=screenHeight-100
        self.up=[]
        self.right=[]
        self.down=[]
        self.left=[]
        self.dir="down"
        for i in range(1,4):
            img=pygame.image.load(os.path.join("student","walk"+str(i)+".png"))
            img=pygame.transform.rotozoom(img,0,0.5)
            self.up.append(img)
        for i in range(4,7):
            img=pygame.image.load(os.path.join("student","walk"+str(i)+".png"))
            img=pygame.transform.rotozoom(img,0,0.5)
            self.right.append(img)
        for i in range(7,10):
            img=pygame.image.load(os.path.join("student","walk"+str(i)+".png"))
            img=pygame.transform.rotozoom(img,0,0.5)
            self.down.append(img)
        for i in range(10,13):
            img=pygame.image.load(os.path.join("student","walk"+str(i)+".png"))
            img=pygame.transform.rotozoom(img,0,0.5)
            self.left.append(img)
        image=self.down[1]
        super().__init__(x,y,image)
        self.rect=image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.upspeed=4
        self.downspeed=4
        self.rightspeed=4
        self.leftspeed=4
        self.frame=0

    def update(self,keysDown):
        self.frame+=1
        if keysDown(ord("a")) and keysDown(pygame.K_LSHIFT):
            self.leftspeed=10
            self.dir="left"
        elif keysDown(ord("d")) and keysDown(pygame.K_LSHIFT):
            self.rightspeed=10
            self.dir="right"
        elif keysDown(ord("w")) and keysDown(pygame.K_LSHIFT):
            self.upspeed=10
            self.dir="up"
        elif keysDown(ord("s")) and keysDown(pygame.K_LSHIFT):
            self.downspeed=10
            self.dir="down"
        else:
            self.leftspeed=4
            self.rightspeed=4
            self.upspeed=4
            self.downspeed=4
            
        if keysDown(pygame.K_LEFT) or keysDown(ord('a')):
            self.image=self.left[self.frame%3]
            self.x-=self.leftspeed
            self.rect.x-=self.leftspeed
            self.dir="left"
        elif keysDown(pygame.K_RIGHT) or keysDown(ord('d')):
            self.image=self.right[self.frame%3]
            self.x+=self.rightspeed
            self.rect.x+=self.rightspeed
            self.dir="right"
        elif keysDown(pygame.K_UP) or keysDown(ord('w')):
            self.image=self.up[self.frame%3]
            self.y-=self.upspeed
            self.rect.y-=self.upspeed
            self.dir="up"
        elif keysDown(pygame.K_DOWN) or keysDown(ord('s')):
            self.image=self.down[self.frame%3]
            self.y+=self.downspeed
            self.rect.y+=self.downspeed
            self.dir="down"

class Neighbor(Player):
    def __init__(self,screenWidth,screenHeight):
        x=838
        y=361
        self.up=[]
        self.right=[]
        self.down=[]
        self.left=[]
        for i in range(1,8):
            img=pygame.image.load(os.path.join("neighbor","bad"+str(i)+".png"))
            img=pygame.transform.rotozoom(img,0,0.5)
            self.up.append(img)
        for i in range(22,29):
            img=pygame.image.load(os.path.join("neighbor","bad"+str(i)+".png"))
            img=pygame.transform.rotozoom(img,0,0.5)
            self.right.append(img)
        for i in range(15,22):
            img=pygame.image.load(os.path.join("neighbor","bad"+str(i)+".png"))
            img=pygame.transform.rotozoom(img,0,0.5)
            self.down.append(img)
        for i in range(8,15):
            img=pygame.image.load(os.path.join("neighbor","bad"+str(i)+".png"))
            img=pygame.transform.rotozoom(img,0,0.5)
            self.left.append(img)
        image=self.down[0]
        super().__init__ (x,y,image)
        self.rect=image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.restupSpeed=2
        self.restdownSpeed=2
        self.restleftSpeed=2
        self.restrightSpeed=2
        self.chaseupSpeed=4
        self.chasedownSpeed=4
        self.chaseleftSpeed=4
        self.chaserightSpeed=4
        self.state="rest"
        self.direction=["left","right","up","down"]
        self.dir=self.direction[3]
        self.frame=0
    
    def chase(self,player):
        if self.x<player.x:
            self.x+=self.chaserightSpeed
            self.rect.x+=self.chaserightSpeed
            self.image=self.right[self.frame%7]
        if self.x>player.x:
            self.x-=self.chaseleftSpeed
            self.rect.x-=self.chaseleftSpeed
            self.image=self.left[self.frame%7]
        if self.y<player.y:
            self.y+=self.chasedownSpeed
            self.rect.y+=self.chasedownSpeed
            self.image=self.down[self.frame%7]
        if self.y>player.y:
            self.y-=self.chaseupSpeed
            self.rect.y-=self.chaseupSpeed
            self.image=self.up[self.frame%7]
    
    def update(self,player):
        self.frame+=1
        if self.state=="rest":
            if self.dir=="left":
                self.x-=self.restleftSpeed
                self.rect.x-=self.restleftSpeed
                self.image=self.left[self.frame%7]
            elif self.dir=="right":
                self.x+=self.restrightSpeed
                self.rect.x+=self.restrightSpeed
                self.image=self.right[self.frame%7]
            elif self.dir=="up":
                self.y-=self.restupSpeed
                self.rect.y-=self.restupSpeed
                self.image=self.up[self.frame%7]
            elif self.dir=="down":
                self.y+=self.restdownSpeed
                self.rect.y+=self.restdownSpeed
                self.image=self.down[self.frame%7]
        elif self.state=="angry":
            Neighbor.chase(self,player)

class PygameGame(object):
    def init(self):
        self.student=Student(self.width,self.height)
        self.neighbor=Neighbor(self.width,self.height)
        self.step=0
        self.frequency=40
        self.range=150
        self.maze = Maze()
        self.blockImg = pygame.image.load("block.png")
        self.blockImg=pygame.transform.scale(self.blockImg,(44,44))
        self.floorImg=pygame.image.load("floor.png")
        self.floorImg=pygame.transform.scale(self.floorImg,(44,44))
        self.maze.getMazeRect(self.blockImg)
        self.sounds=[]
        self.sounds.append(pygame.mixer.Sound("incoming.wav"))
        self.sounds.append(pygame.mixer.Sound("bgm.wav"))
        self.done=False
        
        self.door=Door(955,682)
        self.table1=BigTable(100,80)
        self.table2=SmallTable(850,90)
        self.tv=TV(280,20)
        self.sofa=Sofa(270,90)
        self.cupboard1=Cupboard(54,55)
        self.cupboard2=Cupboard(600,658)
        self.fridge1=Fridge(800,30)
        self.oven=Oven(847,46)
        self.oven2=Oven(1118,286)
        self.microwave=Microwave(1118,260)
        self.table3=SmallTable(1100,600)
        self.key=Key(1180,84)
        self.collected=0
        self.coin1=Coin(50,180)
        self.coin2=Coin(745,130)
        self.coin3=Coin(1010,270)
        self.coin4=Coin(880,670)
        self.coin5=Coin(50,390)
        self.fireplace=Fireplace(835,220)
        self.fireplace2=Fireplace(1074,660)
        self.torch1=Torch(100,self.height-70)
        self.torch2=Torch(250,self.height-70)
        self.torch3=Torch(400,self.height-70)
        self.torch4=Torch(550,self.height-70)
        self.shelf1=Shelf1(570,475)
        self.shelf2=Shelf2(200,380)
        self.torch5=Torch(250,360)
        self.torch6=Torch(405,440)
        self.torch7=Torch(430,220)
        self.torch8=Torch(625,220)
        self.torch9=Torch(480,220)
        self.torch10=Torch(680,220)
        self.torch11=Torch(800,270)
        self.torch12=Torch(880,270)
        
        self.scorecoin=Scorecoin(self.width-140,20)
        self.fog=pygame.Surface((self.width,self.height),pygame.SRCALPHA)
        self.fog.fill((0,0,0,255))
        self.font=pygame.font.SysFont("Five Nights at Freddy's",50)
        self.text=self.font.render("x "+str(self.collected),False,(255,255,255))
        self.path=copy.deepcopy(self.maze.maze)
        self.timeToGetOut=False
    
    #fog of war idea from https://www.reddit.com/r/pygame/comments/4u8iht/challenge_fog_of_war/
    def renderFog(self):
        self.fog.fill((0,0,0,255))
        m=255/float(100)
        for i in range(100,1,-1):
            pygame.draw.circle(self.fog,(0,0,0,i*m)\
                    ,(self.student.x,self.student.y),i)

    def mousePressed(self, x, y):
        print(x,y)

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass
    
    def distance(x1,y1,x2,y2):
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
    
    def timerFired(self, dt):
        self.step+=1
        self.frequency=random.randint(30,50)
        self.distance=PygameGame.distance(self.student.x,self.student.y,\
                                self.neighbor.x,self.neighbor.y)
        if self.distance<=self.range:
            self.sounds[1].stop()
            self.sounds[0].play()
            self.neighbor.state="angry"
        else:
            self.sounds[0].fadeout(2000)
            self.neighbor.state="rest" 
            self.sounds[1].play()
        
        if self.step%self.frequency==0:
            self.neighbor.dir=random.choice(self.neighbor.direction)
        
        for wall in self.maze.walls:
            if self.student.rect.colliderect(wall):
                if self.student.dir=="up":
                    self.student.rect.top=wall.bottom
                    self.student.y=self.student.rect.y
                elif self.student.dir=="down":
                    self.student.rect.bottom=wall.top
                    self.student.y=self.student.rect.y
                elif self.student.dir=="left":
                    self.student.rect.left=wall.right
                    self.student.x=self.student.rect.x
                elif self.student.dir=="right":
                    self.student.rect.right=wall.left
                    self.student.x=self.student.rect.x
            if self.neighbor.rect.colliderect(wall):
                if self.neighbor.dir=="up":
                    self.neighbor.dir="right"
                elif self.neighbor.dir=="down":
                    self.neighbor.dir="left"
                elif self.neighbor.dir=="left":
                    self.neighbor.dir="up"
                elif self.neighbor.dir=="right":
                    self.neighbor.dir="down"
        
        try:
            if self.student.rect.colliderect(self.coin1.rect):
                self.collected+=1
                del self.coin1
        except:
            pass
        try:
            if self.student.rect.colliderect(self.coin2.rect):
                self.collected+=1
                del self.coin2
        except:
            pass
        try:
            if self.student.rect.colliderect(self.coin3.rect):
                self.collected+=1
                del self.coin3
        except:
            pass
        try:
            if self.student.rect.colliderect(self.coin4.rect):
                self.collected+=1
                del self.coin4
        except:
            pass
        try:
            if self.student.rect.colliderect(self.coin5.rect):
                self.collected+=1
                del self.coin5
        except:
            pass
        try:
            if self.student.rect.colliderect(self.key):
                self.timeToGetOut=True
                del self.key
        except:
            pass
                
        self.neighbor.update(self.student)
        self.student.update(self.isKeyPressed)
        try:
            self.coin1.update()
        except:
            pass
        try:
            self.coin2.update()
        except:
            pass
        try:
            self.coin3.update()
        except:
            pass
        try:
            self.coin4.update()
        except:
            pass
        try:
            self.coin5.update()
        except:
            pass
        self.torch1.update()
        self.torch2.update()
        self.torch3.update()
        self.torch4.update()
        self.torch5.update()
        self.torch6.update()
        self.torch7.update()
        self.torch8.update()
        self.torch9.update()
        self.torch10.update()
        self.torch11.update()
        self.torch12.update()
        if self.student.rect.colliderect(self.door.rect):
            if self.timeToGetOut==True:
                self.done=True
        if self.student.rect.colliderect(self.neighbor.rect):
            self.student.x=0
            self.student.y=self.height-100
            self.student.rect.x=self.student.x
            self.student.rect.y=self.student.y

    def redrawAll(self, screen):
        self.maze.draw(screen, self.blockImg,self.floorImg)
        self.table1.draw(screen)
        self.table2.draw(screen)
        self.tv.draw(screen)
        self.sofa.draw(screen)
        self.cupboard1.draw(screen)
        self.cupboard2.draw(screen)
        self.fridge1.draw(screen)
        self.oven.draw(screen)
        self.oven2.draw(screen)
        self.microwave.draw(screen)
        self.table3.draw(screen)
        self.shelf1.draw(screen)
        self.shelf2.draw(screen)
        self.neighbor.draw(screen)
        self.student.draw(screen)
        self.door.draw(screen)
        self.fireplace2.draw(screen)
        self.torch5.draw(screen)
        self.torch6.draw(screen)
        self.torch7.draw(screen)
        self.torch8.draw(screen)
        self.torch9.draw(screen)
        self.torch10.draw(screen)
        self.torch11.draw(screen)
        self.torch12.draw(screen)
        
        try:
            self.coin1.draw(screen)
        except:
            pass
        try:
            self.coin2.draw(screen)
        except:
            pass
        try:
            self.coin3.draw(screen)
        except:
            pass
        try:
            self.coin4.draw(screen)
        except:
            pass
        try:
            self.coin5.draw(screen)
        except:
            pass
        self.fireplace.draw(screen)
        self.torch1.draw(screen)
        self.torch2.draw(screen)
        self.torch3.draw(screen)
        self.torch4.draw(screen)
        try:
            if self.collected==5:
                self.key.draw(screen)
        except:
            pass
        self.renderFog()
        screen.blit(self.fog,(0,0))
        self.scorecoin.draw(screen)
        self.font=pygame.font.SysFont("Five Nights at Freddy's",50)
        self.text=self.font.render("x "+str(self.collected),False,(255,255,255))
        screen.blit(self.text,(self.width-75,35))


    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=1275, height=745, fps=120, title="Escaping the Dungeons of 112"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            if self.done==True:
                playing=False
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()
        sys.exit()

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()