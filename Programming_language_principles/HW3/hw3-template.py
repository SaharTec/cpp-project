# ------------------------------------------------
#       Q1(ADT Date - dispatch)
# ------------------------------------------------
def make_time( h, m, s ):

    def divideTime(msg):
        if(msg == 'hour'):
            return h
        elif(msg == 'minute'):
            return m
        elif(msg == 'second'):
            return s
        
    return divideTime
    
# ------------------------------------------------
def getitem_pair( p, i ):
    return p(i)
# ------------------------------------------------
def hour( time ):
    return time('hour')
# ------------------------------------------------
def minute( time ):
    return time('minute')
# ------------------------------------------------
def second( time ):
     return time('second')
# ------------------------------------------------

def time_difference( time1, time2 ):
    total1 = hour(time1) * 3600 + minute(time1) * 60 + second(time1)
    total2 = hour(time2) * 3600 + minute(time2) * 60 + second(time2)
    diff = abs(total1 - total2)
    h = diff // 3600
    m = (diff % 3600) // 60
    s = diff % 60

    return make_time(h, m, s)
    
# ------------------------------------------------

def str_time( time, tformat = 'hh:mm:ss' ):
    h = hour(time)
    m = minute(time)
    s = second(time)

    if (tformat == 'hh:mm:ss'):
        return f'{h:02d}:{m:02d}:{s:02d}'
    elif (tformat == 'hh:mm'):
        return f'{h:02d}:{m:02d}'
    elif (tformat == 'HH:MM:SS' ,'HH:MM'):
        
        if(h < 12):
            period = 'A.M.'
        else: 
            period = 'P.M.'
        
        h12 = h % 12
        if( h12 == 0):
            h12 = 12
        if(tformat == 'HH:MM:SS'):
            return f'{h12}:{m:02d}:{s:02d} {period}'
        else:
            return f'{h12}:{m:02d} {period}'


    
# ------------------------------------------------
def time_correction( time, corr):
    
    total = hour(time) * 3600 + minute(time) * 60 + second(time)
    total += corr
    total %= 86400
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60

    return make_time(h, m, s) 

# ------------------------------------------------
#       Q2(ADT Tree - dispatch?)
# ------------------------------------------------

def make_tree( val, left, right ):
    def despatch(msg):
        if(msg == 'value'):
            return val
        elif(msg == 'left'):
            return left
        elif(msg == 'right'):
            return right
    return despatch
        
# ------------------------------------------------

def getitem_pair( p, i ):
    return p(i)

# ------------------------------------------------

def value( tree ):
    return tree('value')

# ------------------------------------------------

def left( tree ):
    return tree('left')

# ------------------------------------------------

def right( tree ):
    return tree('right')

# ------------------------------------------------

def print_tree( tree ):
    #print the values in order
    if tree == None:
        return 
    print_tree(left(tree))
    print(value(tree), end=' ')
    print_tree(right(tree))

# ------------------------------------------------

def min_value( tree ):
    #return the minimum value in the tree
    if(tree is None) :
        return float('inf')
    return min((value(tree)),min_value(left(tree)),min_value(right(tree)))

# ------------------------------------------------

def mirror_tree( tree ):

    if(tree is None) :
        return None
    return make_tree(value(tree),mirror_tree(right(tree)),mirror_tree(left(tree)))

# ------------------------------------------------
# Q3(Conventional Interfaces, Generator expressions)
# ------------------------------------------------

Q3 = lambda func,data: tuple(x for x in data if sum(f(x) for f in func) == 1)

# ------------------------------------------------
#print(Q3((lambda x: x>0,lambda x: x%2==0,lambda x: 9<abs(x)<100),(20,-45,133,8,400,7,-300,68)))


# ------------------------------------------------
# Q4(Pipeline)
# ------------------------------------------------

from functools import reduce
temp =[('London',18,16),('Paris',18,20),('Madrid',30,35),('Berlin',20,20),('Roma',32,27)]
Q4a = lambda data: [(city, max(t1, t2)) for city, t1, t2 in data]
Q4b = lambda data: [city for city,t1, t2 in data if t1 < t2]
Q4c = lambda data: reduce( lambda acc ,x: acc and x[1] != x[2], data, True )
Q4d = lambda data: dict(sorted(reduce(lambda acc, x: {**acc, abs(x[1] - x[2]): acc.get(abs(x[1] - x[2]), []) + [x[0]]}, data, {}).items()))


# ------------------------------------------------
#       Q5(Dispatch, Message Passing - Sets)
# https://en.wikipedia.org/wiki/Set_(mathematics)#Basic_operations
# ------------------------------------------------

def sets( d ):
    data = tuple(x for x in d if x > 0 and x <= 20)

    def dispatch(msg, *args):
        nonlocal data
        if(msg == 'set'):
            data = tuple(x for x in args[0] if x > 0 and x <= 20)
        elif(msg == 'view'):
            return '{' + ' ,' .join(map(str,sorted(data))) + '}'
        elif(msg == 'in'):
            return args[0] in data
        elif(msg == 'not in'):
            return args[0] not in data
        elif(msg == 'not'):
            return sets(tuple(x for x in range(21) if x not in data))
        elif(msg == '+'):
            other = args[0]
            other_data = tuple(x for x in range(21) if other('in',x))
            return sets(tuple(set(data) | set(other_data)))
        elif(msg == '*'):
            other = args[0]
            other_data = tuple(x for x in range(21) if other('in',x))
            return sets(tuple(set(data) & set(other_data)))
        elif(msg == '\\'):
            other = args[0]
            other_data = tuple(x for x in range(21) if other('in',x))
            return sets(tuple(set(data) - set(other_data)))
        elif(msg == 'xor'):
            other = args[0]
            other_data = tuple(x for x in range(21) if other('in',x))
            return sets(tuple(set(data) ^ set(other_data)))
    return dispatch

# ------------------------------------------------
# Q6(Dispatch Dictionary, Message Passing-Matrix)
# ------------------------------------------------

def matrix( mtr, n, m ):
    data = list(mtr)
    row = n
    col = m

    def add_line(new_line):
        nonlocal data, row
        data.extend(new_line)
        row += 1
        return data
    
    def add_column(new_col):
        nonlocal data, col
        new_data = []
        for i in range(row):
            for j in range(col):
                new_data.append(data[i * col + j])
            new_data.append(new_col[i])
        data[:] = new_data
        col += 1
        return data
    
    def print():
        index = [0]

        def print_row():
            row_index = index[0]
            index[0] += 1
            element_index = [0]

            def print_col():
                col_index = element_index[0]
                element_index[0] += 1
                return data[row_index * col + col_index ]
            
            return {'print' : print_col}
        
        return {'print': print_row}
    
    def line():
        return row
    
    def column():
        return col
    
    def shift_up():
        nonlocal data
        if row <= 1:
            return data
        
        first_row = data[:col]
        data[:] = data[col:] + first_row
        return data
    
    def shift_down():
        nonlocal data
        if row <= 1:
            return data
        last_row = data[-col:]
        data[:] = data[:-col] + last_row
        return data
    
    def shift_left():
        nonlocal data
        if col <= 1:
            return data
        
        new_data = []
        for i in range(row):
            starting_row = i * col
            row_data = data[starting_row:starting_row + col]
            new_data.extend(row_data[1:] + row_data[:1])
        data[:] = new_data
        return data
    
    def shift_right():
        nonlocal data, row
        if col <= 1:
            return data
        
        new_data = []
        for i in range(row):
            starting_row = i * col
            row_data = data[starting_row:starting_row + col]
            new_data.extend(row_data[-1:] + row_data[:-1])
        data[:] = new_data
        return data
    
    def transpose():
        nonlocal data, row, col
        new_data = []
        old_row, old_col = row, col
       
        for j in range(old_col):
            for i in range(old_row):
                new_data.append(data[i * old_col + j])
        data[:] = new_data
        row, col = old_col, old_row
        return data
    
    return {
        'add_line' : add_line,
        'add_column' : add_column,
        'print': print,
        'line' :line,
        'column':column,
        'shift_up': shift_up,
        'shift_down' :shift_down,
        'shift_left': shift_left,
        'shift_right' :shift_right,
        'transpose': transpose
    }


# ------------------------------------------------
'''
>>> m1 = matrix( ( 1, 2, 3, 4, 5, 6, 7, 8 ), 2, 4 )
>>> m1[ 'add_line' ]( ( 1, 3, 5, 7 ) )
[1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5, 7]
>>> m1[ 'add_column' ]( ( 2, 4, 6 ) )
[1, 2, 3, 4, 2, 5, 6, 7, 8, 4, 1, 3, 5, 7, 6]
>>> mat1 = m1[ 'print' ]( )
>>> for _ in range( m1[ 'line' ]( ) ):
	line = mat1[ 'print' ]( )
	for _ in range( m1[ 'column' ]( ) ):
		print( line[ 'print' ]( ), end = ' ')
	print( )
1 2 3 4 2 
5 6 7 8 4 
1 3 5 7 6 
>>> m1[ 'shift_up' ]( )
[5, 6, 7, 8, 4, 1, 3, 5, 7, 6, 1, 2, 3, 4, 2]
>>> m1[ 'shift_right' ]( )
[4, 5, 6, 7, 8, 6, 1, 3, 5, 7, 2, 1, 2, 3, 4]
>>> m1[ 'transpose' ]( )
[4, 6, 2, 5, 1, 1, 6, 3, 2, 7, 5, 3, 8, 7, 4]
>>> mat1 = m1[ 'print' ]( )
>>> for _ in range( m1[ 'line' ]( ) ):
	line = mat1[ 'print' ]( )
	for _ in range( m1[ 'column' ]( ) ):
		print( line[ 'print' ]( ), end = ' ' )
	print( )
4 6 2 
5 1 1 
6 3 2 
7 5 3 
8 7 4 
>>>
'''
# ------------------------------------------------
#   driver
# ------------------------------------------------
def driver( ):
    print('<<< Q1 >>>')
    t1 = make_time( 11, 5, 47 )
    print( t1 )
    print( hour( t1 ) )
    print( minute( t1 ) )
    print( str_time( t1 ) )
    t2 = make_time( 0, 12, 23 )
    print( str_time( t2, 'HH:MM' ) )
    print( str_time( time_difference( t1, t2 ) ) )
    print( str_time(time_correction( t1, 4623 ),'HH:MM:SS' ) )
    t2 = time_correction( t2, -920 )
    print( str_time( t2 ) )
    print( str_time( t2, 'HH:MM' ) )
    print('<<< Q2 >>>')
    tree = make_tree( 12, make_tree( 6, make_tree( 8, None, None ), None ),
    make_tree( 7, make_tree( 2, None, None ), make_tree( 15, None, None ) ) )
    print( tree )
    print( value( tree ) )
    print( value( left( tree ) ) )
    print( left( right( tree ) ) )
    print( value( left( right( tree ) ) ) )
    print_tree( tree )
    print( )
    print( min_value( tree ) )
    tree1 = mirror_tree( tree )
    print_tree( tree1 )
    print( )
    print('<<< Q3 >>>')
    print( Q3( ( lambda x: x > 0, lambda x: x % 2 == 0, lambda x: 9 < abs( x ) < 100 ),
               (20,-45,133,8,400,7,-300,68) ) )
    print('<<< Q4 >>>')
    print( Q4a( temp ) )
    print( Q4b( temp ) )
    print( Q4c( temp ) )
    print( Q4c( temp[ : 3 ] + temp[ -1: ] ) )
    print( Q4d( temp ) )
    print('<<< Q5 >>>')
    s1 = sets(( 1, 2, 3, 4, 5, 100 ) )
    print( s1 )
    print( s1( 'view' ) )
    print( s1( 'in', 3 ) )
    print( s1( 'not in', 31 ) )
    print( s1( 'not in', 3 ) )
    s2 = s1( 'not' )
    print( s2 )
    print( s2( 'view' ) )
    s1( 'set', ( 1, 2, 3, 4, 5, 7, 9, 12, 17 ) )
    s2( 'set', ( 2, 4, 5, 10, 14, 16, 20 ) ) 
    print( s1( '+', s2 )( 'not' )( 'view' ) )
    print( s1( '*', s2 )( 'xor', s1( '\\', sets( ( 2, 3, 5, 12 ) ) ) )( 'view' ) )

    print('<<< Q6 >>>')

    m1 = matrix( ( 1, 2, 3, 4, 5, 6, 7, 8 ), 2, 4 )
    print( m1[ 'add_line' ]( ( 1, 3, 5, 7 ) ) )
    print( m1[ 'add_column' ]( ( 2, 4, 6 ) ) )
    mat1 = m1[ 'print' ]( )
    for _ in range( m1[ 'line' ]( ) ):
        line = mat1[ 'print' ]( )
        for _ in range( m1[ 'column' ]( ) ):
            print( line[ 'print' ]( ), end = ' ')
        print( )
    print( m1[ 'shift_up' ]( ) )
    print( m1[ 'shift_right' ]( ) )
    print( m1[ 'transpose' ]( ) )
    mat1 = m1[ 'print' ]( )
    for _ in range( m1[ 'line' ]( ) ):
        line = mat1[ 'print' ]( )
        for _ in range( m1[ 'column' ]( ) ):
            print( line[ 'print' ]( ), end = ' ' )
        print( )
driver()
# ------------------------------------------------
'''
<<< Q1 >>>
<function make_time.<locals>.dispatch at 0x000001D35DF3FA60>
11
5
11:05:47
12:12 A.M.
10:53:24
12:22:50 P.M.
23:57:03
11:57 P.M.

<<< Q2 >>>

<function make_tree.<locals>.dispatch at 0x000001D35DF3FEC0>
12
6
<function make_tree.<locals>.dispatch at 0x000001D35DF3FCE0>
2
8 6 12 2 7 15 
2
15 7 2 12 6 8 

<<< Q3 >>>

(-45, 133, 7, -300)

<<< Q4 >>>

[('London', 18), ('Paris', 20), ('Madrid', 35), ('Berlin', 20), ('Roma', 32)]
['Paris', 'Madrid']
False
True
{0: ['Berlin'], 2: ['London', 'Paris'], 5: ['Madrid', 'Roma']}

<<< Q5 >>>
<function sets.<locals>.dispatch at 0x000001D35DF4C9A0>
{1, 2, 3, 4, 5}
True
True
False
<function sets.<locals>.dispatch at 0x000001D35DF4D120>
{6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
{6, 8, 11, 13, 15, 18, 19}
{1, 2, 5, 7, 9, 17}

<<< Q6 >>>
[1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5, 7]
[1, 2, 3, 4, 2, 5, 6, 7, 8, 4, 1, 3, 5, 7, 6]
1 2 3 4 2 
5 6 7 8 4 
1 3 5 7 6 
[5, 6, 7, 8, 4, 1, 3, 5, 7, 6, 1, 2, 3, 4, 2]
[4, 5, 6, 7, 8, 6, 1, 3, 5, 7, 2, 1, 2, 3, 4]
[4, 6, 2, 5, 1, 1, 6, 3, 2, 7, 5, 3, 8, 7, 4]
4 6 2 
5 1 1 
6 3 2 
7 5 3 
8 7 4 
'''
driver()
