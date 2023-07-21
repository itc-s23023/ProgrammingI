# def func_square(*args):
#     results = []
#     for n in args:
#         results.append(n * n)
#     return results


def func_square(*args):
    results = []

    for i in args:
        results.append(i * i)

    for i in range(0, len(results), 10):
        print(results[i : i + 10])


# def func_square(*args):
#     results = [i * i for i in args]
#     for i in range(0, len(results), 10):
#         print(results[i:i+10])
numbers = list(range(100))
func_square(*numbers)
