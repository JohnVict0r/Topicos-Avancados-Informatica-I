#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: john
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#Leitura dos dados
empregados = pd.read_csv("datasets/Salary_Data.csv")

#Separação dos dados nas variáveis dependente e independente

empregados_anos_experiencia = empregados['YearsExperience']
empregados_salario = empregados['Salary']

#Separação dos dados em treino e teste (O split padrão é 0.25)

treino, teste, treino_marcacoes, teste_marcacoes =  train_test_split(empregados_anos_experiencia, empregados_salario)

print("x_treino:")
print(treino)
print("x_teste:")
print(teste)

print("y_treino:")
print(treino_marcacoes)
print("y_teste:")
print(teste_marcacoes)

"""
Reorganização dos dados
    Precisamos transformar o nosso vetor de treino em um vetor coluna e, para isso, utilizamos a função reshape e array do numpy
    Passando o primeiro parâmetro como o numero do nosso array e o segundo o numero de colunas (no caso é 1)
"""
treino = np.array(treino).reshape(len(treino), 1)
teste = np.array(teste).reshape(len(teste), 1)

#Criação do modelo

modelo = LinearRegression()
modelo.fit(treino,treino_marcacoes)

#prevendo o salario dos trabalhadores teste
teste_pred=modelo.predict(teste)
teste_pred = np.array(teste_pred).reshape(len(teste_pred), 1)

modelo.score(treino,treino_marcacoes)
modelo.score(teste,teste_marcacoes)



# The coefficients
print('Coefficients: \n', modelo.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(teste_marcacoes, teste_pred))
# Explained variance score: 1 is perfect prediction
variancia=100*r2_score(teste_marcacoes, teste_pred)
print('Variance score: %.2f%%' % variancia)



# Plot outputs
plt.scatter(teste, teste_marcacoes, color='black')
plt.plot(teste, teste_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()


