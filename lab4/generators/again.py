#1

n = int(input())
some = (x*x for x in range(n))
for num in some :
    print(num)


#2
def even(n):
    for num in range(n):
        if num % 2 == 0:
            yield num

for num in even(n):
    print(num)

#3
def div(n):
    for num in range(n):
        if num % 3 == 0:
            yield num
        if num % 4 == 0:
            yield num

for num in div(n):
    print(num)

