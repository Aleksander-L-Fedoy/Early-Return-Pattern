from typing import Any

# --- OPPGAVE: Implementer `sum_early_return` med funksjonaliteten fra `sum_nested` med tidlig-returnering og if-invertering ---
def sum_early_return(value1: Any, value2: Any) -> int | str:
    # Skriv kode her!
    pass  # Husk å fjerne denne


def sum_nested(value1: Any, value2: Any) -> int | str:
    """Tar inn to verdier og returnerer summen dersom begge verdiene er 'tall'."""
    if type(value1) == int or type(value1) == float:
        if type(value2) == int or type(value2) == float:
            result = value1 + value2
        else:
            result = "value2 is not a number"
    else:
        if type(value2) == int or type(value2) == float:
            result = "value1 is not a number"
        else:
            result = "value1 and value2 are not numbers"
    return result


"""====================== TESTS ======================"""


def main():
    tests = [
        sum_early_return(0, 1) == sum_nested(0, 1) == 1,
        sum_early_return("0", 1) == sum_nested("0", 1) == "value1 is not a number",
        sum_early_return(0, "1") == sum_nested(0, "1") == "value2 is not a number",
        sum_early_return("0", "1")
        == sum_nested("0", "1")
        == "value1 and value2 are not numbers",
    ]

    for idx, test in enumerate(tests, start=1):
        assert test, f"\033[91m❌ Test {idx} feilet\033[0m"

    print("\033[92m ✅ Alle tester bestått!\033[0m")


if __name__ == "__main__":
    main()
