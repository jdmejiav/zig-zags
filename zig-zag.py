

def read_input(n):
    matrices = []
    for x in range(0,n):
        
        temp_zig = []
        for i in range(0,9):
            temp_zig.append(input().split(" "))
        if x != n-1:
            _ = input()
        print_matrix(temp_zig)
        matrices.append(temp_zig)
    return matrices


def print_matrix (matrix):
    for i in range(len(matrix)):
        if i % 3 == 0 and i!=0:
            print("- - - - - - - - - - - - - - - - -")
        
        for j in range(len(matrix[0])):
            if j %3 == 0 and j!=0:
                print(" | ", end="")
            
            if j==8:
                print(" "+str(matrix[i][j]))
            else:
                print(" "+str(matrix[i][j])+" ", end="")
    print("")

def find_empty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == ".":
                return i,j
    else:
        return False

def check_valid(num,row,col,matrix):

    #Find Zigs
    col_zig = find_row_base_zig(row,col)

    for i in range(len(matrix)):
        if col_zig + i <= 8:
            if matrix[i][col_zig+i] == str(num):   
                return False
        elif matrix[i][i - (9-col_zig)] == str(num):  
            return False
    
     # Find Zags

    col_zag = find_row_base_zag(row,col)

    for i in range(len(matrix)):
        if col_zag-i >= 0:
            if matrix[i][col_zag-i] == str(num):
                return False
        else:
            if matrix[i][col_zag+(9-i)] == str(num):
                return False
    
    # Find squares

    row_range = []
    if row>=0 and row <3:
        row_range = [i for i in range(0,3)]
    elif row>=3 and row<6:
        row_range = [i for i in range(3,6)]
    elif row>=6 and row<9:
        row_range = [i for i in range(6,9)]


    col_range = []
    if col>=0 and col <3:
        col_range = [i for i in range(0,3)]
    elif col>=3 and col<6:
        col_range = [i for i in range(3,6)]
    elif col>=6 and col<9:
        col_range = [i for i in range(6,9)]

    for i in row_range:
        for j in col_range:
            if matrix[i][j] == str(num):
                return False
    return True


def find_row_base_zag(row, col):
    if col + row > 8:
        return 7 - ( 8 - col + 8 - row)
    else:
        return col+row


def find_row_base_zig(row, col):
    if row > col:
        return col + (9-row)
    else:
        return col - row 
        


def solve_zigzag(matrix):
    find = find_empty(matrix)
    if not find:
        return matrix[0][0]
    else:
        row, col = find
    for i in range(0,9):
        if check_valid(i, row, col, matrix):
            matrix[row][col] = i
            if solve_zigzag(matrix) != None:
                return matrix[0][0]
            matrix[row][col] = '.'


if __name__=='__main__':
    sum = 0
    n = int(input())
    matrices = read_input(n)
    for i in matrices:
        sum += solve_zigzag(i)
    print(sum)

