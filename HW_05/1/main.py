def caching_fibonacci():

    cache = {}  # Dict to store cached Fibonacci values

    def fib(n):
        if n in cache:
            return cache[n]
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        res = fib(n - 1) + fib(n - 2)  # Recursive calc

        cache[n] = res
        return res

    return fib


if __name__ == "__main__":
    fib = caching_fibonacci()

    print(f'Output of 3 is {fib(3)}')   # 2
    print(f'Output of 15 is {fib(15)}')  # 610
    print(f'Output of 25 is {fib(25)}')  # 75025
