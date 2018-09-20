class linear(object):
    
    def __init__(self, W):
        self.W = W # [L1, L2]
    
    def forward(self, z_in):
        self.z_in = z_in # [N, L1] # cache
        self.z_out = np.dot(z_in, self.W) # [N, L2]
        return self.z_out
    
    def backward(self, d_in):
        # d_in [N, L2]
        self.dW = self.z_in.T.dot(d_in) / d_in.shape[0] # [L1, L2]
        self.d_out = d_in.dot(self.W.T) # [N, L1]
        return self.d_out

class sqrerror(object):
    
    def __init__(self, y):
        self.y = y # [N, C]
        
    def forward(self, z_in):
        self.z_in = z_in # [N, C]
        self.z_out = np.mean(np.square(z_in - self.y), axis=0, keepdims=True) #[1, C]
        return self.z_out # [N, C]
    
    def backward(self):
        self.d_out = -1 * (self.y - self.z_in) #[100, C]
        return self.d_out

class linear_regr(object):
    
    def __init__(self, learning_rate=0.0001, training_iters=100):
        # define os hiper-parâmetros
        self.learning_rate = learning_rate 
        self.training_iters = training_iters

    def fit(self, X_train, y_train, plot=False):
        
        # formata os dados
        if len(X_train.values.shape) < 2:
            X_train = X_train.values.reshape(-1,1)
        X = np.insert(X_train, 0, 1, 1)
        
        # inicia os parâmetros
        self.w_hat = np.random.normal(0, 1, size = (2,1))
        
        # constroi a arquitetura do modelo
        self.linear_layer = linear(self.w_hat) # camada linear
        self.loss = sqrerror(y_train) # camada de custo
        
        # loop de treino
        for _ in range(self.training_iters):
            
            # forward pass
            z2 = self.linear_layer.forward(X)
            self.loss.forward(z2)
            
            # backward pass
            d2 = self.loss.backward()
            self.linear_layer.backward(d2)
            
            # acha o gradiente
            gradient = self.linear_layer.dW
            gradient *= self.learning_rate # multiplica o gradiente pela taxa de aprendizado
            # atualiza os parâmetros
            self.w_hat -= gradient

    def predict(self, X_test):
        # formata os dados
        if len(X_test.values.shape) < 2:
            X = X_test.values.reshape(-1,1)
        X = np.insert(X, 0, 1, 1)
        
        return np.dot(X, self.w_hat) 
    
    




import pandas as pd
import numpy as np
np.random.seed(0)
from matplotlib import pyplot as plt

dados = pd.DataFrame()
dados['x'] = np.linspace(-10,10,100)
dados['y'] = 5 + 3*dados['x'] + np.random.normal(0,3,100)

regr = linear_regr(learning_rate=0.05, training_iters=100)
regr.fit(dados['x'], dados['y'].reshape(-1,1))
regr.w_hat