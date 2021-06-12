import random


def piece_equilibree():
    if random.uniform(0, 1) <= 0.5:
        return 1
    else:
        return -1


def piece_jeu_a():
    if random.uniform(0, 1) <= 0.49:
        return 1
    else:
        return -1


def piece_jeu_b1():
    if random.uniform(0, 1) <= 0.09:
        return 1
    else:
        return -1


def piece_jeu_b2():
    if random.random() <= 0.74:
        return 1
    else:
        return -1


moy = 0

for i in range(10):
    n = 1000000
    gain = 0

    for i in range(n):
        jeu = piece_equilibree()
        if jeu == 1:
            gain += piece_jeu_a()
        else:
            if gain % 3 == 0:
                gain += piece_jeu_b1()
            else:
                gain += piece_jeu_b2()
    moy += gain

print("le gain net est de :", moy / 10, "€")
