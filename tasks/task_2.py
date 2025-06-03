class User:
    def __init__(self, is_active, has_coupon):
        self.is_active = is_active
        self.has_coupon = has_coupon


# --- OPPGAVE: Implementer `calculate_discount_early_return` med funksjonaliteten fra `calculate_discount_nested` med tidlig-returnering og if-invertering ---
def calculate_discount_early_return(user: User) -> int:
    # Skriv kode her!
    pass  # Husk å fjerne denne


def calculate_discount_nested(user: User) -> int:
    """Returnerer rabatt for en bruker basert på om brukeren er aktiv og om de har kupong"""
    discount = 0

    if user.is_active:
        if user.has_coupon:
            discount = 20
        else:
            discount = 10

    return discount


"""====================== TESTS ======================"""


def main():
    user1 = User(is_active=True, has_coupon=True)
    user2 = User(is_active=True, has_coupon=False)
    user3 = User(is_active=False, has_coupon=True)
    user4 = User(is_active=False, has_coupon=False)

    tests = [
        calculate_discount_early_return(user1) == calculate_discount_nested(user1),
        calculate_discount_early_return(user2) == calculate_discount_nested(user2),
        calculate_discount_early_return(user3) == calculate_discount_nested(user3),
        calculate_discount_early_return(user4) == calculate_discount_nested(user4),
    ]

    for idx, test in enumerate(tests, start=1):
        assert test, f"\033[91m❌ Test {idx} feilet\033[0m"

    print("\033[92m ✅ Alle tester bestått!\033[0m")


if __name__ == "__main__":
    main()
