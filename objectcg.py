import numpy as np


class ObjectCG:

    #importar o numphy e criar as estruturas de dados dos objetos (vertices, arestas, ...)
    #os objetos terao numero diferentes de vertices dependendo da forma

    def __init__(self, vertices):
        self.vertices = vertices

    def get_vertices(self):
        return self.vertices

    def set_vertices(self, vertices):
        self.vertices = vertices