# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


x = [[0,0,1], [1,1,0]]
y = [-1,1]

class perceptron(object):
    u=0
    def __init__(self, taxa_aprendizado = 0.4, w=[0.4, -0.6, 0.6], bias=1,limiar=0.5):
        self.taxa_aprendizado = taxa_aprendizado
        self.w = w
        self.bias = bias
        self.limiar = limiar
        
        
    def Atualizar_pesos(self, x_treino, y_treino):
        for xi,yi in zip(x_treino,y_treino):
            
            #self.w += self.taxa_aprendizado*xi*(yi - self.u)
            
                
    def treinar_rede(self, x, w):
        
        m = np.multiply(x,w) 
        u = np.sum(m) - limiar
        return u        
