from functools import reduce
print(reduce((lambda r,x:(r.difference_update(range(x**2,10**6,x)) or r)if (x in r)else r),range(2,10**6),set(range(2,10**6))))
