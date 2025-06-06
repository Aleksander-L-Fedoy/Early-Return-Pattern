""" --- LØSNINGSFORSLAG --- """
def rettigheter(alder: int) -> str:
    """
    Returnerer hvilke rettigheter en person har basert på alder.
    """
    if (alder > 17):
        return "Kan kjøre bil, stemme og kjøpe alkohol"
    
    if (alder > 15):
        return "Kan øvelsekjøre"
    
    return "For ung"


"""====================== TESTS ======================"""


def main():
    tests = [
        rettigheter(20) == "Kan kjøre bil, stemme og kjøpe alkohol",
        rettigheter(18) == "Kan kjøre bil, stemme og kjøpe alkohol",
        rettigheter(17) == "Kan øvelsekjøre",
        rettigheter(16) == "Kan øvelsekjøre",
        rettigheter(15) == "For ung",
    ]

    for idx, test in enumerate(tests, start=1):
        assert test, f"\033[91m❌ Test {idx} feilet\033[0m"

    print("\033[92m✅ Alle tester bestått!\033[0m")


if __name__ == "__main__":
    main()
