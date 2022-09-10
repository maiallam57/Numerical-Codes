import numpy as np
import sys

coeff_of_eq1, coeff_of_eq2, coeff_of_eq3 = [], [], []
augmented_matrix = [coeff_of_eq1, coeff_of_eq2, coeff_of_eq3]
x = np.zeros(3)

def print_augmented_matrix():
    for i in range(0, 3):
        for j in range(0, 4):
            print('%0.2f' % (augmented_matrix[i][j]), end="\t")
            if j == 2:
                print("|", end=" ")
        print()

def getData():
    try:
        for i in range(3):
            coeff1 = float(input("please enter the coeff. of x1: "))
            coeff2 = float(input("please enter the coeff. of x2: "))
            coeff3 = float(input("please enter the coeff. of x3: "))
            free_term = float(input("please enter the free term of eq " + str(i+1) + ": "))
            if i == 0:
                coeff_of_eq1.append(coeff1)
                coeff_of_eq1.append(coeff2)
                coeff_of_eq1.append(coeff3)
                coeff_of_eq1.append(free_term)

            elif i == 1:
                coeff_of_eq2.append(coeff1)
                coeff_of_eq2.append(coeff2)
                coeff_of_eq2.append(coeff3)
                coeff_of_eq2.append(free_term)

            elif i == 2:
                coeff_of_eq3.append(coeff1)
                coeff_of_eq3.append(coeff2)
                coeff_of_eq3.append(coeff3)
                coeff_of_eq3.append(free_term)

        print('\naugmented matrix: ')
        print_augmented_matrix()

    except:
        print("Invalid Input!, Please Try Again..\n")
        getData()

def get_upper_matrix():
    for i in range(3):
        if augmented_matrix[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        for j in range(i + 1, 3):
            ratio = augmented_matrix[j][i] / augmented_matrix[i][i]
            for k in range(4):
                augmented_matrix[j][k] = augmented_matrix[j][k] - ratio * augmented_matrix[i][k]

    print('\naugmented matrix after gauss elimination: ')
    print_augmented_matrix()

def back_Substitution():
    x[2] = augmented_matrix[2][3]/augmented_matrix[2][2]
    x[1] = (augmented_matrix[1][3] - (augmented_matrix[1][2] * x[2])) / augmented_matrix[1][1]
    x[0] = (augmented_matrix[0][3] - (augmented_matrix[0][2] * x[2]) - (augmented_matrix[0][1] * x[1])) / augmented_matrix[0][0]

    # Displaying solution
    print('\nRequired solution is: ')
    for i in range(3):
        print('X%d = %0.2f' % (i+1, x[i]))

getData()
get_upper_matrix()
back_Substitution()