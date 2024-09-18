#Millen, Asobo, Isaac, Jeff
from src.gcd import gcd
class Fraction:
    def __init__(self, numerator, denominator):
        g = gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"
    def __add__(self, other):
        numerator = (self.numerator * other.denominator)+(other.numerator * self.denominator)
        denominator = (self.denominator * other.denominator)
        return Fraction(numerator, denominator)
    def __sub__(self, other):
        numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        denominator = (self.denominator * other.denominator)
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = (self.numerator * other.numerator)
        denominator = (self.denominator * other.denominator)
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = (self.numerator * other.denominator)
        denominator = (self.denominator * other.numerator)
        return Fraction(numerator, denominator)
    def __float__(self):
        return self.numerator / self.denominator

    def __eq__(self, other):
        if self.numerator * other.denominator == self.denominator * other.numerator:
            return True
        else:
            if self.denominator * other.numerator == self.numerator:
                return True
            else:
                return False

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __le__(self, other):
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator

