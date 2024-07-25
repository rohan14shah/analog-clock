from graphics import *
from math import *
import datetime
from time import *


def main():
    win = GraphWin('The Spcs Clock' , 500 ,500, autoflush = False)
    win.setCoords(-250,-250, 250 , 250)
    win.setBackground('white')
    setupClockFace(win)


    rad = 0
    oldx = 0
    oldz = 0
    oldy = 0
    z = 0
    x = 0
    y = 0
    while not win.checkMouse():
        now = datetime.datetime.now()
        oldz = z
        z = now.second
        if oldz != z:
            oldsec_rad = (pi/30) * oldz
            removeShand = myhands(win , 0 , 0,  150 * sin(oldsec_rad)  , 150* cos(oldsec_rad), 'black' , 5)
            oldz = z
            
        sec_rad = (pi/30) * z
        seconds_hand = myhands(win , 0 , 0, 150 * sin(sec_rad), 150 * cos(sec_rad), 'purple' , 1)

       
            
        oldx = x
        x = now.minute
        if oldx != x:
            oldmin_rad = (pi/30) * oldx
            removehand = myhands(win , 0 , 0,  145 * sin(oldmin_rad)  , 145* cos(oldmin_rad), 'black' , 6)
            oldx = x
            
        min_rad = (pi/30) * x
        minute_hand = myhands(win , 0 , 0,  145 * sin(min_rad)  , 145* cos(min_rad), 'blue' , 2)

        oldy = y
        y = now.hour
        if oldy != y:
            oldhr_rad = (pi/30) * oldy * 5
            removehhand = myhands(win , 0 , 0, 70 * sin(oldhr_rad), 70* cos(oldhr_rad), 'black' , 7)
            oldy = y
        hr_rad =  (pi/30) * y * 5
        hour_hand = myhands(win , 0 , 0, 70 * sin(hr_rad), 70* cos(hr_rad), 'red' , 3)
        sleep(1)
        
 
def setupClockFace(win):
    
    circle = Circle(Point(0 ,0), 200)
    circle.setFill("black")
    circle.draw(win)
    centerDot = Circle(Point(0,0) , 7)
    centerDot.setFill('black')
    centerDot.draw(win)
    rad = 0
    q = ['12','1', '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9', '10' ,'11']
    num = 0
    for i in range(60):
        if ((i % 5) == 0 ):
            line = Line(Point(180 * sin(rad) ,180 * cos(rad)) , Point(200 * sin(rad) ,200 * cos(rad)))
            myT = Text(Point(173 * sin(rad) ,173 * cos(rad)), q[num])
            myT.setOutline('white')
            myT.draw(win)
            if num < 11:
                num = num + 1
        else:
            line = Line(Point(190 * sin(rad) ,190 * cos(rad)) , Point(200 * sin(rad) ,200 * cos(rad)))

        line.setOutline('white')
        line.draw(win)    
        rad = rad + 2 *pi/60
                  
def myhands(win, xval1, yval1 , xval2 , yval2, hcolor,  hwidth):
    my_hand = Line(Point(xval1, yval1), Point(xval2,yval2))
    my_hand.setOutline(hcolor)
    my_hand.setWidth(hwidth)
    my_hand.setArrow("last")
    my_hand.draw(win)

    return my_hand

  

main()





    
    

                 

                

