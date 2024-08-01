def create_2d_array(rows, cols):
    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element [{i}][{j}]: "))
            row.append(element)
        array.append(row)
    return array


def multiply_matrices(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    print("Create the first 2D array:")
    rows1 = int(input("Enter the number of rows: "))
    cols1 = int(input("Enter the number of columns: "))
    array1 = create_2d_array(rows1, cols1)

    print("\nCreate the second 2D array:")
    rows2 = int(input("Enter the number of rows: "))
    cols2 = int(input("Enter the number of columns: "))
    if cols1 != rows2:
        print(
            "Error: The number of columns in the first matrix must equal the number of rows in the second matrix for multiplication.")
        return
    array2 = create_2d_array(rows2, cols2)

    print("\nFirst 2D array:")
    print_matrix(array1)

    print("\nSecond 2D array:")
    print_matrix(array2)

    print("\nResult of matrix multiplication:")
    result = multiply_matrices(array1, array2)
    print_matrix(result)


if __name__ == "__main__":
    main()
