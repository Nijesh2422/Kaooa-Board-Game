from turtle import *
import math
import time
linelength = 1000
radius = 100
turn = 0
total_crows = 7
placed_crows = 0
vulture_placed = 0
vulture_co_ords = []
prev_clicked_crow = []
movement_flag = 0
first = 0
#Cyan = Crow Gold = Vulture
#Occupancy = 0 = None , 1 = Vulture , 2 = Crow 

class Point:
    def __init__(self,co_ords,i) -> None:
        self.x_co = co_ords[0]
        self.y_co = co_ords[1]
        self.index = i
        self.occupancy = 0
    def clocks(self,turt):
        global turn
        global vulture_placed
        global vulture_co_ords
        global placed_crows
        if self.occupancy == 0 : 
            if turn%2 ==  1 and vulture_placed == 0: #vulture's turn
                turt.up()
                turt.goto(self.x_co,self.y_co)
                turt.down()
                turt.dot(100,"gold")
                self.occupancy = 1
                vulture_placed = 1
                vulture_co_ords.append(self)
            elif turn%2 == 0 : #crow's turn
                turt.up()
                turt.goto(self.x_co,self.y_co)
                turt.down()
                turt.dot(100,"turquoise")
                self.occupancy = 2
                placed_crows += 1
            turn += 1

    def vulture_movement(self,points_list,turt,flag):
        global turn
        global adjacents_list
        global jump_list
        global vulture_co_ords
        global total_crows
        global placed_crows
        if flag == 0:
            for points in adjacents_list[vulture_co_ords[0].index]:
                if points_list[points].x_co == self.x_co and points_list[points].y_co == self.y_co and self.occupancy == 0:
                    turt.up()
                    turt.goto(vulture_co_ords[0].x_co,vulture_co_ords[0].y_co)
                    turt.down()
                    turt.dot(100,"white")
                    turt.up()
                    turt.goto(self.x_co,self.y_co)
                    turt.down()
                    turt.dot(100,"gold")
                    self.occupancy = 1
                    points_list[vulture_co_ords[0].index].occupancy = 0
                    vulture_co_ords.pop(0)
                    vulture_co_ords.append(self)
                    turn += 1
                    return
        else:
            for points in jump_list[vulture_co_ords[0].index]:
                if points_list[points[1]].x_co == self.x_co and points_list[points[1]].y_co == self.y_co and self.occupancy == 0:
                    if points_list[points[0]].occupancy == 2 : 
                        turt.up()
                        turt.goto(vulture_co_ords[0].x_co,vulture_co_ords[0].y_co)
                        turt.down()
                        turt.dot(100,"white")
                        turt.up()
                        turt.goto(self.x_co,self.y_co)
                        turt.down()
                        turt.dot(100,"gold")
                        self.occupancy = 1
                        points_list[vulture_co_ords[0].index].occupancy = 0
                        vulture_co_ords.pop(0)
                        vulture_co_ords.append(self)
                        turn += 1
                        turt.up()
                        turt.goto(points_list[points[0]].x_co,points_list[points[0]].y_co)
                        turt.down()
                        turt.dot(100,"white")
                        points_list[points[0]].occupancy = 0
                        total_crows -= 1
                        placed_crows -= 1
                        return
        
    def crows_movement(self,points_list,turt):
        global turn
        global adjacents_list
        global prev_clicked_crow,movement_flag
        if self.occupancy == 2:
            prev_clicked_crow.append(self)
            movement_flag = 1
        elif movement_flag == 1 and self.occupancy != 1:
            movement_flag = 0
            for points in adjacents_list[prev_clicked_crow[-1].index]:
                if points_list[points].x_co == self.x_co and points_list[points].y_co == self.y_co and self.occupancy == 0:
                    turt.up()
                    turt.goto(prev_clicked_crow[-1].x_co,prev_clicked_crow[-1].y_co)
                    turt.down()
                    turt.dot(100,"white")
                    turt.up()
                    turt.goto(self.x_co,self.y_co)
                    turt.down()
                    turt.dot(100,"turquoise")
                    self.occupancy = 2
                    points_list[prev_clicked_crow[-1].index].occupancy = 0
                    prev_clicked_crow.clear()
                    turn += 1

def intersection_point(tup1,tup2,tup3,tup4):
    m1 = (tup2[1] - tup1[1]) / (tup2[0] - tup1[0])
    m2 = (tup4[1] - tup3[1]) / (tup4[0] - tup3[0])

    x = ((m1 * tup1[0] - tup1[1]) - (m2 * tup3[0] - tup3[1])) / (m1 - m2)
    y = m1 * (x - tup1[0]) + tup1[1]

    return x, y

def hahahhehe(x,y):
    pass

def clicks(x,y,points_list,turt):
    global turn,vulture_placed,placed_crows,total_crows,first
    for i in range(len(points_list)):
        distance = ((points_list[i].x_co - x)**2 + (points_list[i].y_co - y)**2)**0.5
        if distance <= radius:
            if turn%2 == 1 and vulture_placed == 1:
                flag = 0
                for points in jump_list[vulture_co_ords[0].index]:
                    if points_list[points[1]].occupancy == 0 and points_list[points[0]].occupancy == 2 :
                        flag += 1 
                points_list[i].vulture_movement(points_list,turt,flag) #Vulture movement
            elif turn%2 == 0 and placed_crows == total_crows:
                points_list[i].crows_movement(points_list,turt) #Crows Movement
            else:
                points_list[i].clocks(turt) #Crows and Vulture Placement
    
    if total_crows == 3 :
        turt.up()
        turt.goto(0,0)
        turt.down()
        turt.color("black")
        turt.write("VULTURE WINSSS!! RAHHHHHH!!!!!", align="center", font=("Montserrat", 24, "bold"))
        turt.onclick(hahahhehe)
        time.sleep(3)
        turt.screen.bye()        
        return

    flag = 0
    if first != 0 :
        for points in adjacents_list[vulture_co_ords[0].index]:
                if points_list[points].occupancy == 0:
                    flag += 1
        for points in jump_list[vulture_co_ords[0].index]:
            if points_list[points[0]].occupancy == 2  and points_list[points[1]].occupancy == 0:
                flag += 1 
        if flag == 0:
            turt.up()
            turt.goto(0,0)
            turt.down()
            turt.color("black")
            turt.write("CROWS WINNN!!", align="center", font=("Montserrat", 24, "bold"))
            turt.onclick(hahahhehe)
            time.sleep(3)
            turt.screen.bye()
            return
    else:
        first += 1

    return



corners_list = []

angle_in_radians = math.radians(72)
sine_value = math.sin(angle_in_radians)
cosecant_value = 1 / sine_value

t = Turtle()
t.color("dim gray")
t.screen.bgcolor("orange")
t.hideturtle()
t.width(3)
t.speed(10)

t.up()
t.goto((-linelength/2,(linelength/4)*cosecant_value - 150))
corners_list.append((-linelength/2,(linelength/4)*cosecant_value - 150))
t.down()

for i in range(5):
    t.forward(linelength)
    t.right(144)
    corners_list.append(t.pos())

corners_list.pop(-1)

corners_list.append(intersection_point(corners_list[0],corners_list[1],corners_list[2],corners_list[3]))
corners_list.append(intersection_point(corners_list[0],corners_list[1],corners_list[3],corners_list[4]))
corners_list.append(intersection_point(corners_list[1],corners_list[2],corners_list[3],corners_list[4]))
corners_list.append(intersection_point(corners_list[0],corners_list[4],corners_list[1],corners_list[2]))
corners_list.append(intersection_point(corners_list[0],corners_list[4],corners_list[2],corners_list[3]))

points_list = []
for i in range(len(corners_list)):
    t.up()
    t.goto(corners_list[i])
    t.down()
    t.dot(106,"dim gray")
    t.dot(100,"white")
    points_list.append(Point(corners_list[i],i))

adjacents_list = []
adjacents_list.append([5,9])
adjacents_list.append([6,7])
adjacents_list.append([8,9])
adjacents_list.append([5,6])
adjacents_list.append([7,8])
adjacents_list.append([0,6,9,3])
adjacents_list.append([5,3,1,7])
adjacents_list.append([6,8,1,4])
adjacents_list.append([7,9,2,4])
adjacents_list.append([5,8,0,2])

jump_list = []
jump_list.append([(5,6),(9,8)])
jump_list.append([(6,5),(7,8)])
jump_list.append([(9,5),(8,7)])
jump_list.append([(5,9),(6,7)])
jump_list.append([(8,9),(7,6)])
jump_list.append([(9,2),(6,1)])
jump_list.append([(5,0),(7,4)])
jump_list.append([(8,2),(6,3)])
jump_list.append([(9,0),(7,1)])
jump_list.append([(5,3),(8,4)])

t.screen.onclick(lambda x, y: clicks(x, y, points_list,t))

t.screen.mainloop()
