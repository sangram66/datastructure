'''
Excel Column Number
Easy
30


In excel sheets there are multiple rows and columns. The rows are numbered like 1, 2, 3…

The columns are numbered like A, B, C,…X, Y, Z, AA, AB,...AY, AZ, BA,...ZY, ZZ, AAA, AAB,...

Here the column numbers denote the following:

A => 1

B => 2

C => 3

.

.

.

X => 24

Y => 25

Z => 26

.

.

Given an excel column number, find the numerical column number.

Examples
Z => 26

AA => 27

ABCA => 19007

Testing

Input Format
First-line contains ‘T’ denoting the number of test cases.

For each test-case, one line containing a string denoting the column number.

Output format
For each test-cases, print a number denoting excel column number.

Examples

Sample Input
2
Z
ABCA
Expected Output
26
19007
Sample Input
2
ABC
AAB
Expected Output
731
704
Constraints

1 <= t <= 1000

1 <= Length of column name <= 6

Note: Column names will be in uppercase English letters.



'''
def excel_column_number(column_name: str) -> int:
    result = 0
    for char in column_name:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

# Reading input
t = int(input())
for _ in range(t):
    column_name = input().strip()
    print(excel_column_number(column_name))



