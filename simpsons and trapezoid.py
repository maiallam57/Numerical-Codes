x, fx = [], []
again=1

def getData():
    try:
        global equation
        equation = input("please enter the equation: ").lower()
        global start_point
        start_point = float(input("please enter the start point: "))
        global end_point
        end_point = float(input("please enter the end point: "))
        global n
        n = int(input("please enter the no of points: "))

    except:
        print("Invalid Input!, Please Try Again..\n")
        getData()

def getX(start, n, step):
    x.append(start)
    for i in range(0, n-1):
        start += step
        x.append(start)

def getFx(equation, x, n):
    for i in range(0, n):
        fpoint = eval(str(equation), {'x':x[i]})
        fx.append(fpoint)

def trap_eq(h):
    I_trap = (h / 2) * (fx[0] + 2 * sum(fx[1:n - 1]) + fx[n - 1])
    print("I= ", I_trap)

def simpson_one_third_rule(h):
    I_3simp = (h / 3) * (fx[0] + 2 * sum(fx[0:n - 2:2]) + 4 * sum(fx[1:n - 1:2]) + fx[n - 1])
    print("I= ", I_3simp)

def simpson_three_eight_rule(h):
    I_3_8simp = (3* h / 8) * (fx[0] + 3 * sum(fx[1:n - 1]) + fx[n - 1])
    print("I= ", I_3_8simp)

def get_integrated_Choice(h):
    CalcChoice = int(input("For calculating The Data by\nTrapezoidal Rule, Please Enter: 1\nsimpson's Rule,   Please Enter: 2\n"))
    if CalcChoice == 1:
        trap_eq(h)
    elif CalcChoice == 2:
        if n >= 3 and n % 2 != 0:
            simpson_one_third_rule(h)
        elif n == 4:
            simpson_three_eight_rule(h)
        else:
            print("simpson is not allowed in case of n=", n)
            print("By Trapezoidal Rule", end=' ')
            trap_eq(h)
    else:
        print("Invalid Input!, Please Try Again..")
        get_integrated_Choice(h)

def getAgainChoice():
    try:
        again = int(input("\nTo Fit Another Data, Please Enter 1 \nTo Exit, Please Enter 2\n"))
        if again == 2:
            print("\nTHE END!\n")
        return again
    except:
        print("\nInvalid Input!, Please Try Again..")
        getAgainChoice()

while again == 1:
    print("\n\tWelcome To Numerical Integration!\n")
    getData()
    h = (end_point - start_point) / (n - 1)
    getX(start_point, n, h)
    getFx(equation, x, n)
    get_integrated_Choice(h)
    again = getAgainChoice()