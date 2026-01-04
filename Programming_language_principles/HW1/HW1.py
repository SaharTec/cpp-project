# --------------------------------------------
#                   Q1
# --------------------------------------------
# cheack if a given year is a leap year
def is_leap_year( year ):
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            return True
#return the last day of each month   
def is_last_day( d, m, y ):
     if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
     elif m in [4, 6, 9, 11]:
        return 30
     elif m == 2:
        return 29 if is_leap_year(y) else 28
#print the next day of the given date
def print_next_date( date ):
    d = int(date / 1000000)
    m = int((date / 10000) % 100)
    y = int(date % 10000)

    print( "Source Date: "f"{d:02d}/{m:02d}/{y}")

    if(d == is_last_day(d , m ,y)):
        if(m == 12):
            d = 1
            m = 1
            y = y + 1
        else:
            d = 1
            m = m + 1 
    else:
        d = d + 1

    print("Next Day: "f"{d:02d}/{m:02d}/{y}")


# --------------------------------------------
'''
>>> print_next_date( 28102025 )
Source Date: 28/10/2025
Next Day:    29/10/2025
>>> print_next_date( 31102025 )
Source Date: 31/10/2025
Next Day:    01/11/2025
>>> print_next_date( 28022024 )
Source Date: 28/02/2024
Next Day:    29/02/2024
>>> print_next_date( 28022026 )
Source Date: 28/02/2026
Next Day:    01/03/2026
>>> print_next_date( 31122025 )
Source Date: 31/12/2025
Next Day:    01/01/2026
'''

# --------------------------------------------
#                   Q2
# --------------------------------------------
def arange_digits( num ):
    """bulding 2 string that represent odd and even numbers"""
    evenstr = ""
    oddStr= ""
    """casting the input number into string"""
    number = str(num)
    """go trow the number string and sort for even and odd number to the correct string"""
    for n in number:
        digit = int(n)
        if(digit % 2 == 0):
            evenstr += n
        else:
            oddStr += n
    """build a sorted string whene even numbers are first"""        
    new_num = evenstr + oddStr
    """casting the string into int"""
    return int(new_num)

# --------------------------------------------
'''
>>> print("Number %d after arange digits: %d" % (1234567,arange_digits(1234567)))
Number 1234567 after arange digits: 2461357
>>> print("Number %d after arange digits: %d" % ( 2804,arange_digits(2804)))
Number 2804 after arange digits: 2804
>>> print("Number %d after arange digits: %d" % (5713,arange_digits(5713)))
Number 5713 after arange digits: 5713
'''

# --------------------------------------------
#                   Q3
# --------------------------------------------
#if the number is prime it will print it
def print_prime_numbers( ):
    min, max = 100 , 200
    print("Prime numbers [100,200]: ", end="")
    for n in range(min,max+1):
        if is_prime(n) == True:
            print(n , end=",")
    #check if a given number in range is prime or not

def is_prime(num):
    #Check if a given number is prime or not.
    if num <= 1:
        return False
    # Check for divisibility from 2 up to the square root of num
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False  # Found a divisor, so it's not prime.
    
    return True  # Only returns True if the loop finishes without returning False.

    
# --------------------------------------------
'''
>>> print_prime_numbers( )
Prime numbers [100,200]: 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
'''

# --------------------------------------------
#                   Q4
# --------------------------------------------
#print a parmid base on given size 
def print_figure( n ):
    width = 2 * n + 1
    print("*".center(width))
    #print * to each row
    for num in range(1, n):
        line = "*"
        #add all the number between 1 and n an upper order
        for i in range(1 ,num + 1):
            line += str(i)
        #add all the number between 1 and n an lower order
        for i in range(num - 1, 0, -1):
            line += str(i)

        line += "*"
        print(line.center(width))

    print("*" * width) 
        
# --------------------------------------------
'''
>>> print_figure( 11 )
          *
         *1*
        *121*
       *12321*
      *1234321*
     *123454321*
    *12345654321*
   *1234567654321*
  *123456787654321*
 *12345678987654321*
*********************
'''
# --------------------------------------------
#                   Q5
# --------------------------------------------
#count the amount of values in a number
def count_digits( n ):
   if (n < 10):
       return 1
   else:
       return 1 + count_digits(n // 10)
# find the largest max digit in the number
def max_digit( n ):
    if(n < 10):
        return n
    
    last = n % 10
    rest = max_digit(n // 10)

    if(last > rest):
        return last
    else:
        return rest
# add the amount of digits in the number and add to it the max digit
def num_weight( n ):
    if (n < 10):
        return n + 1
    else:
        return count_digits(n) + max_digit(n)

# --------------------------------------------
'''
>>> count_digits( 351 )
3
>>> max_digit( 351 )
5
>>> num_weight( 7145 )
11
>>> num_weight( 15 )
7
>>> num_weight ( 351 )
8
'''
# --------------------------------------------
#                   Q6
# --------------------------------------------
#cheack if a number is a pow of 2
def is_power2( n ):
    if(n == 2):
        return True
    if(n % 2 == 0):
        return is_power2(n // 2)
    else:
        return False

# --------------------------------------------
'''
>>> is_power2( 1024 )
True
>>> is_power2( 1000 )
False
'''
# --------------------------------------------
#                   Q7
# --------------------------------------------
#remove all the 0 in a number
def reduce( n ):
    #if the number is negetive we set the sinh to -1 to make the new number also negetive
    if(n < 0):
        sign = -1
    else:
        sign = 1
    n = abs(n)

    if n < 10:
        return sign * n if n != 0 else 0
    
    # remove all the 0    
    last_num = n % 10
    rest_num = reduce(n // 10)

    if(last_num == 0):
        red = rest_num
    else:
        red = rest_num * 10 + last_num
    #retuen the new number without 0
    return red * sign

# ------------------------------------------------
'''
>>> reduce( -160760 )
-1676
>>> reduce( 1020034000 )
1234
'''

# --------------------------------------------
#                   Q8
# --------------------------------------------
#return a value of of a given row and col in pascal  
def pascal( n, m ):
    if (m > n):
        return -1
    if (m == 0 or m == n):
        return 1
    return pascal(n -1, m -1) + pascal(n -1, m)


# ------------------------------------------------
'''
>>> pascal( 5, 1 )
5
>>> pascal( 3, 2 )
3
>>> pascal( 10, 4 )
210
>>> pascal( 5, 3 )
10
>>> pascal( 5, 2 )
10
>>> pascal( 5, 13 )
-1
'''

# --------------------------------------------
#                   main
# --------------------------------------------
def main( ):
    print("<<< Q#1 >>>")
    print_next_date( 28102025 )
    print_next_date( 31102025 )
    print_next_date( 28022024 )
    print_next_date( 28022026 )
    print_next_date( 31122025 )
    print("<<< Q#2 >>>")
    print("Number %d after arange digits: %d" % (1234567,arange_digits(1234567)))
    print("Number %d after arange digits: %d" % ( 2804,arange_digits(2804)))
    print("Number %d after arange digits: %d" % (5713,arange_digits(5713)))
    print("<<< Q#3 >>>")
    print_prime_numbers( )
    print("<<< Q#4 >>>")
    print_figure( 11 )
    print("<<< Q#5 >>>")
    print( count_digits( 351 ) )
    print( max_digit( 351 ) )
    print( num_weight( 7145 ), end = ', ' )
    print( num_weight( 15 ), end = ', ' )
    print( num_weight ( 351 ) )
    print("<<< Q#6 >>>")
    print( is_power2( 1024 ), end = ', ')
    print( is_power2( 1000 ) )
    print("<<< Q#7 >>>")
    print( reduce( -160760 ), end = ', ' )
    print( reduce( 1020034000 ) )    
    print("<<< Q#8 >>>")
    print( pascal( 5, 1 ), end = ', ')
    print( pascal( 3, 2 ), end = ', ' )
    print( pascal( 10, 4 ), end = ', ')
    print( pascal( 5, 3 ), end = ', ')
    print( pascal( 5, 2 ), end = ', ')
    print( pascal( 5, 13 ) )
    

# --------------------------------------------
'''
<<< Q#1 >>>
Source Date: 28/10/2025
Next Day:    29/10/2025
Source Date: 31/10/2025
Next Day:    01/11/2025
Source Date: 28/02/2024
Next Day:    29/02/2024
Source Date: 28/02/2026
Next Day:    01/03/2026
Source Date: 31/12/2025
Next Day:    01/01/2026
<<< Q#2 >>>
Number 1234567 after arange digits: 2461357
Number 2804 after arange digits: 2804
Number 5713 after arange digits: 5713
<<< Q#3 >>>
Prime numbers [100,200]: 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
<<< Q#4 >>>
          *
         *1*
        *121*
       *12321*
      *1234321*
     *123454321*
    *12345654321*
   *1234567654321*
  *123456787654321*
 *12345678987654321*
*********************
<<< Q#5 >>>
3
5
11, 7, 8
<<< Q#6 >>>
True, False
<<< Q#7 >>>
-1676, 1234
<<< Q#8 >>>
5, 3, 210, 10, 10, -1
'''
main()