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
P4 = P1 + np.array([L/2, ((L*(mh.sqrt(3)))/6) ,((L*(mh.sqrt(6)))/6)])

print("P1: {:.2f} {:.2f} {:.2f} ".format(P1[0],P1[1],P1[2]))
print("P2: {:.2f} {:.2f} {:.2f} ".format(P2[0],P2[1],P2[2]))
print("P3: {:.2f} {:.2f} {:.2f} ".format(P3[0],P3[1],P3[2]))
print("P4: {:.2f} {:.2f} {:.2f} ".format(P4[0],P4[1],P4[2]))
print("\n")


LAt = P4-np.array([0,0,((L*(mh.sqrt(6)))/6)])
Eye = np.array([A-5,B+L,(L*(mh.sqrt(6)))/6])
avup = (LAt)+(0,0,1)
'avup = P4'

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
ic = (i / np.linalg.norm(i))
jc = np.cross(kc, ic)

print("KC:")
print(kc)
print("IC:")
print(ic)
print("JC:")
print(jc)

icw = np.append(ic, 0)
jcw = np.append(jc, 0)
kcw = np.append(kc, 0)
eyecw = np.append(Eye, 1)
camera_world = np.column_stack((icw, jcw, kcw, eyecw))

print("CAMERA->MUNDO")
print(camera_world)

print("\n")

iwc = np.append(ic, -np.dot(ic, Eye[:3]))
jwc = np.append(jc, -np.dot(jc, Eye[:3]))
kwc = np.append(kc, -np.dot(kc, Eye[:3]))
rowIdentity = np.array([0, 0, 0, 1])
world_camera = np.vstack([iwc, jwc, kwc, rowIdentity])

print("MUNDO->CAMERA")
print(world_camera)
print("\n")

P1l = np.append(P1,1)
P2l = np.append(P2,1)
P3l = np.append(P3,1)
P4l = np.append(P4,1)

P1w = world_camera.dot(P1l)[:4]
P2w = world_camera.dot(P2l)[:4]
P3w = world_camera.dot(P3l)[:4]
P4w = world_camera.dot(P4l)[:4]

print("\n")
print("P1:")
print(P1w)
print("\n")
print("P2:")
print(P2w)
print("\n")
print("P3:")
print(P3w)
print("\n")
print("P4:")
print(P4w)