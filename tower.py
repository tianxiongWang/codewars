def tower_builder(n_floors):
    L = [' ' * (-i + n_floors - 1) + '*' * ((2*i) + 1) + ' ' * (-i + n_floors - 1)
         for i in range(n_floors)]
    return L

if __name__ == "__main__":
    print(tower_builder(3))