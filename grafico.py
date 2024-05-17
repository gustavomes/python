import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x=[]
y=[]

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(',')
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x, y, color = '#787745')
plt.bar(x, y, color = 'k', linestyle = '-')

plt.title('População Brasileira')
plt.xlabel('Ano')
plt.ylabel('População por 100m')
plt.show()