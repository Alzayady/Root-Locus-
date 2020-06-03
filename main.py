import math
from tkinter import *

import draw
from sympy import *
import matplotlib.pyplot as plot


def BreakAwayPoint(text, equ):
    text.insert(INSERT, "\n\n\n   Finding break away point")

    s = symbols('s')
    expr_diff = diff(equ, s)
    rootsdirv = solve(expr_diff, s)

    text.insert(INSERT, "\n\n    k=-(" + equ + ")")

    text.insert(INSERT, "\n    dk/ds=-(" + str(expr_diff) + ")")

    text.insert(INSERT, "\n    roots of derivative are :  \n")

    for i in rootsdirv:
        c = complex(expand(i).evalf()).real
        text2.insert(INSERT, "\n   " + str(c))

    breakAway = complex(expand(rootsdirv[2]).evalf()).real
    text.insert(INSERT, "\n\n   the only valid one is " + str(breakAway))
    draw.drowPoint([breakAway, 0])


def FindCentroidAndAngels(poles):
    centroid = 0
    for i in poles:
        centroid += i
    centroid /= len(poles)
    centroid = centroid.real

    su = str(sum(poles).real)
    text2.insert(INSERT, "\n\n   centroid = " + su + " / " + str(len(poles)) + "=  " + str(centroid))
    text2.insert(INSERT, "\n   asymptotic angels :\n")
    for i in range(0, len(poles) + 1):
        num = 180 * (2 * i + 1) / len(poles)
        text2.insert(INSERT, "          +" + str(num) + "  , -" + str(num) + "\n")
    angels = [45, -45]
    text2.insert(INSERT, "\n   it can be simplified to [45 , -45]")
    return centroid


def findIntersection(text):
    k = 4580 * 65000 / 125
    equ = "4580*s**2+" + str(k)
    s = symbols('s')
    ans = solve(equ, s)
    text.insert(INSERT, "\n\n   Intersection with imaginary axis are \n\n       " + str(ans))
    draw.drowPoint2([0, (complex(ans[0])).imag])
    draw.drowPoint2([0, (complex(ans[1])).imag])
    return ans


def getAngle(point1, point2):
    vec = [point2.real - point1.real, point2.imag - point1.imag]
    ans = (atan(abs(vec[1] / (vec[0] + .000000000000000001))) * 180 / math.pi)
    return 180 - ans
    pass


def findDeptureAngle(text2, poles):
    angle = 180 - (getAngle(poles[0], poles[2]) + getAngle(poles[1], poles[2]) + getAngle(poles[3], poles[2])) + 360

    text2.insert(INSERT, "\n\n   Departure angles for poles " + str(poles[2]) + " is " + str(angle))
    text2.insert(INSERT, "\n   Departure angles for poles " + str(poles[3]) + " is -" + str(angle))

    pass



root = Tk()
root.title("Root Locus")
text1 = Text(root, height=10, width=75)
text1.insert(INSERT, "\n\n    Given the following open loop transfer function with four poles at\n    S = 0 ,"
                     "\n    S = -25 \n    S= -50 + j 10 "
                     "\n    S = -50 – j 10\n    and no zeroes Draw it's Root Locus.")

equ = "s**4+125*s**3+5100*s**2+65000*s"

text2 = Text(root, height=50, width=75)
text2.insert(INSERT, " \n    Answer: ")
text2.tag_add("start", "2.2", "2.13")
text2.tag_config("start", foreground="red")

poles = [0, -25, -50 + 10j, -50 - 10j]

centroid = FindCentroidAndAngels(poles)




findDeptureAngle(text2, poles)
draw.drawRealAxis()
draw.drawRightCurve()
draw.drawLeftCurve()
text1.pack()
text2.pack()
draw.draw(poles, centroid)
draw.drawAssemtotic( centroid)
BreakAwayPoint(text2, equ)
intersection = findIntersection(text2)

draw.drawExactPoint()

plot.show()
root.mainloop()
