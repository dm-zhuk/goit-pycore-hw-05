def caching_fibonacci():

    cache = {}  # Dictionary to store cached Fibonacci values

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        result = fibonacci(n - 1) + fibonacci(n - 2)  # Recursive calc

        cache[n] = result
        return result

    return fibonacci


if __name__ == "__main__":
    fibonacci = caching_fibonacci()

    print(fibonacci(10))
    print(fibonacci(15))
    print(fibonacci(25))
