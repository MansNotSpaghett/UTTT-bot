def theWinner(arr):
    y = arr
    if y[0][0]==y[0][1] and y[0][1]==y[0][2] and y[0][0]!=0 and y[0][0]!=3:
        return y[0][0]
    if y[1][0]==y[1][1] and y[1][1]==y[1][2] and y[1][0]!=0 and y[0][0]!=3:
        return y[1][0]
    if y[2][0]==y[2][1] and y[2][1]==y[2][2] and y[2][0]!=0 and y[0][0]!=3:
        return y[2][0]
    if y[0][0]==y[1][0] and y[1][0]==y[2][0] and y[2][0]!=0 and y[0][0]!=3:
        return y[2][0]
    if y[0][1]==y[1][1] and y[1][1]==y[2][1] and y[2][1]!=0 and y[0][0]!=3:
        return y[2][1]
    if y[0][2]==y[1][2] and y[1][2]==y[2][2] and y[2][2]!=0 and y[0][0]!=3:
        return y[2][2]
    if y[0][0]==y[1][1] and y[1][1]==y[2][2] and y[2][2]!=0 and y[0][0]!=3:
        return y[2][2]
    if y[0][2]==y[1][1] and y[1][1]==y[2][0] and y[2][0]!=0 and y[0][0]!=3:
        return y[2][0]
    else:
        return 0
