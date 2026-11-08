import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2


def monte_carlo_integral(a, b, n):
    """Обчислення інтеграла методом Монте-Карло."""
    x = np.random.uniform(a, b, n)
    return (b - a) * np.mean(f(x))


if __name__ == "__main__":
    a, b = 0, 2

    # Щоб можна було відтворити результати
    np.random.seed(42)

    # Точний результат: інтеграл x² = x³ / 3
    exact = (b**3 - a**3) / 3

    print(f"Точне значення інтеграла: {exact:.6f}\n")
    print(f"{'Точки':>10} | {'Монте-Карло':>15} | {'Похибка (%)':>12}")

    for n in [1000, 10000, 100000, 1000000]:
        result = monte_carlo_integral(a, b, n)
        error = abs(result - exact) / exact * 100

        print(f"{n:>10} | {result:>15.6f} | {error:>12.4f}")

    # Побудова графіка
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    plt.plot(x, y, color="red", label="f(x) = x²")
    plt.fill_between(x, y, where=(x >= a) & (x <= b), color="gray", alpha=0.3)

    plt.axvline(a, color="gray", linestyle="--")
    plt.axvline(b, color="gray", linestyle="--")

    plt.title("Інтегрування методом Монте-Карло")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
