A = ()
B = (1,2,3,4,5)
C =  (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})

print(A,B,C)
print()
print(C[1:4])
print()
print(B[-1])
print()

# [:] returns a shallow copy of the tuple, 
# while [::step] allows stepping through elements. 
# Using [::-1] reverses the sequence.

print(A[:])
print(A[1:])
print(A[::2])
print(C[::-1])