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

---

## Descrição do Projeto

Neste projeto, calculamos as principais métricas para avaliar modelos de classificação de dados. Para isso, utilizamos os valores de Verdadeiros Positivos (VP), Falsos Negativos (FN), Falsos Positivos (FP) e Verdadeiros Negativos (VN), oriundos de uma matriz de confusão.

### Tabela 1: Visão Geral das Métricas

| Métrica         | Fórmula                                           | Descrição                                                                                                    |
| :-------------- | :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- |
| **Sensibilidade** | $\frac{VP}{VP + FN}$                               | Proporção de positivos reais que foram corretamente identificados.                                           |
| **Especificidade**| $\frac{VN}{VN + FP}$                               | Proporção de negativos reais que foram corretamente identificados.                                           |
| **Acurácia** | $\frac{VP + VN}{VP + FN + FP + VN}$                | Proporção total de previsões corretas em relação ao número total de instâncias.                            |
| **Precisão** | $\frac{VP}{VP + FP}$                               | Proporção de previsões positivas que foram de fato corretas.                                                |
| **F-score** | $2 \times \frac{Precisão \times Sensibilidade}{Precisão + Sensibilidade}$ | Média harmônica da precisão e sensibilidade, útil para balancear ambas e em datasets desbalanceados. |

**Legenda:**
* **VP:** Verdadeiros Positivos
* **FN:** Falsos Negativos
* **FP:** Falsos Positivos
* **VN:** Verdadeiros Negativos

---

## Estrutura do Projeto

<img width="961" height="950" alt="Screenshot_20250914-153932" src="https://github.com/user-attachments/assets/c1beca83-8381-4b4e-910f-22393218f35c" />


---



