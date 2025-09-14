# src/metrics_calculator.py

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np # Necessário para lidar com arrays de previsões/rótulos


def calcular_sensibilidade(vp: int, fn: int) -> float:
    """
    Calcula a Sensibilidade (Recall) de um modelo.
    Formula: VP / (VP + FN)

    Argumentos:
        vp (int): Verdadeiros Positivos.
        fn (int): Falsos Negativos.

    Retorna:
        float: O valor da sensibilidade.
    """
    if (vp + fn) == 0:
        return 0.0  # Evita divisão por zero
    return vp / (vp + fn)

def calcular_especificidade(vn: int, fp: int) -> float:
    """
    Calcula a Especificidade de um modelo.
    Formula: VN / (VN + FP)

    Argumentos:
        vn (int): Verdadeiros Negativos.
        fp (int): Falsos Positivos.

    Retorna:
        float: O valor da especificidade.
    """
    if (vn + fp) == 0:
        return 0.0  # Evita divisão por zero
    return vn / (vn + fp)

def calcular_acuracia(vp: int, fn: int, fp: int, vn: int) -> float:
    """
    Calcula a Acurácia de um modelo.
    Formula: (VP + VN) / (VP + FN + FP + VN)

    Argumentos:
        vp (int): Verdadeiros Positivos.
        fn (int): Falsos Negativos.
        fp (int): Falsos Positivos.
        vn (int): Verdadeiros Negativos.

    Retorna:
        float: O valor da acurácia.
    """
    total = vp + fn + fp + vn
    if total == 0:
        return 0.0  # Evita divisão por zero
    return (vp + vn) / total

def calcular_precisao(vp: int, fp: int) -> float:
    """
    Calcula a Precisão de um modelo.
    Formula: VP / (VP + FP)

    Argumentos:
        vp (int): Verdadeiros Positivos.
        fp (int): Falsos Positivos.

    Retorna:
        float: O valor da precisão.
    """
    if (vp + fp) == 0:
        return 0.0  # Evita divisão por zero
    return vp / (vp + fp)

def calcular_fscore(precisao: float, sensibilidade: float) -> float:
    """
    Calcula o F-score (F1-score) de um modelo.
    Formula: 2 * (Precisão * Sensibilidade) / (Precisão + Sensibilidade)

    Argumentos:
        precisao (float): O valor da precisão.
        sensibilidade (float): O valor da sensibilidade.

    Retorna:
        float: O valor do F-score.
    """
    if (precisao + sensibilidade) == 0:
        return 0.0  # Evita divisão por zero
    return 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

if __name__ == '__main__':
    # Exemplo de uso básico direto do arquivo (para testes rápidos)
    print("Testando as funções de métricas diretamente:")
    vp_exemplo, fn_exemplo, fp_exemplo, vn_exemplo = 80, 20, 10, 90

    sens = calcular_sensibilidade(vp_exemplo, fn_exemplo)
    esp = calcular_especificidade(vn_exemplo, fp_exemplo)
    acur = calcular_acuracia(vp_exemplo, fn_exemplo, fp_exemplo, vn_exemplo)
    prec = calcular_precisao(vp_exemplo, fp_exemplo)
    f1 = calcular_fscore(prec, sens)

    print(f"Matriz de Confusão: VP={vp_exemplo}, FN={fn_exemplo}, FP={fp_exemplo}, VN={vn_exemplo}")
    print(f"Sensibilidade: {sens:.4f}")
    print(f"Especificidade: {esp:.4f}")
    print(f"Acurácia: {acur:.4f}")
    print(f"Precisão: {prec:.4f}")
    print(f"F-score: {f1:.4f}")


# ... (código existente das outras funções) ...

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np # Necessário para lidar com arrays de previsões/rótulos

def plotar_metricas_principais(vp: int, fn: int, fp: int, vn: int):
    """
    Plota um gráfico de barras comparando Sensibilidade, Especificidade, Acurácia, Precisão e F-score.

    Argumentos:
        vp, fn, fp, vn (int): Valores da matriz de confusão.
    """
    sensibilidade = calcular_sensibilidade(vp, fn)
    especificidade = calcular_especificidade(vn, fp)
    acuracia = calcular_acuracia(vp, fn, fp, vn)
    precisao = calcular_precisao(vp, fp)
    f1 = calcular_fscore(precisao, sensibilidade)

    metricas = ['Sensibilidade', 'Especificidade', 'Acurácia', 'Precisão', 'F-score']
    valores = [sensibilidade, especificidade, acuracia, precisao, f1]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=metricas, y=valores, palette='viridis')
    plt.title('Comparativo das Principais Métricas de Avaliação')
    plt.ylabel('Valor')
    plt.ylim(0, 1) # Métricas de 0 a 1
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plotar_matriz_confusao(vp: int, fn: int, fp: int, vn: int, classes: list = ['Negativo', 'Positivo']):
    """
    Plota a matriz de confusão como um heatmap.

    Argumentos:
        vp, fn, fp, vn (int): Valores da matriz de confusão.
        classes (list): Nomes das classes (ex: ['Não-Fraude', 'Fraude']).
    """
    matriz = np.array([[vn, fp], [fn, vp]]) # Ordem: VN, FP, FN, VP para sklearn-like confusion_matrix
    plt.figure(figsize=(7, 5))
    sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues',
                xticklabels=[f'Previsto {c}' for c in classes],
                yticklabels=[f'Real {c}' for c in classes])
    plt.title('Matriz de Confusão')
    plt.xlabel('Previsão')
    plt.ylabel('Valor Real')
    plt.show()

# ---
# Você precisará adaptar as chamadas dessas funções no seu main.py ou nos notebooks.
# Por exemplo, em main.py:
# plotar_metricas_principais(vp, fn, fp, vn)
# plotar_matriz_confusao(vp, fn, fp, vn)
# ---

# ... (código existente das outras funções e plotagens) ...

def calcular_mcc(vp: int, fn: int, fp: int, vn: int) -> float:
    """
    Calcula o Matthews Correlation Coefficient (MCC).
    Formula: (VP*VN - FP*FN) / sqrt((VP+FP)*(VP+FN)*(VN+FP)*(VN+FN))

    Argumentos:
        vp, fn, fp, vn (int): Valores da matriz de confusão.

    Retorna:
        float: O valor do MCC.
    """
    num = (vp * vn) - (fp * fn)
    den = np.sqrt(
        (vp + fp) * (vp + fn) * (vn + fp) * (vn + fn)
    )

    if den == 0:
        return 0.0 # Evita divisão por zero
    return num / den

def calcular_auc_roc_exemplo(sensibilidade: float, especificidade: float) -> float:
    """
    Calcula um valor de exemplo para AUC-ROC.
    Em um cenário real, isso seria calculado a partir das probabilidades.
    Esta é uma aproximação muito simplificada para fins de demonstração.
    Uma forma comum de aproximar é usando a relação com a precisão e recall.
    Para fins deste exemplo, vamos usar uma fórmula que tenta capturar a ideia,
    mas lembre-se que a forma correta envolve curvas e integrais.

    Uma maneira de pensar é que AUC é a probabilidade de que um exemplo positivo
    aleatório tenha uma pontuação maior que um exemplo negativo aleatório.

    Argumentos:
        sensibilidade (float): Valor de Sensibilidade (Recall).
        especificidade (float): Valor de Especificidade.

    Retorna:
        float: Um valor de exemplo para AUC-ROC.
    """
    # Nota: Esta é uma simplificação grosseira. O cálculo correto envolve
    # curva ROC e o cálculo da área sob ela, que precisa de todas as pontuações de probabilidade.
    # Para fins deste projeto, vamos usar uma aproximação que reflete o quão bem
    # o modelo separa as classes.
    # Se sensibilidade = 1 e especificidade = 1, AUC = 1.
    # Se uma delas for 0, AUC é menor.
    # Uma fórmula comum para aproximar (em cenários binários simples) pode ser:
    # (Sensibilidade + Especificidade) / 2, mas isso não é estritamente correto.
    # Vamos usar uma aproximação mais comum baseada em como a precisão e recall afetam a separação.
    # Se tivermos um modelo que é bom em distinguir, tanto a sensibilidade quanto (1-especificidade) são baixos.
    # Uma métrica mais apropriada para *aproximar* AUC usando métricas únicas é a média ponderada
    # de sensibilidade e especificidade, ou simplesmente usar MCC como um proxy.

    # Para este projeto, vamos calcular de forma simples:
    # Consideramos que quanto mais alta a sensibilidade E a especificidade, mais perto de 1 é a AUC.
    # Uma maneira comum de ter um *único número* que relaciona sensibilidade e especificidade
    # para aproximação é usando a precisão (que já combina VP e FP) e o recall (sensibilidade).
    # Ou, como uma aproximação simples:
    # AUC ~ (Sensibilidade + Especificidade) / 2 se os dados forem balanceados.
    # Se quisermos algo que funcione bem com a matriz, podemos usar MCC como um proxy.

    # Vamos usar o MCC como um indicador de quão bem as classes são separadas.
    # Para este exemplo, vamos apenas *retornar um valor calculado* de uma forma que
    # ilustre a ideia, embora não seja o método rigoroso de cálculo de AUC.

    # Em um cenário real, você precisaria de `y_true` e `y_pred_proba`.
    # Como não temos isso, vamos usar um valor simulado que se alinha com a qualidade das nossas métricas.
    # Por exemplo, se todas as métricas são perfeitas (1.0), AUC seria ~1.0.
    # Se as métricas são baixas, AUC seria menor.
    
    # Um proxy simples, mas não o cálculo formal:
    # MCC já é uma boa métrica que considera todos os 4 elementos.
    # Se quisermos *simular* um valor de AUC baseado em nossas métricas calculadas:
    # Precisão e Sensibilidade são boas para isso.
    # `sklearn.metrics.roc_auc_score` é a função correta, mas requer probabilidades.
    
    # Para demonstrar o conceito, vamos retornar um valor que reflete a "bondade" geral.
    # Um modelo ideal teria sensibilidade e especificidade de 1.
    # Vamos usar uma aproximação que considera ambos:
    
    # Para este exemplo, vamos apenas usar uma aproximação simples que funciona com os valores calculados:
    # Esta é uma forma *muito simplificada* e não a maneira formal de calcular AUC.
    # A forma correta de calcular AUC envolve as probabilidades previstas.
    
    # Se sensibilidade e especificidade são 1, AUC é 1.
    # Se uma delas é 0, AUC é <= 0.5.
    
    # Aproximação: (sensibilidade + especificidade) / 2 é uma heurística comum.
    # Ou, para um valor mais ligado à correlação:
    auc_aprox = (sensibilidade + especificidade) / 2
    
    # Em um projeto real, você usaria:
    # from sklearn.metrics import roc_auc_score
    # auc = roc_auc_score(y_true, y_pred_proba)
    
    return auc_aprox

# ---
# Você precisará adicionar essas novas funções e suas chamadas.
# ---



