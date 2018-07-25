a=10
squares=[]
for value in range(1,a,2) :
    square=value**2
    squares.append(square)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))
