def arabicToRoman(n):
    roman, dict = "", {1: "i", 5: "v", 10: "x", 50: "l", 100: "c", 500: "d", 1000: "m"}
    values = [1000, 500, 100, 50, 10, 5, 1]

    for i, v in enumerate(values):
        if n // v == 4:
            roman+=dict[values[i]]+dict[values[i-1]]
        elif n // v > 0:
            roman+=dict[values[i]] * (n // v)

        n-= n // v * v

    return roman

def romanToArabic(n):
    n, num, i, dict = n.lower(), 0, 0, {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}

    while i < len(n):
        if dict[n[i+1]] > dict[n[i]]:
            num+= dict[n[i+1]] - dict[n[i]]
            i+= 1
        else:
            num+= dict[n[i]]

        i+= 1

    return num
