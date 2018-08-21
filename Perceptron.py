# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

class perceptron(object):
    
    def __init__(self, taxa_aprendizado = 0.4, w=[0.4, -0.6, 0.6], bias=1,limiar=0.5):
        self.taxa_aprendizado = taxa_aprendizado
        self.w = w
        self.bias = bias
        self.limiar = limiar
    def atualizar_pesos(self, xi, yi, u):
        for i in range(len(self.w)):
            self.w[i] += self.taxa_aprendizado*xi[i]*(yi - u)
            
        self.limiar += self.taxa_aprendizado*(-1)*(yi - u)
    def treinar_rede(self, x_treino, y_treino):
        for xi,yi in zip(x_treino,y_treino):
            m = np.multiply(xi,self.w) 
            u = np.sum(m) - self.limiar
            if u != yi:
                self.atualizar_pesos(xi,yi,u)
    def previsao(self, x_teste):
        m = np.multiply(x_teste,self.w)
        u = np.sum(m) - self.limiar
        if u< 0:
            return -1
        else:
            return 1

if __name__ == '__main__':    
    
    x_treino = [[0,0,1], [1,1,0]]
    y_treino = [-1,1]
    
    x_teste=[0,1,1]
    
    # usa perceptron para separar os dados	
    clf = perceptron(taxa_aprendizado = 0.4,limiar=0.5)
    clf.treinar_rede(x_treino,y_treino)
    y_prev = clf.previsao(x_teste)
    
    print(y_prev)