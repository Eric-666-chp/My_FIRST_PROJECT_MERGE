import pyautogui as pg
import time


f = open('make card number.txt','r')

tj = 17
N = f.read(16)
f.seek(tj)
P = f.read(8)

pg.click(x=1590,y=1306)
time.sleep(0.2)
pg.click(x=1548,y=1115)
time.sleep(1)
pg.write('foot locker',interval=0.1)
time.sleep(1)
pg.click(x=1087,y=286)
time.sleep(1)
pg.write(N,interval=0.03)
pg.click(x=1027,y=584)
pg.write(P)
pg.press('enter')
pg.write('200',interval=0.03)
time.sleep(0.5)
pg.click(x=1615,y=106)


tj = tj+27
N = f.read(17)
f.seek(tj)
P = f.read(8)
N = N.strip('\n')

while P.strip() != '':

    time.sleep(2)
    pg.click(x=1590, y=1306)
    time.sleep(0.2)
    pg.click(x=1548,y=1115)
    time.sleep(0.5)
    pg.write('foot locker', interval=0.1)
    time.sleep(1)
    pg.click(x=1087,y=286)
    time.sleep(1)
    pg.write(N, interval=0.03)
    pg.click(x=1027,y=584)
    pg.write(P)
    pg.press('enter')
    pg.write('200', interval=0.1)
    time.sleep(0.5)
    pg.click(x=1615, y=106)

    tj = tj + 27
    N = f.read(17)
    f.seek(tj)
    P = f.read(8)
    N = N.strip('\n')

f.close()
