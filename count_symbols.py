text = input()
symbols = {}

for letter in text:

    if letter not in symbols:
        symbols[letter] = 0
    symbols[letter] += 1

sorted_symbols = dict(sorted(symbols.items(), key=lambda x: x[0]))

for symbol, count in sorted_symbols.items():
    print(f"{symbol}: {count} time/s")
