"""EX03 - prime functions."""

__author__: str = "730317621"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(7))
    print(is_prime(4))
    print(list_primes(2,100))
    print(list_primes(5,75))


def is_prime(number: int) -> bool:
    character: int = number
    if character > 1:
        for i in range(2, (character // 2) + 1):
            if character % i == 0:
                return False
        return True
    else:
        return False


def list_primes(numero: int, numera: int) -> list[int]:
    primes = []
    lower_bound: int = numero
    upper_bound: int = numera
    for i in range(lower_bound, upper_bound):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == "__main__":
    main()