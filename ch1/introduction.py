#
a = 1 + 2 + 3
print(a); #print 6

#Multi-line statement with \
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
        7 + 8 + 9
print(a); #print 45

#Multi-line statement with "()"
a = (1 + 2 + 3 + 
    4 + 5 + 6 + 
        7 + 8 + 9)

print(a); #print 45

colors = ['red',
          'blue',
          'green']
print(colors[0]);


#print and a need to align and need indent 
if True:
 print('Hello')
 a = 5

print(a);

#Multi-line comments

#example 1
#line1
#line2
#line3

#example 2
"""line1
line2
line3"""


def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__);


def testFunc(num):
    """test __doc__
    hihi hihi hihi hihi
    """
    return 

print(testFunc.__doc__); 
#print 
#test __doc__
#    hihi hihi hihi hihi


