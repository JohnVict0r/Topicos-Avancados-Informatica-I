# -*- coding: utf-8 -*-
"""
@AUTOR 
    John Victor - ECT - UFRN - 2018
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
        
        
    def ativacao_sinal(self, u):
        if u>= 0:
            return 1
        else:
            return -1
        
    def atualizar_pesos(self, xi, yi, u):
        
        print("atualizando...")       
        for i in range(len(self.w)):
            self.w[i] += self.taxa_aprendizado*xi[i]*(yi-u)
        self.limiar += self.taxa_aprendizado*(-1)*(yi - u)
        
        print("vetor de pesos atualizado = %s \nlimiar = %s" % (self.w, self.limiar))
        
    def treinar_rede(self, x_treino, y_treino):
        for xi,yi in zip(x_treino,y_treino):
          
            #multiplicar o vetor de caracteristicas(X) pelo vetor de pesos(W)
            m = np.inner(xi,self.w)            
            u = np.sum(m) - self.limiar
            
            #encontrar o valor gerado pela função de ativação
            y=self.ativacao_sinal(u)
            
            #verificar se o valor desejado é igual ao valor gerado pela rede
            if (y-yi) != 0:
                
                #senao for igual, a rede deve atualizar os pesos para tentar se adaptar ao formato dos dados, ou padrão...
                self.atualizar_pesos(xi,yi,y)
        
    def previsao(self, x_teste):
        m = np.multiply(x_teste,self.w)
        u = np.sum(m) - self.limiar
        
        return self.ativacao_sinal(u)


if __name__ == '__main__':    
    
    x_treino = [[0,0,1], [1,1,0]]
    y_treino = [-1,1]
    
    x1=[1,1,1]
    x2=[0,0,0]
    x3=[1,0,0]
    x4=[0,1,1]
    
            
    clf = perceptron(taxa_aprendizado = 0.4,limiar=0.5)
    clf.treinar_rede(x_treino,y_treino)
    
    y1 = clf.previsao(x1)
    y2 = clf.previsao(x2)
    y3 = clf.previsao(x3)
    y4 = clf.previsao(x4)
    
    print(y1,y2,y3,y4)
    