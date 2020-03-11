from p5 import *
import vehicle as vh
import random as rd

vList = []
vFood = []


def setup():
    size(1280, 720)
    #vList.append(vh.Vehicle(width / 3, height/3))
    vList.append(vh.Vehicle(width / 2, height/2))

    for i in range(10):
        x = rd.randrange(width)
        y = rd.randrange(height)
        vFood.append(Vector(x, y))


def draw():
    background(51)

    # Demonstração visual dos foods na tela
    for obj in vFood:
        fill(0, 255, 0)
        no_stroke()
        ellipse((obj.x, obj.y), 8, 8)

    # Demonstração visual dos vehicles na tela
    for i in range(len(vList)):
        #print("cheguei for")
        print(i, " : ", vList[i].position)

        #vList[i].seek(Vector(mouse_x, mouse_y))

        vList[i].eat(vFood)
        vList[i].update()
        vList[i].display()


# def key_pressed(event):
run()
