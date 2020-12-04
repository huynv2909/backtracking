# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def read_input():
    f = open("input.txt", "r")
    lines = f.read().split("\n")

    output = []

    for i in lines:
        output.append(i.split(" "))

    return output


def write_output(a):
    print("Result:")
    for i in a:
        print(*i)


def valid(a, x, y, t):
    for i in a[x]:
        if i == t:
            return False

    for i in a:
        if i[y] == t:
            return False

    for i in range((x//3)*3, (x//3)*3 + 3):
        for j in range((y//3)*3, (y//3)*3 + 3):
            if a[i][j] == t:
                return False

    return True


def sodoku(a, x, y):
    if y == 9:
        if x == 8:
            write_output(a)
            exit()
        else:
            sodoku(a, x + 1, 0)
    elif not a[x][y] == '0':
        sodoku(a, x, y + 1)
    else:
        for i in range(1, 10):
            if valid(a, x, y, str(i)):
                a[x][y] = str(i)
                sodoku(a, x, y + 1)
                a[x][y] = '0'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = read_input()
    sodoku(a, 0, 0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
