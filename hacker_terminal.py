import time

def eve_row():
    eve_row = 1
    while eve_row >= 0 :
        if eve_row == 1:
            yield eve_row
            eve_row -= 1
        else :
            yield eve_row
            eve_row +=1
def odd_row():
    odd_row = 0
    while odd_row >= 0 :
        if odd_row == 0:
            yield odd_row
            odd_row += 1
        else :
            yield odd_row
            odd_row -=1

k = eve_row()
l = odd_row()

while True:
    print("{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}{0:5}{1:5}".format(next(k),next(l)))
    time.sleep(0.10)

