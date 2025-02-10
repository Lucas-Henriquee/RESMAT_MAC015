# 📘 Análise Computacional de Estruturas em Resistência dos Materiais

## 🎯 Resumo

Este projeto visa implementar rotinas computacionais para resolver problemas clássicos de **Resistência dos Materiais**, utilizando a linguagem **Python** e bibliotecas como **NumPy**, **Matplotlib**, **SymPy**, **Tkinter** e outras. A abordagem adotada foca no desenvolvimento de métodos computacionais para análise de **forças em vigas e treliças isostáticas**, permitindo cálculos automatizados e visualização gráfica dos resultados.

A disciplina de **Resistência dos Materiais** estuda o comportamento de materiais e estruturas submetidos a forças externas, analisando tensões, deformações e deslocamentos para garantir segurança e eficiência estrutural. O projeto desenvolvido explora esses conceitos através de implementações computacionais que facilitam a solução de problemas estruturais.

O trabalho foi dividido em **4 atividades**, cada uma abordando um aspecto específico da análise estrutural. Abaixo, detalhamos as implementações realizadas.

## 🛠️ Atividade 1 - Análise de Sistemas Mecânicos

1. **Forças Coplanares Concorrentes**
   - **Descrição:** Determina a força resultante a partir de um conjunto de forças concorrentes em um nó.
   - **Parâmetros:** Intensidade e ângulo das forças ou suas componentes cartesianas.
   - **Saída:** Força resultante e direção.

2. **Reações de Apoio em Vigas**
   - **Descrição:** Calcula as reações de apoio em vigas submetidas a cargas pontuais ou distribuídas.
   - **Parâmetros:** Tipo de apoio, posição e magnitude das cargas.
   - **Saída:** Valores das reações de apoio.

3. **Análise de Treliças Planas Isostáticas**
   - **Descrição:** Determina os esforços internos nas barras de uma treliça usando o **Método dos Nós**.
   - **Parâmetros:** Geometria da treliça, tipo de apoio e forças aplicadas.
   - **Saída:** Esforço normal nas barras (tração ou compressão).

📜 **Relatório Completo da Atividade 1:**  
O relatório detalhado desta atividade está disponível aqui:
📄 [Acessar](./activities/Activity_01/docs/Relatorio_Atividade_01.pdf)

## 🏗️ Atividade 2 - Análise Avançada de Vigas e Treliças

1. **Cálculo de Esforços Internos em Vigas**
   - **Descrição:** Calcula os diagramas de **Momento Fletor (M(x))** e **Força Cortante (V(x))** para vigas isostáticas.
   - **Parâmetros:** Tipo de viga, posição dos apoios e carregamentos.
   - **Saída:** Gráficos dos diagramas de esforço.

2. **Deformações em Treliças Planas Isostáticas**
   - **Descrição:** Determina os deslocamentos nodais e o alongamento das barras usando o **Princípio do Trabalho Virtual (PTV)**.
   - **Parâmetros:** Configuração da treliça, propriedades do material e forças aplicadas.
   - **Saída:** Deslocamentos dos nós e deformações nas barras.

📜 **Relatório Completo da Atividade 2:**  
O relatório detalhado desta atividade está disponível aqui:
📄 [Acessar](./activities/Activity_02/docs/Relatorio_Atividade_02.pdf)

## ⚙️ Orientações para Execução

### 📦 Bibliotecas Necessárias

As bibliotecas utilizadas no projeto são:

```
matplotlib
tkintertable
sympy
numpy
pillow
setuptools
```

Você pode instalá-las de duas formas:

- **Instalação via arquivo requirements.txt:**
  ```sh
  pip install -r requirements.txt
  ```
- **Instalação manual:**
  ```sh
  pip install matplotlib tkintertable sympy numpy pillow setuptools
  ```

### 🖥️ Compatibilidade

O programa é compatível com **Windows, Linux e WSL**.

### 🚀 Execução

O programa pode ser executado diretamente pelo Python ou via executável pré-gerado.

#### 🔹 No Windows:
```sh
python main.py
```

#### 🔹 No Linux e WSL:
```sh
python3 main.py
```

### 📂 Executável

O executável gerado pode ser encontrado na pasta [**build**](./build).

Para facilitar a execução, foi gerado um **executável** que pode ser rodado no ambiente Windows sem necessidade de instalar dependências e está localizado na pasta **build**.

#### 🔹 No Windows:
```sh
./Atividades_RESMAT.exe
```

## 👥 Integrantes do Grupo
- **Breno Montanha Costa** - 202265513B  
- **Lucas Henrique Nogueira** - 202265515B  

## 📚 Resistência dos Materiais
**Disciplina:** Resistência dos Materiais (MAC-015) - UFJF  
**Período:** 2024/3  