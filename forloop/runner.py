import timeit

for i in range(60):
    result = timeit.timeit("forloop.forloop()", setup="import forloop", number=10)
    print(result)