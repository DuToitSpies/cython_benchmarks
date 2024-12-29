import timeit

for i in range(60):
    result = timeit.timeit("fibonacci.fibonacci(10)", setup="import fibonacci", number=50)
    print(result)
