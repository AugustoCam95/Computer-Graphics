from objectcg import ObjectCG

import numpy as np
import math

class Transformations:

    # escala sem passar a matriz homogenea
    def scale(self, mh, x, y, z):
        mh[0, 0] = mh[0, 0] * x
        mh[1, 1] = mh[1, 1] * y
        mh[2, 2] = mh[2, 2] * z

        return mh

    def apply_scale(self, obj, mh):
        vertices = obj.get_vertices()

        for v in vertices:
            v[0] = v[0] * mh[0, 0]
            v[1] = v[1] * mh[1, 1]
            v[2] = v[2] * mh[2, 2]

        obj.set_vertices(vertices)

        return obj

    def translation(self, mh, x, y, z):
        mh[0, 3] = mh[0, 3] + x
        mh[1, 3] = mh[1, 3] + y
        mh[2, 3] = mh[2, 3] + z

        return mh

    def apply_translation(self, obj, mh):
        vertices = obj.get_vertices()

        for v in vertices:
            v[0] = v[0] + mh[0, 3]
            v[1] = v[1] + mh[1, 3]
            v[2] = v[2] + mh[2, 3]

        obj.set_vertices(vertices)

        return obj

    '''
    def apply_shearing(self, obj, mh):
        vertices = obj.get_vertices()

        if mh[0, 1] != 0 :
            for v in vertices:
                v[0] = v[0] + mh[0, 1] * v[1]
        elif mh[1, 0] != 0 :
            for v in vertices:
                v[1] = v[1] + mh[1, 0] * v[0]
        if mh[0, 2] != 0 :
            for v in vertices:
                v[2] = v[3] + mh[0, 2] * v[1]
    '''

    def rotation(self, mh,  alpha, axis):

        # convertendo de graus pra radiano
        alpha = math.radians(alpha)

        if axis == 'z' :
            mh[0, 0] = math.cos(alpha)
            mh[0, 1] = math.sin(alpha)
            mh[1, 0] = - math.sin(alpha)
            mh[1, 1] = math.cos(alpha)

        elif axis == 'x' :
            mh[1, 1] = math.cos(alpha)
            mh[1, 2] = math.sin(alpha)
            mh[1, 1] = - math.sin(alpha)
            mh[1, 2] = math.cos(alpha)

        elif axis == 'y' :
            mh[0, 0] = math.cos(alpha)
            mh[0, 2] = math.sin(alpha)
            mh[2, 0] = - math.sin(alpha)
            mh[2, 2] = math.cos(alpha)

        return mh


    def apply_rotation(self, obj, mh):
        vertices = obj.get_vertices()
        mTemp = np.ones((4, 1))

        for v in vertices:
            mTemp[0, 0] = v[0]
            mTemp[1, 0] = v[1]
            mTemp[2, 0] = v[2]

            mTemp = np.dot(mh, mTemp)

            v[0] = mTemp[0, 0]
            v[1] = mTemp[1, 0]
            v[2] = mTemp[2, 0]

        obj.set_vertices(vertices)

        return obj

    def shearing(self, mh, alpha, direction, plane):
        # convertendo de graus pra radiano
        alpha = math.radians(alpha)
        tan = np.tan(alpha)

        if direction == 'x' :
            if plane == 'xy' or plane == 'yx' :
                mh[0, 1] = tan

            elif plane == 'xz' or plane == 'zx' :
                mh[0, 2] = tan

        elif direction == 'y' :
            if plane == 'xy' or plane == 'yx' :
                mh[1, 0] = tan

            elif plane == 'yz' or plane == 'zy' :
                mh[1, 2] = tan

        elif direction == 'z' :
            if plane == 'xz' or plane == 'zx' :
                mh[2, 0] = tan

            elif plane == 'yz' or plane == 'zy' :
                mh[2, 1] = tan

        return mh


    def apply_shearing(self, obj, mh):
        vertices = obj.get_vertices()
        mTemp = np.ones((4, 1))

        for v in vertices:
            mTemp[0, 0] = v[0]
            mTemp[1, 0] = v[1]
            mTemp[2, 0] = v[2]

            mTemp = np.dot(mh, mTemp)

            v[0] = mTemp[0, 0]
            v[1] = mTemp[1, 0]
            v[2] = mTemp[2, 0]

        obj.set_vertices(vertices)

        return obj

    def apply_escambau(self, obj, mh):
        vertices = obj.get_vertices()
        mTemp = np.ones((4, 1))

        for v in vertices:
            mTemp[0, 0] = v[0]
            mTemp[1, 0] = v[1]
            mTemp[2, 0] = v[2]

            mTemp = np.dot(mh, mTemp)

            v[0] = mTemp[0, 0]
            v[1] = mTemp[1, 0]
            v[2] = mTemp[2, 0]

        obj.set_vertices(vertices)

        return obj