put = 98


def Func1(put):
    if str(put)[1] == "1" or str(put)[1] == "2" or str(put)[1] == "3":
        return 0
    if str(put)[1] == "4" or str(put)[1] == "5" or str(put)[1] == "6":
        return 1
    if str(put)[1] == "7" or str(put)[1] == "8"or str(put)[1] == "9":
        return 2


def Func2(put):
    if str(put)[1] == "1" or str(put)[1] == "4" or str(put)[1] == "7":
        return 0
    if str(put)[1] == "2" or str(put)[1] == "5" or str(put)[1] == "8":
        return 1
    if str(put)[1] == "3" or str(put)[1] == "6" or str(put)[1] == "9":
        return 2


def FuncU1(put):
    if str(put)[0] == "1" or str(put)[0] == "2" or str(put)[0] == "3":
        return 0
    if str(put)[0] == "4" or str(put)[0] == "5" or str(put)[0] == "6":
        return 1
    if str(put)[0] == "7" or str(put)[0] == "8"or str(put)[0] == "9":
        return 2


def FuncU2(put):
    if str(put)[0] == "1" or str(put)[0] == "4" or str(put)[0] == "7":
        return 0
    if str(put)[0] == "2" or str(put)[0] == "5" or str(put)[0] == "8":
        return 1
    if str(put)[0] == "3" or str(put)[0] == "6" or str(put)[0] == "9":
        return 2
