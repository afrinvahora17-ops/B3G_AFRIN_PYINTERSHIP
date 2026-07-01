def find_sum(n):
    if n==1:
        return 1
    else:
        return n+find_sum(n-1)
n=21
print("the Number is:",n)
print("sum of number 1 to n:",n,"=",find_sum(n))

