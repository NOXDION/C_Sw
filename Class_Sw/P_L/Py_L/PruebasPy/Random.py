import random
bala=random.randint(1,5)
for i in range(1,5):
    input('Presiona enter para disparar')
    if i == bala:
        print('Tomas un shot')
        break


