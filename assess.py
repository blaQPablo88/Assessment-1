import random

def grade_average(grades):
    """ Write a program that returns the average number of a given list of grades.
    It should not add any negative grades to the average.

    Args:
        grades (list): List of grades to calculate
    """
    average = 0
    new_grades = []
    for grade in grades:
        if grade >= 1:
            new_grades.append(grade)
        average = sum(new_grades) // len(new_grades)
    return average


def find_prime_factors(number):
    """Write code to return the prime factors of the number. 

    Args:
        number (int): Number to find the prime factors of
    """
    prime_list = []
    for num in range(1, number + 1):
        for x in range(1, num + 1):
            if number % x == 0:
                prime_list.append(x)
    return prime_list
print(find_prime_factors(4))

def calculate_interest(principal, rate, years):
    """Write a program that returns the compound interest

    Args:
        principal (int): The principal amount
        rate (int): The interest rate
        years (int): The amount of years to calculate the interest for
    """
    amount = 0
    for n in range(1, years + 1):
        amount += principal * (rate / 100)


def code_word(code):
    """Write a program that returns the word given a code.

    e.g. Given code: [3,1,20]
    Expected Word: "cat"

    Args:
        code (list): The code to decipher
    """

    new_code = ''
    alpha_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26
    }

    for char in code:
        for key, value in alpha_dict.items():
            if char == value:
                new_code += key
    return new_code
print(code_word([9, 0, 3, 1, 14, 0, 4, 15, 0, 9, 20]))


def triangles(length):
    """Write a program that returns a triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    ***
    ****
    *****

    Args:
        length (int): The length your triangle should be
    """
    new_list = []
    for _ in range(1, length + 1):
        # print('*' * _)
        new_list.append('*' * _)
    return new_list


def hollow_triangle(length):
    """Write a program that returns a hollow triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    * *
    *  *
    *****

    Args:
        length (int): The ;ength your triangle should be
    """
    
    new_list = []
    triangles = ''
    for _ in range(1, length + 1):
        # print('*' * _)
        # if _ == 3:
        #     triangles += ('* *')

        # elif _ == length:
        #     triangles += ('*')

        triangles += ('*' * _)
        new_list.append(triangles)
        print(new_list)
    return new_list

    # triangles = ''
    # for _ in range(1, length + 1):

    #     # triangles += ('*' * _)
    #     print('*' * _)
    # return triangles

print(hollow_triangle(5))


# There are no tests for this function so test by running the program. 
def number_guessing(number):
    """Write a guessing game. The player has 10 opprtunites to guess.

    e.g. Number: 4
         User Input: 5
         Output: Incorrect

         Number: 4
         User Input: 4
         Output: Correct

    Args:
        number (int): The number to be guessed
    """

    # rand_num = random.randint(1, 10)
    # print(rand_num)
    # user_input = input('guess a number(1-10): ')
    # if user_input == rand_num:
    #     print('Correct')
    # else:
    #     print('Incorrect')


    user_input = input('guess a number(1-10): ')
    if number == user_input:
        print('Correct')
    else:
        print('Inorrect')

