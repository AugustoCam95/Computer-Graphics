import np as np
import numpy as np
import math as mh

matricula = '388112'
#matricula = '370019'
#matricula = '391941'
#matricula = '353003'

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
P4 = P1 + np.array([L/2, ((L*(mh.sqrt(3)))/6) ,((L*(mh.sqrt(6)))/6)])

print("P1: {:.2f} {:.2f} {:.2f} ".format(P1[0],P1[1],P1[2]))
print("P2: {:.2f} {:.2f} {:.2f} ".format(P2[0],P2[1],P2[2]))
print("P3: {:.2f} {:.2f} {:.2f} ".format(P3[0],P3[1],P3[2]))
print("P4: {:.2f} {:.2f} {:.2f} ".format(P4[0],P4[1],P4[2]))
print("\n")


LAt = P4-np.array([0,0,((L*(mh.sqrt(6)))/6)])
Eye = np.array([A-5,B+L,(L*(mh.sqrt(6)))/6])
'avup = (LAt)+(0,0,10.2)'
avup = P4

print("Avup:{}".format(avup))
print("LAt:{}".format(LAt))
print("Eye:{}".format(Eye))
print("\n")


k = Eye - LAt
kc = (k / np.linalg.norm(k))
vup = avup - Eye
print("VUP:")
print(vup)
print("\n")
i = np.cross(vup, kc)
print("Izao")
print(i)
ic = (i / np.linalg.norm(i))
jc = np.cross(kc, ic)

print("KC:")
print(kc)
print("IC:")
print(ic)
print("JC:")
print(jc)
print("\n")

icw = np.append(ic, 0)
jcw = np.append(jc, 0)
kcw = np.append(kc, 0)
eyecw = np.append(Eye, 1)
camera_world = np.column_stack((icw, jcw, kcw, eyecw))

print("CAMERA->MUNDO")
print(camera_world)

print("\n")

iwc = np.append(ic, -1*(np.dot(ic, Eye[:3])))
jwc = np.append(jc, -1*(np.dot(jc, Eye[:3])))
kwc = np.append(kc, -1*(np.dot(kc, Eye[:3])))
rowIdentity = np.array([0, 0, 0, 1])
world_camera = np.vstack([iwc, jwc, kwc, rowIdentity])

print("MUNDO->CAMERA")
print(world_camera)
print("\n")

P1l = np.append(P1,1)
P2l = np.append(P2,1)
P3l = np.append(P3,1)
P4l = np.append(P4,1)

P1c = world_camera.dot(P1l)[:3]
P2c = world_camera.dot(P2l)[:3]
P3c = world_camera.dot(P3l)[:3]
P4c = world_camera.dot(P4l)[:3 ]

print("\n")
print("P1c:")
print(P1c)
print("\n")
print("P2c:")
print(P2c)
print("\n")
print("P3c:")
print(P3c)
print("\n")
print("P4c:")
print(P4c)
print("\n")

w11 = P4c-P1c
w12 = P3c-P1c
Nzao = np.cross(w11,w12)
n = (Nzao/np.linalg.norm(Nzao))
print("Nzao")
print(Nzao)
print("\n")
print("n normalizado:")
print(n)
print("\n")

pw =np.array([23.5,12.64,4.7,1])
fw =np.array([12,24,46,1])
#pw= np.array([29,11.77,4.2817,1])
#fw= np.array([A+10,B+L,2*L,1])
#pw= np.array([24.5,16.79,-69.97,1])
#fw= np.array([11,31,54,1])
pc = world_camera.dot(pw)[:3]
fc = world_camera.dot(fw)[:3]
print("pc:")
print(pc)
print("fc:")
print(fc)
print("\n")

t = (np.dot(P1c,n)/np.dot(pc,n))
print("t:")
print(t)
print("\n")

pint = t*pc
print("pint:")
print(pint)
print("\n")

lzao =  fc - pint
print("lzao")
print(lzao)
print("\n")
l = (lzao/np.linalg.norm(lzao))
print("l:")
print(l)
print("\n")

vzao = -pint
print("vzao:")
print(vzao)
print("\n")
v = (vzao/np.linalg.norm(vzao))
print("v:")
print(v)
print("\n")

prod_esc = l[0]*n[0] + l[1]*n[1] + l[2]*n[2]
print (n)
print (prod_esc)
r = []
r.append(2*n[0] * prod_esc - l[0])
r.append(2*n[1] * prod_esc - l[1])
r.append(2*n[2] * prod_esc - l[2])
#r = (np.dot(l,n)*(2*n))-l
print("r")
print(r)
