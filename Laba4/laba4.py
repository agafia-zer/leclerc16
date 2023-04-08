import os.path
import numpy as np
import matplotlib.pyplot as plt
def main():
    with open('Laba4/Chisla.conf', 'r') as f:
        k = f.read()
        k = str(k)
        k = k.split(' ')
        a=int(k[0])
        b=int(k[1])
        x=np.linspace(-a,a,b)
        y=np.sin(2*x*np.pi)
        print(y)
        plt.plot(x,y)
        plt.savefig('Laba4/laba44.svg')
        plt.show()
        


file_path = r'Laba4/Chisla.conf'
flag = os.path.isfile(file_path)
 
if flag:
    main()
else:

    print("Файл не найден")
    a,b=input("Введите значения").split(' ')
    k1 = a + ' ' + b
    print(k1)
    with open('Laba4/Chisla.conf','w')as f1:
        f1.write(str(k1))
        f1.close()
        main()
