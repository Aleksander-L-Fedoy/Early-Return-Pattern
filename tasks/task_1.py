"""
OPPGAVE: Tidlig retur og if-invertering

Skriv en funksjon som tar inn en alder (heltall) og sjekker hvilke rettigheter en person har i Norge.

Funksjonen skal returnere én bestemt tekst, avhengig av alder:
- Hvis personen er 18 år eller eldre, skal den returnere: «Kan kjøre bil, stemme og kjøpe alkohol»
- Hvis personen er minst 16, men under 18 år, skal den returnere: «Kan øvelsekjøre»
- Hvis personen er under 16 år, skal den returnere: «For ung»

Krav:
- Bruk tidlig retur slik at funksjonen avslutter så snart det er klart hvilket svar som gjelder.
- Inverter if-betingelser der det gir mening, slik at du unngår dype eller unødvendige else-blokker.
"""


def rettigheter(alder: int) -> str:
    """
    Returnerer hvilke rettigheter en person har basert på alder.
    Bruk tidlig retur og inverter if der det gir mening.
    """
    # Skriv kode her!
    pass  # Husk å fjerne denne


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
