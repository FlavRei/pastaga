def pastaga(a:int, b:int) -> int:
    if a > 10:
        return a + b + 2
    return a + b

compte_les_verres = pastaga(8, 10)
print(compte_les_verres)