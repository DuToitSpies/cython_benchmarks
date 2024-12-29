import timeit

for i in range(60):
    result = timeit.timeit("fannkuch.fannkuch(6)", setup="import fannkuch", number=20)
    print(result)