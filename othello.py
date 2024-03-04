##1

# #8×8の2次元配列を-1で初期化

array_2d = [[-1 for _ in range(8)] for _ in range(8)]
array_2d[3][3] = 0
array_2d[4][4] = 0
array_2d[3][4] = 1
array_2d[4][3] = 1




my_list = [(2,4), (3,5), (4,2), (5,3)]
print(my_list)







def input_number():
    try:
        # 1回目の入力
        num1 = int(input("1から8までの整数を入力してください: "))
        if 1 <= num1 <= 8:
            return num1
        else:
            print("無効な入力です。1から8までの整数を入力してください。")
    except ValueError:
        print("無効な入力です。整数を入力してください。")
        
        
        
        
        
def extract_element(index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range"


X = input_number()

Z = extract_element(X-1)    



# タプルから行と列のインデックスを抽出
row_index, column_index = Z

array_2d[row_index][column_index] = 0





# #配列の要素を読み取り、"-"または"o"を表示

for row in array_2d:
    for element in row:
        if element == -1:
            print("-", end=" ")
        elif element == 0:
            print("o", end=" ")
        else:
            print("x", end=" ")
    print()  # 改行
    


##4
A = ["aiueo", "kaki", "kukeko"]


def input_number():
    try:
        # 1回目の入力
        num1 = int(input("1から8までの整数を入力してください: "))
        if 1 <= num1 <= 8:
            print(f"入力された整数は {num1} です。")
        else:
            print("無効な入力です。1から8までの整数を入力してください。")
    except ValueError:
        print("無効な入力です。整数を入力してください。")
        