# gauss-jordan
Implementation of Gauss-Jordan Elimination in Python.

The required packages:
* numpy
* fractions
* pandas
* copy
* os
* sys

The program expects a parameter which indicates the root folder that contains all the input files. In our case, the command was:

```
python gauss-jordan.py ./input
```

Shortly, the program performs gaussian elimination and prints the solution for three cases, which include unique solution, arbitrary solution and inconsistent problem.
At the beginning, the program starts iterating over the files in the given folder one by one. Then, the input file is read, and the matrix is stored in a 2D numpy array with each number represented as a Fraction. Then, the gauss_jordan method is performed on the matrix. The iteration starts from the element in the first row and the first column. During iteration, we check if the element is a non-zero pivot. If it is, then, we divide the row by the pivot and also make the entries above and below the pivot zero. And repeat the same steps after incrementing the row and column counters. Otherwise, if the entry is zero, we try to find a non-zero entry in the rows below. If such a row is found, the rows are swapped. However, if it is not found, we move to the next column without changing the row number and repeat the steps. Once the row reduced form of the matrix is obtained we check if it is an inconsistent problem or if it has infinitely many solutions. The problem is inconsistent if the entries in the row are zero except for the last one. And the problem has infinitely many solutions if the matrix has zero rows. And the arbitrary variables are the ones that have all zeros in the column. 

For finding the inverse matrix, we perform gauss_jordan elimination on the augmented matrix.

The output for the given input dataset is displayed. First, the name of the input file is printed. Then the output.(Floats have 2 digits after decimal point) Each input file is separated by a dashed line. For more detailed description, the comments are included in the source code.
