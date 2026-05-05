""" modulo de colections """
from collections import defaultdict

mi_dic = {"uno":"verde", "dos":"azul", "tres": "rojo"}
mi_dic = defaultdict(lambda: "nada",mi_dic)
print(mi_dic["cuatro"])
print(mi_dic)
