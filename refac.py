def handle_order(order):
    if order is not None:
        if order.is_paid:
            if len(order.items) > 0:
                if order.customer.is_active:
                    print("Ordren behandles")
                else:
                    print("Kunde er ikke aktiv")
            else:
                print("Ordren har ingen varer")
        else:
            print("Ordren er ikke betalt")
    else:
        print("Ingen ordre mottatt")