'''
Count the minimum moves required to get from src to dest for a knight(Chess board)
'''
Table = [   [0, 3, 2, 3, 2, 3, 4, 5],
            [3, 2, 1, 2, 3, 4, 3, 4],
            [2, 1, 4, 3, 2, 5, 4, 5],
            [3, 2, 3, 2, 3, 4, 3, 4],
            [2, 3, 2, 3, 4, 3, 4, 5],
            [3, 4, 5, 4, 3, 4, 5, 4],
            [4, 3, 4, 3, 4, 5, 4, 5],
            [5, 4, 5, 4, 5, 4, 5, 6] ]

def answer(src, dest):
    return Table[int(abs(src/8 - dest/8))][int(abs(src%8 - dest%8))]

if __name__ == "__main__":
    print(answer(23, 40))
    print(answer(19, 36))
    print(answer(0, 1))