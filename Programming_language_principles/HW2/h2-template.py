# ------------------------------------------------
#   Q3(Higher-Order Functions, Lambda Functions)
# ------------------------------------------------
x, y = 2, 3
def f( ):
    def g( x ):
        return x + y
    return g( 1 ) * x
def k( x, y, fn ):
    return fn( ) * x - y
#print( k( 3, 2, f ) )

print((lambda x, y, fn: fn() * x - y)(3,2,lambda: (lambda x: x + 3)(1) * 2))
#------------------------------------------------
#   Q4(Higher-Order Functions)
# ------------------------------------------------
def polynomial(factors):
    """
    Creates a polynomial function based on a list of coefficients.
    The list 'factors' represents the polynomial:a_n*x^n + a_{n-1}*x^{n-1} + ... + a_1*x + a_0 where factors = [a_n, a_{n-1}, ..., a_0].
    Args: factors (list[int]): Coefficients of the polynomial ordered from highest degree to lowest.
    Returns: function: A function compute(x) that returns the value of the polynomial at the given input x.
    """
    def compute(x):
        """ 
        Evaluates the polynomial at the given value x.
        Args:x (int or float): Input value for evaluating the polynomial.
        Returns: int or float. The value of the polynomial at x.
        """
        sum = 0
        n = len(factors)
        for i, coef in enumerate(factors):
            pow = n - 1 - i
            sum += coef * (x ** pow)
        return sum

    return compute


# ------------------------------------------------
'''
>>> parabola = polynomial( [ 3, 5, 6 ] )
>>> parabola
<function polynomial.<locals>.eval at 0x0000017C842FE700>
>>> value = parabola( 3 )
>>> value
48
>>> polynom = polynomial( [ 1, 2, 1, 0 ] )
>>> value = polynom( 4 )
>>> value
100
'''


# ------------------------------------------------
#   Q5(Higher-Order Functions)
# ------------------------------------------------
import random

def code_cracker():
    secret_number = random.randint(10000, 99999)
    points = 100
    clue_count = 0
    digits = [int(d) for d in str(secret_number)]

    print("welcome to the pin cracker game!")

    # A: yes_or_no ------------------------------------------------------
    def yes_or_no(f, n):
        """
        Applies predicate f to n and returns 'Yes' or 'No'.
        """
        return "Yes" if f(n) else "No"

    # B: print_msg_to_func ----------------------------------------------
    def print_msg_to_func(msg, f):
        """
        Prints: msg : <result of f()>
        """
        print(msg, ":", f())

    # C: show_string_by_func --------------------------------------------
    def show_string_by_func(msg, f):
        """
        Prints patterns of X / - according to predicate f(digit)
        """
        pattern = ''.join("X" if f(int(d)) else "-" for d in str(secret_number))
        print(msg, ":", pattern)

    # ---------- Clues A–F ----------------------------------------------

    def clue_a():
        holder = input("Enter number to check if the code is smaller: ")
        holder = int(holder)
        print(yes_or_no(lambda x: x < holder, secret_number))

    def clue_b():
        holder = input("Enter number to check if the code is smaller: ")
        holder = int(holder)
        print(yes_or_no(lambda x: x > holder, secret_number))

    def clue_c():
        print_msg_to_func("sum", lambda: sum(digits))

    def clue_d():
        print_msg_to_func("sub", lambda: digits[0] - digits[-1])

    def clue_e():
        show_string_by_func("odd digits", lambda d: d % 2 == 1)

    def clue_f():
        show_string_by_func("digits divided by 3", lambda d: d % 3 == 0)

    clues = [clue_a, clue_b, clue_c, clue_d, clue_e, clue_f]

    # ------------------- Game Loop ------------------------------------

    while points > 0:
        clue_count += 1
        points -= 10

        print(f"\nclue #{clue_count}")
        random.choice(clues)()

        print("points left:", points)
        guess = input("guess or press ENTER for exit: ")

        if guess == "":
            print("\nwrong, bye bye!")
            print("Points left:", points)
            return

        if guess.isdigit() and int(guess) == secret_number:
            print("yes, correct!")
            print("points left:", points)
            return

    # If points ran out
    print("\nwrong, bye bye!")
    print("points left:", points)



code_cracker()

