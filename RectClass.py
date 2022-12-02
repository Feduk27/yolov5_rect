import pygame
from random import randint
import math

#configuration
screensize = (640, 480)
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(screensize)


class rectangle(pygame.sprite.Sprite):
    def __init__(self, screensize):
        self.fig_color = list(map(lambda x: randint(0, 125), (0, 0, 0)))
        self.side_x = randint(150, 250)
        self.side_y = randint(150, 250)
        self.angle = randint(0, 89)
        limit = round(math.sqrt((self.side_x**2 + self.side_y**2)))
        self.xtopleft = randint(0, screensize[0] - limit)
        self.ytopleft = randint(0, screensize[1] - limit)

        self.image = pygame.Surface((self.side_x, self.side_y))
        self.image.set_colorkey((0, 0, 0))
        self.image.fill(self.fig_color)
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(topleft = (self.xtopleft, self.ytopleft))
    def output(self, i):
        size_rect = list(self.rect)
        x, y, w, h = size_rect
        sin = math.sin(self.angle/180*math.pi)
        cos = math.cos(self.angle/180*math.pi)
        print('Описывающий прямоугольник:',
              'x =',x,
              'y =',y,
              'w =',w,
              'h =',h,
              )
        x1 = x
        y1 = y + round(self.side_x*sin)
        x2 = x + round(self.side_x*cos)
        y2 = y
        x3 = x+w
        y3 = y+round(self.side_y*cos)
        x4 = x + round(self.side_y*sin)
        y4 = y + h

        print('Коорднаты углов:\n x1 =', x1, 'y1=', y1, '\n',
              'x2 =', x2, 'y2 =', y2, '\n',
              'x3 =', x3, 'y3 =', y3, '\n',
              'x4 =', x4, 'y4 =', y4
              )
#saving coordinates file in certain directory
        f_test1 = open('/Users/admin/PycharmProjects/Rect/labels/' + str(i)+'.txt', 'w+')
        f_test1.write('0 '+ str((x+w/2)/640)+' '+str((y+h/2)/480)+' '+str(w/640)+' '+str(h/480))
        f_test1.close()
        f_test2 = open('/Users/admin/PycharmProjects/Rect/CornerLabels/'+str(i)+'.txt', 'w+')
        f_test2.write(str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(x3) + ' ' + str(y3) + ' ' + str(x4) + ' ' + str(y4))
        f_test2.close()

for i in range(1000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
#creating random screen color
    sc_color = list(map(lambda x: randint(125, 255), (0, 0, 0)))
#initialisation of rectangle
    Rect1 = rectangle(screensize)
    Rect1.output(i)
#visualisation
    screen.fill(sc_color)
    screen.blit(Rect1.image, Rect1.rect)


# saving images for dataset
    pygame.image.save(screen, '/Users/admin/PycharmProjects/Rect/images/'+str(i)+'.png')
    pygame.display.update()
#setting 100 frames pe second
    clock.tick(100)

