# src/metrics_calculator.py

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
