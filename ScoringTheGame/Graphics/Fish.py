import pygame
import random


class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self).__init__()
        self.size = ""
        self.speed = ""
        self.position = ""
        self.image = ""
        self.list = []
        self.range = ""


Plankton_list = []
for i in range(1):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    Plankton_list.append([x, y])


leftShark_list = []
for i in range(3):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    leftShark_list.append([x, y])

rightPiranha_list = []
for i in range(5):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    rightPiranha_list.append([x, y])

leftPiranha_list = []
for i in range(5):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    leftPiranha_list.append([x, y])

rightShark_list = []
for i in range(3):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    rightShark_list.append([x, y])


class plankton(Fish):
    def __init__(self):
        super(plankton,self).__init__()
        #plankton = Fish()
        plankton.position = (random.randrange(0,1277), random.randrange(0, 717))
        #plankton.range = 1
        plankton.list = createFishList(1)
        plankton.image = pygame.image.load("Plankton.png")



#class rightPiranha(Fish):
#def __init__(self):
#super(rightPiranha,self).__init__()
rightPiranha = Fish()
rightPiranha.size = 10
rightPiranha.speed = 20
rightPiranha.image = pygame.image.load("rightPiranha.png")
rightPiranha.list = rightPiranha_list


#class leftShark(Fish):
#def __init__(self):
#super(leftShark, self).__init__()
leftShark = Fish()
leftShark.size = 15
leftShark.speed = 10
leftShark.image = pygame.image.load("leftShark.png")
leftShark.list = leftShark_list


#class leftPiranha(Fish):
#def __init__(self):
#super(leftPiranha, self).__init__()
leftPiranha = Fish()
leftPiranha.size = 5
leftPiranha.speed = 15
leftPiranha.image = pygame.image.load("leftPiranha.png")
#leftPiranha.range = 5
leftPiranha.list = leftPiranha_list

#class rightShark(Fish):
#def __init__(self):
#super(rightShark, self).__init__()
rightShark = Fish()
rightShark.size = 15
rightShark.speed = 5
rightShark.image = pygame.image.load("rightShark.png")
rightShark.position = (-10,random.randint(0,717))
rightShark.list = rightShark_list


