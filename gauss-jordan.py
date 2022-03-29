import numpy as np
from fractions import Fraction
import pandas as pd
import copy
import os
import sys

pd.options.display.float_format = '{:,.2f}'.format
# path to the root folder which contains input files
assert(len(sys.argv) > 1 and sys.argv[1] != "")
root_path = sys.argv[1]


def main(path):
    with open(path, "r") as file:   # open the input file
        n = int(file.readline())
        read = file.read().splitlines()
        # storing input as Fractions in a 2D numpy array
        X = np.array([[Fraction(num) for num in line.split()] for line in read])

    # storing the copy of the matrix X (for inverse operation later)
    initial = copy.deepcopy(X)

    def print_matrix(X):
        # converting Fractions to floats
        array = [[float(frac) for frac in row] for row in X]
        df = pd.DataFrame(array)
        # printing pandas dataframe without indices and column names
        # for better display of the matrices
        print('\n'.join(df.to_string(index=False).split('\n')[1:]))

    def gauss_jordan(X):
        num_of_rows = X.shape[0]
        num_of_cols = X.shape[1]

        i = 0  # row counter
        c = 0  # column counter
        while i < num_of_rows:
            if c >= num_of_cols:
                break
            while c < num_of_cols:
                if X[i, c] != 0:      # selecting nonzero pivot
                    X[i, :] = np.divide(X[i, :], X[i, c])      # dividing the row by the pivot

                    for j in range(num_of_rows): # making the entries of the pivot column zero
                        if i != j:               # except the pivot row
                            X[j, :] -= X[i, :] * X[j, c] / X[i, c]
                else:
                    k = i + 1                                   # if the entry is zero
                    while k < num_of_rows and X[k, c] == 0:     # try to find a non-zero entry in the rows below
                        k += 1

                    if k != num_of_rows:     # if found, swap rows
                        X[[i, k]] = X[[k, i]]
                        break
                    else:
                        c += 1         # if not found move to next column but do not change row.
                        continue

                # increment row and column counter
                i += 1
                c += 1
                break

        return X

    X = gauss_jordan(X)
    found = []
    for t in range(n):
        if np. all((X[t, :-1] == 0)) and X[t, -1] != 0:   # if all entries in a row are zero
            found.append('NS')                            # except the last one
        elif np. all((X[t] == 0)): # if all entries in a row are zero
            found.append('Inf')

    if 'NS' in found:
        print("Inconsistent problem")
    elif 'Inf' in found:
        # converting fractions to float
        arr = np.array([[float(col) for col in row] for row in X])
        # find indices of rows with all zero elements
        indices = np.where(~arr.any(axis=1))[0]
        index_found = []
        values = [0] * (X.shape[1] - 1)
        for ind in range(X.shape[0]):
            if ind not in indices:   # if row contains non-zero elements
                # index of column with entry 1
                index = np.where(arr[ind] == 1)[0][0]
                # storing index of column which was matched with a value
                index_found.append(index)
                # storing the last element of row as value a variable
                values[index] = arr[ind, -1]
        # finding indices of arbitrary variables (that have not been matched previously)
        arbitrary = set(range(X.shape[0])).difference(set(index_found))
        print("Arbitrary variables: " + " ".join([f"x{ind + 1}" for ind in arbitrary]))
        print("Arbitrary solution: " + " ".join([f"{'{:.2f}'.format(num)}" for num in values]))
    else:
        print("Unique solution " + " ".join([f"{'{:.2f}'.format(float(num))}" for num in X[:, -1]]))
        identity = np.identity(n)
        identity = [[Fraction(col) for col in row] for row in identity]
        # horizontally stack identity matrix to matrix A
        matrix = np.hstack((initial[:, :-1], identity))
        # perform gauss_jordan on augmented matrix
        inverse = gauss_jordan(matrix)
        print("Inverted A:")
        print_matrix(inverse[:, n:])


# start of the program
for input_file in os.listdir(root_path):  # iterate over files in the root folder
    input_path = os.path.join(root_path, input_file)  # full path to the input file
    print("Processing input file: " + input_file)
    main(input_path)
    print("-" * 30)
