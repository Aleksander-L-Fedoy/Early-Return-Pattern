def handle_order(order):
    feedback = None

    if order is not None:
        if order.is_paid:
            if len(order.items) > 0:
                if order.customer.is_active:
                    feedback = "Ordren behandles"
                else:
                    feedback = "Kunde er ikke aktiv"
            else:
                feedback = "Ordren har ingen varer"
        else:
            feedback = "Ordren er ikke betalt"
    else:
        feedback = "Ingen ordre mottatt"

    return feedback


""" --- LØSNINGSFORSLAG --- """


def handle_order(order):
    if order is None:
        return "Ingen ordre mottatt"

    if not order.is_paid:
        return "Ordren er ikke betalt"

    if len(order.items) == 0:
        return "Ordren har ingen varer"

    if not order.customer.is_active:
        return "Kunde er ikke aktiv"

    return "Ordren behandles"  # Funksjonens hovedlogikk
