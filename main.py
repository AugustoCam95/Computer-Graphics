from transformations import Transformations
from objectcg import ObjectCG
from camera import Camera

import numpy as np


def main():
    t = Transformations()

    # criar objeto e sua matriz de vertices
    # cubo
    vertices = np.zeros((8, 3))
    vertices[1] = [1, 0, 0]
    vertices[2] = [1, 1, 0]
    vertices[3] = [0, 1, 0]
    vertices[4] = [0, 0, 1]
    vertices[5] = [1, 0, 1]
    vertices[6] = [1, 1, 1]
    vertices[7] = [0, 1, 1]

    cube = ObjectCG(vertices)

    mh = np.eye(4)
    mh = t.scale(mh, 2, 2, 2)

    # aplicando escala no cubo
    cube = t.apply_scale(cube, mh)

    #print(cube.get_vertices())
    #print("")

    # setando translacao na matriz homogenea
    #mh = t.translation(mh, 3, 3, 3)

    #aplicando translacao no cubo
    #cube = t.apply_translation(cube, mh)

    #print(cube.get_vertices())

    # setando e aplicando rotaçao
    #mh = t.rotation(mh, 30, 'z')
    #cube = t.apply_rotation(cube, mh)



    # 4)Posicionar observador e orientar a camera
    camera = Camera()

    eye = np.array([0, 0, 10])
    lookat = np.array([0, 0, -3])
    avup = np.array([0, 5, -3])

    mWC = camera.find_world_camera(eye, lookat, avup)
    mCW = camera.find_camera_world(eye, lookat, avup)






def menu(obj):
    mh = np.eye(4)
    t = Transformations()

    print("Vertices dados:")
    print(obj.get_vertices())

    op = 0

    while op != -1 :
        print("Escolha uma opção:")
        print("1 - Escala")
        print("2 - Aplicar Escala")
        print("3 - Translacao")
        print("4 - Aplicar Translacao")
        print("5 - Rotacao")
        print("6 - Aplicar Rotacao")
        print("7 - Cisalhamento")
        print("8 - Aplicar Cisalhamento")
        print("")
        print("0 - Sair")

        op = int(input("-> "))

        if op == 1 :
            x = float(input("Qual a escala do eixo x? "))
            y = float(input("Qual a escala do eixo y? "))
            z = float(input("Qual a escala do eixo z? "))

            mh = t.scale(mh, x, y, z)

            print("")
            print("Matriz homogenea resultante:")
            print(mh)

        elif op == 2:
            obj = t.apply_scale(obj, mh)
            mh = np.eye(4)

            print("")
            print("Vertices resultantes:")
            print(obj.get_vertices())

        elif op == 3 :
            x = float(input("Qual a translacao do eixo x? "))
            y = float(input("Qual a translacao do eixo y? "))
            z = float(input("Qual a translacao do eixo z? "))

            mh = t.translation(mh, x, y, z)

            print("")
            print("Matriz homogenea resultante:")
            print(mh)

        elif op == 4:
            obj = t.apply_translation(obj, mh)
            mh = np.eye(4)

            print("")
            print("Vertices resultantes:")
            print(obj.get_vertices())

        elif op == 5 :
            alpha = float(input("Qual o angulo de rotacao? "))
            axis = input("Qual o eixo de rotacao (x, y, z) ? ")

            mh = t.rotation(mh, alpha, axis)

            print("")
            print("Matriz homogenea resultante:")
            print(mh)

        elif op == 6:
            obj = t.apply_rotation(obj, mh)
            mh = np.eye(4)

            print("")
            print("Vertices resultantes:")
            print(obj.get_vertices())

        elif op == 7 :
            alpha = float(input("Qual o angulo de cisalhamento? "))
            direction = input("Qual a direcao do cisalhamento(x, y, z) ? ")
            plane = input("Qual o plano de cisalhamento (xy, xz, yz) ? ")

            mh = t.shearing(mh, alpha, direction, plane)

            print("")
            print("Matriz homogenea resultante:")
            print(mh)

        elif op == 8:
            obj = t.apply_shearing(obj, mh)
            mh = np.eye(4)

            print("")
            print("Vertices resultantes:")
            print(obj.get_vertices())

        elif op == 0 :
            op = -1

main()

# substitua os valores pelos pontos do seu objeto
#vertices = np.zeros((4, 3))

'''
vertices[0] = [5, 2.8867, 4.0324]
vertices[1] = [10, 0, 0]
vertices[2] = [0, 0, 0]
vertices[3] = [5, 8.6602, 0]
'''

#aqui ohh
'''
vertices[0] = [-5.4414, 1.9282, 4.0824]
vertices[1] = [0, 0, 0]
vertices[2] = [-1.0531, 5.6750, 8.1624]
vertices[3] = [-6.4922, 7.6047, 0]

obj = ObjectCG(vertices)
'''

'''
mh = np.zeros((4, 4))
mh[0] = [0.9790, -0.2038, 0, 0]
mh[1] = [0.2038, 0.9790, 0, 0]
mh[2] = [0, 0, 1, 0]
mh[3] = [0, 0, 0, 1]



t = Transformations()

obj = t.apply_rotation(obj, mh)
'''
'''
mh = np.eye(4)
mh = t.translation(mh, 270, 50, 0)
obj = t.apply_translation(obj, mh)
'''
'''
print("")
print("Vertices resultantes:")
print(obj.get_vertices())
'''

#menu(obj)

'''
m1 = np.eye(3)

m2 = np.zeros((3, 1))
m2[0] = [-0.6209]
m2[1] = [-0.5301]
m2[2] = [-0.5773]

m3 = np.zeros((1, 3))
m3[0] = [-0.6209, -0.5301, -0.5773]

mtemp = np.dot(m2, m3)
print(mtemp)

mtemp = 2.0 * mtemp
print(mtemp)

mtemp = m1 - mtemp
print("matriz de espelhamento")
print(mtemp)

p3 = np.zeros((3, 1))
p3[0] = [-9.8320]
p3[1] = [-1.8200]
p3[2] = [0]

mtemp = np.dot(mtemp, p3)

print("Vertices resultantes:")
print(mtemp)
'''