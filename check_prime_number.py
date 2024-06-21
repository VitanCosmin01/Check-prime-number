"""
Write a Python unit test program to check if a given number is prime or not.
"""
import unittest


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


numbers = input("Introdu numere separate prin spațiu: ").split()
prime_numbers = []
non_prime_numbers = []

for number in numbers:
    number = int(number)
    if is_prime(number):
        prime_numbers.append(number)
    else:
        non_prime_numbers.append(number)


print("Numere prime: ", prime_numbers)
print("Numere non-prime: ", non_prime_numbers)


class PrimeNumberTestCase(unittest.TestCase):

    def test_prime_numbers(self):
        for number in prime_numbers:
            self.assertTrue(is_prime(number), f'{number} is not a prime number!')
#

    def test_non_prime_numbers(self):
        for number in non_prime_numbers:
            self.assertFalse(is_prime(number), f'{number} is a prime number')
