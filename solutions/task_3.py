from typing import Any

""" --- LØSNINGSFORSLAG --- """
def sum_early_return(value1: Any, value2: Any) -> int | str:
    value1_is_num = (type(value1) == int or type(value1) == float)
    value2_is_num = (type(value2) == int or type(value2) == float)

    if (not value1_is_num) and (not value2_is_num):
        return "value1 and value2 are not numbers"
    
    if not value1_is_num:
        return "value1 is not a number"

    if not value2_is_num:
        return "value2 is not a number"

    return value1 + value2


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
