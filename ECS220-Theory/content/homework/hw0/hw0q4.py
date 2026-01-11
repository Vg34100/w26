import math


def f0(n):
    return 2 ** (n**2)


def f1(n):
    return 2 ** (2**n) if n < 10 else float("inf")  # grows too fast


def f2(n):
    return 5**n


def f3(n):
    return n ** (2 * n)


def f4(n):
    return math.log2(n) if n > 0 else 0


def f5(n):
    return 2 ** (2 * n)  # = 4^n


def f6(n):
    return 1


def f7(n):
    return math.sqrt(n)


def f8(n):
    return n**n if n > 0 else 1


def f9(n):
    return 3**n


def f10(n):
    return 4 ** (math.log2(n)) if n > 0 else 0  # = n^(log 4) = n^2


def f11(n):
    return 2**n


def f12(n):
    return n**2.5


def f13(n):
    return math.factorial(n) if n < 100 else float("inf")


def f14(n):
    return n**4


def f15(n):
    return n * (2**n)


functions = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15]

# Test with various n values
test_values = [10, 20, 50, 100, 200]

print("Testing with different n values:")
for n in test_values:
    print(f"\nn = {n}:")
    results = []
    for i, func in enumerate(functions):
        try:
            val = func(n)
            if val == float("inf") or val > 1e100:
                results.append((i, float("inf"), "inf"))
            else:
                results.append((i, val, f"{val:.2e}"))
        except:
            results.append((i, float("inf"), "error"))

    # Sort by value
    results.sort(key=lambda x: x[1])

    print("Order:", " ".join(str(r[0]) for r in results))
    print("Order:", ' '.join(str(r[0]) for r in results))
    for idx, val, val_str in results:
        print(f"  ({idx}): {val_str}")
