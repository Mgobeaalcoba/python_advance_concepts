import numpy as np

def main():
    lista = [x ** 2 for x in range(10)]
    matriz = [[x * 2 for x in range(10)],[x * 3 for x in range(10)]]
    matriz_np = np.matrix(data=matriz)
    print(lista)
    print(matriz)
    print(matriz_np)
    print()

    # Matriz con list comprehensions
    rows, cols = 3, 3
    matrix = [[x for x in range(cols)] for _ in range(rows)] # Matriz por list comprehensions
    matrix_np = np.array(matrix)
    print(matrix_np)
    print(matrix_np.shape)
    print()

    # Tensor con list comprehensions
    depth, rows, cols = 2, 3, 4
    tensor = [[[x for x in range(cols)] for _ in range(rows)] for _ in range(depth)]
    tensor_np = np.array(tensor)
    print(tensor_np)
    print(tensor_np.shape)
    print()

    print("### Valores Diferentes ###")

    # Matriz con valores diferentes
    rows, cols = 3, 3
    matrix = [[row * col for col in range(1, cols + 1)] for row in range(1, rows + 1)]
    matrix_np2 = np.array(matrix)
    print(matrix_np2)
    print(matrix_np2.shape)
    print()

    # Tensor con valores diferentes
    depth, rows, cols = 3, 5, 4
    tensor = [[[dep * row * col for dep in range(1, depth + 1)] for col in range(1, cols + 1)] for row in range(1, rows + 1)]
    tensor_np2 = np.array(tensor)
    print(tensor_np2)
    print(tensor_np2.shape)
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print(e)
        print("Saliendo...")