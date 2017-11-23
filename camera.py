import numpy as np


class Camera:


    def find_kij(self, eye, lookat, avup):
        k = eye - lookat
        kc = (k / np.linalg.norm(k))
        vup = avup - eye
        i = np.cross(vup, kc)
        ic = (i / np.linalg.norm(i))
        jc = np.cross(kc, ic)
        return kc, jc, ic

    def find_camera_world(self, eye, lookat, avup):
        kc, jc, ic = self.find_kij(eye, lookat, avup)
        icw = np.append(ic, 0)
        jcw = np.append(jc, 0)
        kcw = np.append(kc, 0)
        eyecw = np.append(eye, 1)
        camera_world = np.column_stack((icw, jcw, kcw, eyecw))
        return camera_world

    def find_world_camera(self, eye, lookat, avup):
        kc, jc, ic = self.find_kij(eye, lookat, avup)
        iwc = np.append(ic, -np.dot(ic, eye[:3]))
        jwc = np.append(jc, -np.dot(jc, eye[:3]))
        kwc = np.append(kc, -np.dot(kc, eye[:3]))
        rowIdentity = np.array([0, 0, 0, 1])
        world_camera = np.vstack([iwc, jwc, kwc, rowIdentity])
        return world_camera

    def apply_m_camera(self, mWC, objectsList):
        # Percorre os objetos do cenario
        for obj in objectsList:
            vertices = obj.get_vertices()
            mTemp = np.ones((4, 1))

            # Para cada vertice do objeto converte para coordenadas de camera
            for v in vertices:
                mTemp[0, 0] = v[0]
                mTemp[1, 0] = v[1]
                mTemp[2, 0] = v[2]

                mTemp = np.dot(mWC, mTemp)

                v[0] = mTemp[0, 0]
                v[1] = mTemp[1, 0]
                v[2] = mTemp[2, 0]

            obj.set_vertices(vertices)

        return objectsList
