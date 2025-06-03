"""
OPPGAVE (avansert): Refaktorer til tidlig retur og if-invertering

Funksjonen `final_price_nested` under beregner sluttprisen på et kjøp, men er skrevet med tunge, nøstede if-setninger og mye gjentakelse.
Ditt oppdrag er å implementere `final_price_early_return` slik at den har **samme funksjonalitet**,
men bruker tidlig retur og if-invertering for å gjøre koden mer lesbar og pythonic.

Regler:
- Kunder kan være 'vip', 'student', 'regular' eller 'blacklisted'.
- Kjøp (purchase) kan være 'online' eller 'in_store'.
- VIP får 20% rabatt, uansett.
- Studenter får 15% rabatt, men bare på kjøp i butikk (in_store).
- Blacklisted får ikke kjøpe (prisen er alltid 0).
- Andre kunder får ingen rabatt.
- Hvis handlekurven inneholder mer enn 5 varer og kunden ikke er 'blacklisted', trekkes ytterligere 5% rabatt på sluttprisen.
- Hvis sluttprisen blir under 100 kr, skal det gis et varsel i retur som tuple: (pris, "Lav pris: dobbeltsjekk!").
- Funksjonen skal alltid returnere `(pris, feedback)`, der feedback er None om det ikke er varsel.
- Priser skal avrundes til to desimaler.
"""

from typing import Any

PRC = 2  # Precision for float rounding


# --- OPPGAVE: Implementer final_price_early_return med tidlig retur og if-invertering ---
def final_price_early_return(
    customer: str, purchase: dict[str, Any]
) -> tuple[float, str | None]:
    # Skriv kode her!
    pass  # Husk å fjerne denne


def final_price_nested(
    customer: str, purchase: dict[str, Any]
) -> tuple[float, str | None]:
    """Returnerer sluttpris for et kjøp, med riktige rabatter og varsel ved lav pris."""

    feedback = None

    if customer != "blacklisted":
        price = purchase["total"]
        items = purchase["items"]
        type_ = purchase["type"]

        if customer == "vip":
            price = price * 0.8
            if items > 5:
                price = price * 0.95
            if price < 100:
                feedback = "Lav pris: dobbeltsjekk!"
                return (round(price, PRC), feedback)
            else:
                return (round(price, PRC), feedback)
        else:
            if customer == "student":
                if type_ == "in_store":
                    price = price * 0.85
                    if items > 5:
                        price = price * 0.95
                    if price < 100:
                        feedback = "Lav pris: dobbeltsjekk!"
                        return (round(price, PRC), feedback)
                    else:
                        return (round(price, PRC), feedback)
                else:
                    if items > 5:
                        price = price * 0.95
                    if price < 100:
                        feedback = "Lav pris: dobbeltsjekk!"
                        return (round(price, PRC), feedback)
                    else:
                        return (round(price, PRC), feedback)
            else:
                if items > 5:
                    price = price * 0.95
                if price < 100:
                    feedback = "Lav pris: dobbeltsjekk!"
                    return (round(price, PRC), feedback)
                else:
                    return (round(price, PRC), feedback)
    else:
        price = 0
        return (round(price, PRC), feedback)


"""====================== TESTS ======================"""


def main():
    purchases = [
        {"total": 200, "items": 6, "type": "online"},
        {"total": 120, "items": 3, "type": "in_store"},
        {"total": 99, "items": 6, "type": "in_store"},
    ]
    tests = [
        final_price_early_return("blacklisted", purchases[0])
        == final_price_nested("blacklisted", purchases[0])
        == (0, None),
        final_price_early_return("vip", purchases[0])
        == final_price_nested("vip", purchases[0])
        == (152.0, None),
        final_price_early_return("student", purchases[1])
        == final_price_nested("student", purchases[1])
        == (102.0, None),
        final_price_early_return("student", purchases[0])
        == final_price_nested("student", purchases[0])
        == (190.0, None),
        final_price_early_return("student", purchases[2])
        == final_price_nested("student", purchases[2])
        == (79.94, "Lav pris: dobbeltsjekk!"),
        final_price_early_return("regular", purchases[0])
        == final_price_nested("regular", purchases[0])
        == (190.0, None),
        final_price_early_return("regular", purchases[1])
        == final_price_nested("regular", purchases[1])
        == (120.0, None),
    ]

    for idx, test in enumerate(tests, start=1):
        assert test, f"\033[91m❌ Test {idx} feilet\033[0m"

    print("\033[92m ✅ Alle tester bestått!\033[0m")


if __name__ == "__main__":
    main()
