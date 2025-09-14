# main.py

from src.metrics_calculator import (
    calcular_sensibilidade,
    calcular_especificidade,
    calcular_acuracia,
    calcular_precisao,
    calcular_fscore,
    calcular_mcc, # Importa nova função
    calcular_auc_roc_exemplo, # Importa nova função
    plotar_metricas_principais, # Importa função de plotagem
    plotar_matriz_confusao # Importa função de plotagem
)

def main():
    """
    Função principal para demonstrar o cálculo e visualização das métricas.
    """
    print("--- Calculando e Visualizando Métricas de Avaliação de Aprendizado ---")

    # Definindo a matriz de confusão arbitrária
    vp = 80  # Verdadeiros Positivos
    fn = 20  # Falsos Negativos
    fp = 10  # Falsos Positivos
    vn = 90  # Verdadeiros Negativos

    print(f"\nMatriz de Confusão Utilizada:")
    print(f"  VP (Verdadeiros Positivos): {vp}")
    print(f"  FN (Falsos Negativos):      {fn}")
    print(f"  FP (Falsos Positivos):      {fp}")
    print(f"  VN (Verdadeiros Negativos): {vn}")

    # Calculando as métricas
    sensibilidade = calcular_sensibilidade(vp, fn)
    especificidade = calcular_especificidade(vn, fp)
    acuracia = calcular_acuracia(vp, fn, fp, vn)
    precisao = calcular_precisao(vp, fp)
    f1 = calcular_fscore(precisao, sensibilidade)

    # Calculando novas métricas
    mcc = calcular_mcc(vp, fn, fp, vn)
    # A AUC-ROC de exemplo precisa das métricas já calculadas
    auc_roc_exemplo = calcular_auc_roc_exemplo(sensibilidade, especificidade)

    # Exibindo os resultados textuais
    print("\n--- Resultados das Métricas ---")
    print(f"Sensibilidade (Recall): {sensibilidade:.4f}")
    print(f"Especificidade:         {especificidade:.4f}")
    print(f"Acurácia:               {acuracia:.4f}")
    print(f"Precisão:               {precisao:.4f}")
    print(f"F-score:                {f1:.4f}")
    print(f"MCC:                    {mcc:.4f}")
    print(f"AUC-ROC (Exemplo):      {auc_roc_exemplo:.4f}")
    print("\n------------------------------")

    # Gerando visualizações
    print("\n--- Gerando Visualizações ---")
    plotar_metricas_principais(vp, fn, fp, vn)
    plotar_matriz_confusao(vp, fn, fp, vn, classes=['Classe Negativa', 'Classe Positiva']) # Exemplo de nomes de classe personalizados
    print("------------------------------")

if __name__ == "__main__":
    main()
