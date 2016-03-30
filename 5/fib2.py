def super_fibonacci(n, m):
    a, i = [], m
    if m > n or m == 1:
        return 1
    else:
        a = [ 1 for j in range(m) ]
        while i != n:
            a.append(sum(a[len(a)-m:]))
            i += 1
        return a[-1]

print(super_fibonacci(2,1))
print(super_fibonacci(3,5))
print(super_fibonacci(8,2))
print(super_fibonacci(9,3))
print(super_fibonacci(9,4))
