## Cálculo de Métricas de Avaliação de Aprendizado.

![bairesDev](https://github.com/user-attachments/assets/148b3cd0-37e3-4f86-91c8-be3b0e7804fc)



**Bootcamp BairesDev - Machine Learning Training.**

---

**Descrição:**

Neste projeto, vamos calcular as principais métricas para avaliação de modelos de classificação de dados, como acurácia, sensibilidade (recall), especificidade, precisão e F-score. Para que seja possível implementar estas funções, você deve utilizar os métodos e suas fórmulas correspondentes (Tabela 1).

<img width="794" height="1123" alt="BairesDev001" src="https://github.com/user-attachments/assets/f0ec3628-c2be-4af7-be28-805d93f26a96" />

Para a leitura dos valores de VP, VN, FP e FN, será necessário escolher uma matriz de confusão para a base dos cálculos. Essa matriz você pode escolher de forma arbitraria, pois nosso objetivo é entender como funciona cada métrica.  

---

# Cálculo de Métricas de Avaliação de Aprendizado

Este projeto tem como objetivo demonstrar o cálculo de métricas fundamentais para a avaliação de modelos de classificação em Machine Learning. Serão implementadas funções em Python para calcular:

* **Sensibilidade (Recall)**
* **Especificidade**
* **Acurácia**
* **Precisão**
* **F-score (F1-score)**
* **Matthews Correlation Coefficient (MCC)**
* **AUC-ROC (Valor de Exemplo)**

---

## Descrição do Projeto

Neste projeto, calculamos as principais métricas para avaliar modelos de classificação de dados. Para isso, utilizamos os valores de Verdadeiros Positivos (VP), Falsos Negativos (FN), Falsos Positivos (FP) e Verdadeiros Negativos (VN), oriundos de uma matriz de confusão.

### Tabela 1: Visão Geral das Métricas

| Métrica         | Fórmula                                                                   | Descrição                                                                                                    |
| :-------------- | :------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- |
| **Sensibilidade** | $\frac{VP}{VP + FN}$                                                      | Proporção de positivos reais que foram corretamente identificados.                                           |
| **Especificidade**| $\frac{VN}{VN + FP}$                                                      | Proporção de negativos reais que foram corretamente identificados.                                           |
| **Acurácia** | $\frac{VP + VN}{VP + FN + FP + VN}$                                       | Proporção total de previsões corretas em relação ao número total de instâncias.                            |
| **Precisão** | $\frac{VP}{VP + FP}$                                                      | Proporção de previsões positivas que foram de fato corretas.                                                |
| **F-score** | $2 \times \frac{Precisão \times Sensibilidade}{Precisão + Sensibilidade}$ | Média harmônica da precisão e sensibilidade, útil para balancear ambas e em datasets desbalanceados. |
| **MCC** | $\frac{(VP \times VN) - (FP \times FN)}{\sqrt{(VP+FP)(VP+FN)(VN+FP)(VN+FN)}}$ | Coeficiente de correlação que considera todos os valores da matriz de confusão, robusto em datasets desbalanceados. |
| **AUC-ROC** | *Aproximação* | Mede a capacidade do modelo de distinguir entre classes. **Nota:** Aqui usamos uma aproximação simples. |

**Legenda:**
* **VP:** Verdadeiros Positivos
* **FN:** Falsos Negativos
* **FP:** Falsos Positivos
* **VN:** Verdadeiros Negativos

---

## Estrutura do Projeto

O projeto está organizado da seguinte forma:


<img width="961" height="950" alt="Screenshot_20250914-153932" src="https://github.com/user-attachments/assets/24de6c60-1600-4eea-a7b9-b03c72a65002" />

---

## Como Executar o Projeto

Para rodar este projeto localmente, siga os passos abaixo:

### 1. Preparação do Ambiente

1.  **Clone o Repositório:**
    Primeiro, clone o repositório do GitHub para sua máquina local:
    ```bash
    git clone [https://github.com/Santosdevbjj/calculoMetricasML.git](https://github.com/Santosdevbjj/calculoMetricasML.git)
    cd calculoMetricasML
    ```

2.  **Crie e Ative um Ambiente Virtual:**
    É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.
    * **Crie o ambiente:**
        ```bash
        python -m venv venv
        ```
    * **Ative o ambiente:**
        * **Linux/macOS:**
            ```bash
            source venv/bin/activate
            ```
        * **Windows (CMD):**
            ```bat
            venv\Scripts\activate.bat
            ```
        * **Windows (PowerShell):**
            ```powershell
            venv\Scripts\Activate.ps1
            ```
            *(Pode ser necessário ajustar a política de execução do PowerShell se encontrar erros. Execute `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` como administrador, se necessário).*

3.  **Instale Dependências:**
    Para executar os notebooks Jupyter e as visualizações, você precisará instalar algumas bibliotecas:
    ```bash
    pip install matplotlib seaborn jupyter numpy
    ```
    *(O `numpy` já é usado internamente pelas funções de métrica, mas adicioná-lo aqui garante que ele esteja disponível.)*

### 2. Executando o Projeto

Com o ambiente virtual ativado, você pode:

1.  **Executar o Script Principal:**
    O script `main.py` calcula, imprime as métricas e gera as visualizações (gráfico de barras e matriz de confusão).
    ```bash
    python main.py
    ```

2.  **Explorar os Notebooks:**
    Para uma compreensão mais interativa, abra os notebooks Jupyter:
    * Abra o terminal na pasta raiz do projeto (`calculoMetricasML/`).
    * Execute `jupyter notebook` (ou `jupyter lab`).
    * Navegue pela interface do Jupyter para abrir os arquivos `01_Matriz_Confusao.ipynb` e `02_Exemplo_Calculo.ipynb`.

3.  **Executar os Testes Unitários:**
    Para verificar a correção das suas implementações, rode os testes. Isso é crucial para garantir que as funções se comportam como esperado.
    ```bash
    python -m unittest discover tests
    ```

---

## Contribuição

Este projeto é um exemplo educacional focado em demonstrar o cálculo e a visualização de métricas de avaliação de modelos de classificação.

Se você tiver sugestões de melhoria, novas métricas para adicionar, ou encontrar algum bug, sinta-se à vontade para:
* Abrir uma **Issue** no GitHub para discutir sua ideia ou reportar um problema.
* Enviar um **Pull Request** com suas contribuições.

--- 






