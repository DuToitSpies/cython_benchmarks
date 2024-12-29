import timeit

for i in range(60):
    result = timeit.timeit("float.benchmark(100)", setup="import float", number=100)
    print(result)