def checkDict(d: dict) -> dict:
    for k, v in d.items():
        if v[0] == '✅':
            d[k] = True
        else:
            d[k] = False
    return d
