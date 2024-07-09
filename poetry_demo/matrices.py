import numpy as np

def main():
    lista = [x ** 2 for x in range(10)]
    matriz = [[x * 2 for x in range(10)],[y * 3 for y in range(10)]]
    matriz_np = np.matrix(data=matriz)
    print(lista)
    print(matriz)
    print(matriz_np)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print(e)
        print("Saliendo...")