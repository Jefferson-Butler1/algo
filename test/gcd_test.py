from src.gcd import gcd

def test_finds_gcd_when_a_less():
    assert(gcd(8,12) == 4)
def test_finds_gcd_when_a_greater():
    assert(gcd(12,8) == 4)
def test_finds_gcd_when_a_is_exact_divisor():
    assert(gcd(4,12) == 4)
