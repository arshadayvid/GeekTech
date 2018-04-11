#Tell the user to type in the first side as 'a'
a = int(input('enter the value of a'))

#Tell the user to type in the second side as 'b'
b = int(input('enter the value of b'))

#Tell the user to type in the third side as 'c'
c = int(input('enter the value of c'))

s = (a+b+c)/3
z = int (s*(s-a)*(s-b)*(s-c))
print (z)
