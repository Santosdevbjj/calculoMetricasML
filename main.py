# main.py

# Importa as funções do nosso pacote de métricas
from src.metrics_calculator import (
    calcular_sensibilidade,
    calcular_especificidade,
    calcular_acuracia,
    calcular_precisao,
    calcular_fscore
)

def main():
    """
    Função principal para demonstrar o cálculo das métricas.
    """
    print("--- Calculando Métricas de Avaliação de Aprendizado ---")

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
    f1 = calcular_fscore(precisao, sensibilidade) # Passamos precisão e sensibilidade já calculadas

    # Exibindo os resultados
    print("\n--- Resultados das Métricas ---")
    print(f"Sensibilidade (Recall): {sensibilidade:.4f}")
    print(f"Especificidade:         {especificidade:.4f}")
    print(f"Acurácia:               {acuracia:.4f}")
    print(f"Precisão:               {precisao:.4f}")
    print(f"F-score:                {f1:.4f}")
    print("\n------------------------------")

if __name__ == "__main__":
    main()
