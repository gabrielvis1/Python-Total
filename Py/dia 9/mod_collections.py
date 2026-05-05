""" modulo de colections """
from collections import Counter

numeros = [8,2,5,4,5,6,6,8,9,1,5,5,7]
frase = "al pan, pan, y al vino, vino"
serie = Counter([1,1,1,1,1,1,2,2,3,3,3,3,4])

print(Counter(numeros))
print(Counter("mississippi"))
print(Counter(frase.split()))
print(serie.most_common())
print(serie.most_common(1))
print(serie.most_common(2))
