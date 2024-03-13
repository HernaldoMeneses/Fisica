import matplotlib.pyplot as plt

# Definindo coordenadas X e Y da trajetória
x = [1, 2, 3, 4, 5]  # coordenadas X
y = [2, 3, 4, 3, 2]  # coordenadas Y

# Criando o gráfico
plt.figure(figsize=(8, 6))  # Definindo o tamanho da figura

# Plotando a trajetória
plt.plot(x, y, marker='o', linestyle='-')

# Adicionando rótulos e título
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Trajetória de um Ponto')

# Exibindo o gráfico
plt.grid(True)  # Habilitando as grades
plt.show()

#####Fim da Figura 1
import numpy as np
#import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Definindo coordenadas X e Y da trajetória
x = np.array([1, 2, 3, 4, 5])  # coordenadas X
y = np.array([2, 3, 4, 3, 2])  # coordenadas Y

# Interpolação dos pontos para ajustar uma curva suave
interp_func = interp1d(x, y, kind='cubic')

# Gerando mais pontos ao longo da curva
x_interp = np.linspace(x.min(), x.max(), 100)
y_interp = interp_func(x_interp)

# Criando o gráfico
plt.figure(figsize=(8, 6))  # Definindo o tamanho da figura

# Plotando a trajetória suavizada
plt.plot(x_interp, y_interp, label='Trajetória suavizada', color='blue')

# Plotando os pontos originais
plt.scatter(x, y, color='red', label='Pontos originais')

# Adicionando rótulos e título
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Trajetória de um Ponto com Curvas')

# Adicionando uma legenda
plt.legend()

# Exibindo o gráfico
plt.grid(True)  # Habilitando as grades
plt.show()
