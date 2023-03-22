Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> @*3
SyntaxError: invalid syntax
>>> 2*3
6
>>> 2=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> for a in range(2,8):print(a,a**2)
... 
2 4
3 9
4 16
5 25
6 36
7 49
2
>>> for y in range(1,10)
SyntaxError: incomplete input
>>> for y in range(1,5):
...     for x in range(y) :
...         print('#', end='')
...     print()
... 
...     
#
##
###
####
