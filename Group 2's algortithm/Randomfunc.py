import random
def Randomfun():
    out = []

    for i in range(9):
        check = [random.randint(0,10),random.randint(0,10)]
        if check not in out:
            out.append(check)

        else:
            check = [random.randint(0,10),random.randint(0,10)]
            if check not in out:
                out.append(check)
    return(out)