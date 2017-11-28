import numpy as np
import math as mh

matricula = '388112'

F,E,D,C,B,A = matricula

F = float(F)
E = float(E)
D = float(D)
C = float(C)
B = float(B)
A = float(A)

L = (A+B+C+D+E+F)

print("Valor de L:{}".format(L))

P1 = np.array([A+10, B+5, 0])
P2 = P1 + np.array([L,0,0])
P3 = P1 + np.array([L/2, ((L*(mh.sqrt(3)))/2),0])
P4 = P1 + np.array([L/2, ((L*(mh.sqrt(3)))/6) ,((L*(mh.sqrt(6)))/6) ])

print("P1: {:.2f} {:.2f} {:.2f}".format(P1[0],P1[1],P1[2]))
print("P2: {:.2f} {:.2f} {:.2f}".format(P2[0],P2[1],P2[2]))
print("P3: {:.2f} {:.2f} {:.2f}".format(P3[0],P3[1],P3[2]))
print("P4: {:.2f} {:.2f} {:.2f}".format(P4[0],P4[1],P4[2]))
print("\n")


LAt = P4-np.array([0,0,((L*(mh.sqrt(6)))/6)])
Eye = np.array([A-5,B+L,(L*(mh.sqrt(6)))/6])
'avup = (LAt)+(0,0,1)'
avup = P4

print("Avup:{}".format(avup))
print("LAt:{}".format(LAt))
print("Eye:{}".format(Eye))
print("\n")

K = Eye - LAt
print("K:{}".format(K))
kbarra = mh.sqrt((K[0])**2+(K[1])**2+(K[2])**2)
print("kbarra:{}".format(kbarra)) 
knorm = [(K[0]/kbarra),(K[1]/kbarra),(K[2]/kbarra)]
print("K normalizado:[{:.2f},{:.2f},{:.2f}]".format(knorm[0],knorm[1],knorm[2]))
print("\n")

vup =  avup - Eye
print("vup:{}".format(vup))
I = np.cross(vup,knorm)
print("I:{}".format(I))
ibarra = mh.sqrt(((I[0])**2)+((I[1])**2)+((I[2])**2))
print("ibarra:{}".format(ibarra)) 
inorm = [(I[0]/ibarra),(I[1]/ibarra),(I[2]/ibarra)]
print("I normalizado:[{:.2f},{:.2f},{:.2f}]".format(inorm[0],inorm[1],inorm[2]))
print("\n")

jnorm = np.cross(knorm,inorm)
print("J normalizado:[{:.2f},{:.2f},{:.2f}]".format(jnorm[0],jnorm[1],jnorm[2]))
print("\n")
'''
print("Matriz c->w:")
Mcw = np.array([inorm[0],jnorm[0],knorm[0],Eye[0]],
		   	    [inorm[1],jnorm[1],knorm[1],Eye[1]],
		   	    [inorm[2],jnorm[2],knorm[2],Eye[2]],
		   	    [[0],[0],[0],[1]])
print(Mcw)
'''
print("\n")
