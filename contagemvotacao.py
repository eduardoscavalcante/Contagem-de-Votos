import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_excel('/content/VOTAÇÃO PARA HOMENAGEADOS (respostas).xlsx')

respostas = df['Quem você gostaria que fosse homenageado na formatura da turma? (LIMITE DE 10 OPÇÕES)'].dropna().tolist()

nomes = []
for resposta in respostas:
    nomes.extend([nome.strip() for nome in resposta.split(',')])

contador = Counter(nomes)

contagem_df = pd.DataFrame(contador.items(), columns=['Nome', 'Contagem'])
contagem_df = contagem_df.sort_values(by='Contagem', ascending=False)

# Gráfico pizza do TOP 10
top_10_df = contagem_df.head(10)
plt.figure(figsize=(10, 8))
plt.pie(top_10_df['Contagem'], labels=top_10_df['Nome'], autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Homenageados na Formatura')
plt.show()

# Gráfico de barras geral
plt.figure(figsize=(12, 8))
plt.bar(contagem_df['Nome'], contagem_df['Contagem'], color='skyblue')
plt.xlabel('Nome')
plt.ylabel('Contagem de Votos')
plt.title('Contagem de Votos por Candidato')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Contagem completa
contagem_df.to_excel('contagem_completa.xlsx', index=False)
print("Contagem completa dos candidatos:")
print(contagem_df)
