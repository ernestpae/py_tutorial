def manyArgs(*a):
    result = ''
    for w in a:
        result += w
    return result
print(manyArgs('Ama ',"Kojo ",'kofi'))