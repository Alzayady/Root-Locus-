import math

import matplotlib.pyplot as plot
from sympy import symbols, solve
from sympy.parsing.sympy_parser import standard_transformations, implicit_application, parse_expr


def draw(poles, centroid):
    fig = plot.gcf()
    fig.set_size_inches(10.5, 10.5)
    fig.savefig('test2png.png', dpi=100)

    drowLineBlack([0, -40], [0, 40])
    drowLineBlack([-100, 0], [50, 0])


    x = []
    y = []
    for i in poles:
        x.append(i.real)
        y.append(i.imag)
        plot.scatter(i.real, i.imag, s=45, marker='o', color="red")
    pass


def drowLineBlack(point1, point2):
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plot.plot(x_values, y_values, color="black", lw=.5)
def drawAssemtotic(centroid):
    drowLineDashed([-50 + centroid, 50], [50 + centroid, -50])
    drowLineDashed([-50 + centroid, -50], [50 + centroid, 50])


def drowLineDashed(point1, point2):
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plot.plot(x_values, y_values, ls='--', color='lightblue', lw=.7)


def drowPoint(point):
    plot.scatter(point[0], point[1], s=30, marker='o', color="green")

def drowPoint2(point):
    plot.scatter(point[0], point[1], s=20, marker='+', color="blue")


def drawRightCurve():
    lastP1 = None
    lastP2 = None
    begin = -9.15039
    while begin <= 0:
        y = getPoint(begin)
        p1 = [begin, y]
        p2 = [begin, -y]
        drawDeltaCurve(lastP1, p1)
        drawDeltaCurve(lastP2, p2)
        begin += .01
        lastP1 = p1
        lastP2 = p2
    completeCurve()
    pass


def getPoint(x):
    return math.sqrt((x + 9.15039) / .01759760213)


def drawDeltaCurve(point1, point2):
    if point1 == None:
        return
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plot.plot(x_values, y_values, color="black", lw=.5)


def completeCurve():
    point1 = [0, 22.803]
    point2 = [50, 80.803]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plot.plot(x_values, y_values, color="black", lw=.8)

    point1 = [0, -22.803]
    point2 = [50, -72.803]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1] - 8]
    plot.plot(x_values, y_values, color="black", lw=.8)


def drawRealAxis():
    point1 = [0, 0]
    point2 = [-25, 0]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plot.plot(x_values, y_values, color="black", lw=1.5)


def getPoint2(x):
    return math.sqrt((x + 47.5) / (-.0285))
    pass


def completeCurve2():
    point1 = [-58, 19.388542155125376]
    point2 = [point1[0] - 50, point1[1] + 50]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1] + 6]

    plot.plot(x_values, y_values, color="black", lw=1)

    point1 = [-58, -19.388542155125376]
    point2 = [point1[0] - 50, point1[1] - 50]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1] - 6]
    plot.plot(x_values, y_values, color="black", lw=1)


def drawLeftCurve():
    lastP1 = None
    lastP2 = None
    begin = -50
    while begin >= -58:
        y = getPoint2(begin)
        p1 = [begin, y]
        p2 = [begin, -y]
        drawDeltaCurve(lastP1, p1)
        drawDeltaCurve(lastP2, p2)
        begin -= .01
        lastP1 = p1
        lastP2 = p2
    completeCurve2()


def drawRoot(num):
    num = complex(num)
    color = "red"
    if num.real > -9 and num.imag > 0:
        color = "yellow"
    elif num.real > -9:
        color = "brown"
    elif num.imag > 0:
        color = "blue"

    if abs(num.imag)<1:
        if num.real<-9:
            color="brown"
        else:
            color="yellow"

    plot.scatter(num.real, num.imag, s=50, marker='.', color=color)
    pass


def drawRoots(equ):
    s = symbols('s')
    f=eval(equ)
    ans = solve(f, s)
    for i in ans:
        num = i.evalf()
        drawRoot(num)



def drawExactPoint():

    equ = "s**4+125*s**3+5100*s**2+65000*s"
    for i in range(0, 4000000, 50000):
        equ = equ + "+" + str(i)
        drawRoots(equ)
