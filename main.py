from pygame import *
import time
init()
 #test time

begin = time.time()

a = 0
for i in range(1000):
    a+=1

end = time.time()

print(end-begin)
#test test de booléens
