import numpy as np
from objectcg import ObjectCG

class Face:
	def __init__(self, point1, point2, point3, color)
		self.point1 = point1
		self.point2 = point2
		self.point3 = point3
		self.color = color


   @property
    def point1(self):
        return self._point1

    @property
    def point2(self):
        return self._point2

    @property
    def point3(self):
        return self._point3

    @property
    def color(self):
		return self._texture

	@property
	def normal(self):
		#LEMBRAR REGRA DA MÃO DIREITA E O SENTIDO ANTI-HORÁRIO
		#Do ponto 1 para o ponto 2
		p1top2 = np.array(_point2-_point1)
		#Do ponto 1 para o ponto 3
		p1top3 = np.array(_point3-_point1)

		#calcula o vetor atraves do produto vetorial
		nzao = np.cross(p1top2,p1top3)
		
		#depois normaliza 
		normal = (nzao/np.linalg.norm(nzao))
		
		#retorna a normal da face
		return normal