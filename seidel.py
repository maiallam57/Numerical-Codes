x_old, points = [0, 0, 0], [0, 0, 0]
free_terms = []
i = 0


def seidel(coeff, free_terms, points):
    for j in range(0, 3):
        temp = free_terms[j]      # temp to store free_terms[j]

        for i in range(0, 3):     # to calculate xi, yi, zi
            if (j != i):
                temp -= coeff[j][i] * points[i]

        points[j] = temp / coeff[j][j]      # updating the solution

    return points


x1 = float(input("please enter the coeff. of x1: "))
y1 = float(input("please enter the coeff. of x2: "))
z1 = float(input("please enter the coeff. of x3: "))
b = float(input("please enter the free term of eq1: "))
free_terms.append(b)
x2 = float(input("please enter the coeff. of x1: "))
y2 = float(input("please enter the coeff. of x2: "))
z2 = float(input("please enter the coeff. of x3: "))
b = float(input("please enter the free term of eq2: "))
free_terms.append(b)
x3 = float(input("please enter the coeff. of x1: "))
y3 = float(input("please enter the coeff. of x2: "))
z3 = float(input("please enter the coeff. of x3: "))
b = float(input("please enter the free term of eq3: "))
free_terms.append(b)
e = float(input('Enter tolerable error: '))

coeff = [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]]
print(points)



# loop run for m times depending on m the error value
while True:
    points = seidel(coeff, free_terms, points)

    e1 = abs(points[0] - x_old[0])
    print("e1= ", e1)
    e2 = abs(points[1] - x_old[1])
    print("e2= ", e2)
    e3 = abs(points[2] - x_old[2])
    print("e3= ", e3)
    print()

    x_old = seidel(coeff, free_terms, x_old)

    i += 1

    if e1 == e or e2 == e or e3 == e or e1 == 0 or e2 == 0 or e3 == 0:
        break

    # print each time the updated solution
    print("i= ", i)
    print("x1, x2, x3 = ", points)
    print()