from sympy import *

x, y = [], []
XPower2, XPower3, XPower4 = [], [], []
XY, XPower2Y = [], []
choice = 'y'
n = 0
again = 1


def getData():
    try:
        point1 = float(input("Please Enter A Number On X-axis: "))
        x.append(point1)
        XPower2.append(point1 ** 2)
        XPower3.append(point1 ** 3)
        XPower4.append(point1 ** 4)
        point2 = float(input("Please Enter A Number On Y-axis: "))
        y.append(point2)
        XY.append(point1 * point2)
        XPower2Y.append((point1**2) * point2)
    except:
        print("Invalid Input!, Please Try Again..\n")
        getData()


def straightLine(n, sumOfX, sumOfY, sumOfXPower2, sumOfXY):
    a, b = symbols('a b')
    eq1 = Eq(n * a + sumOfX * b - sumOfY, 0)
    eq2 = Eq(sumOfX * a + sumOfXPower2 * b - sumOfXY, 0)
    answer = solve((eq1, eq2), (a, b))
    print(f'a = {answer[a]}')
    print(f'b = {answer[b]}')
    print(f"The Equation of Straight Line Is:    y= {answer[a]} + {answer[b]} x")


def parabola(n, sumOfX, sumOfY, sumOfXPower2, sumOfXY, sumOfXPower3, sumOfXPower4, sumOfXPower2Y):
    b0, b1, b2 = symbols('b0 b1 b2')
    eq1 = Eq(n * b0 + sumOfX * b1 + sumOfXPower2 * b2, sumOfY)
    eq2 = Eq(sumOfX * b0 + sumOfXPower2 * b1 + sumOfXPower3 * b2, sumOfXY)
    eq3 = Eq(sumOfXPower2 * b0 + sumOfXPower3 * b1 + sumOfXPower4 * b2, sumOfXPower2Y)
    answer = solve((eq1, eq2, eq3), (b0, b1, b2))
    print(f'b0 = {answer[b0]}\n')
    print(f'b1 = {answer[b1]}\n')
    print(f'b2 = {answer[b2]}\n')
    print(f"The Equation of Parabola Is:    y= {answer[b0]} +{ answer[b1]} x +{ answer[b2]} x^2")


def getChoice():
    return input("To Add Another Elements, Please Enter 'y' \nTo Exit,                 Please Enter 'n'\n").lower()


def getFittingChoice():
    fittingChoice = int(input("For Fitting The Data To\nStraight Line, Please Enter: 1\nParabola,      Please Enter: 2\n"))
    if fittingChoice == 1:
        straightLine(n, sumOfX, sumOfY, sumOfXPower2, sumOfXY)
    elif fittingChoice == 2:
        parabola(n, sumOfX, sumOfY, sumOfXPower2, sumOfXY, sumOfXPower3, sumOfXPower4, sumOfXPower2Y)
    else:
        print("Invalid Input!, Please Try Again..")
        getFittingChoice()


def getAgainChoice():
    try:
        again = int(input("\nTo Fit Another Data, Please Enter 1 \nTo Exit, Please Enter 2\n"))
        if again == 2:
            print("\nTHE END!\n")
    except:
        print("\nInvalid Input!, Please Try Again..")
        getAgainChoice()


while again == 1:
    print("\n\tWelcome To Least Square Data Fitting!\n")
    while True:
        getData()
        n += 1
        choice = getChoice().lower()
        if choice == 'y':
            getData()
            choice = getChoice().lower()
        elif choice == 'n':
            break
        elif choice != 'y' or choice != 'n':
            print("Invalid Input!, Please Try Again..\n")
            choice = getChoice().lower()

    sumOfX, sumOfY = sum(x), sum(y)
    sumOfXPower2, sumOfXPower3, sumOfXPower4 = sum(XPower2), sum(XPower3), sum(XPower4)
    sumOfXY = sum(XY)
    sumOfXPower2Y = sum(XPower2Y)

    getFittingChoice()
    getAgainChoice()