store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_real  = lambda data: (data[0], data[1]*5.08)
to_dollars = lambda data: (data[0], data[1]/5.08)

store_dollars = list(map(to_dollars, store))

for i, p, in store_dollars:
    print(f"{i}: ${p:.2f}")