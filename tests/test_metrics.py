# tests/test_metrics.py
import unittest
import numpy as np # Necessário para comparar com np.sqrt
from src.metrics_calculator import (
    calcular_sensibilidade,
    calcular_especificidade,
    calcular_acuracia,
    calcular_precisao,
    calcular_fscore,
    calcular_mcc, # Importa nova função
    calcular_auc_roc_exemplo # Importa nova função
)

class TestMetricsCalculator(unittest.TestCase):

    def setUp(self):
        """Configura valores comuns para os testes."""
        self.vp = 80
        self.fn = 20
        self.fp = 10
        self.vn = 90

        self.sens = 0.8 # Calculado: 80 / (80+20)
        self.esp = 0.9  # Calculado: 90 / (90+10)
        self.acur = 0.85 # Calculado: (80+90) / 200
        self.prec = 80/90 # Calculado: 80 / (80+10)
        self.f1 = 0.8421052631578947 # Calculado: 2 * (prec * sens) / (prec + sens)


    def test_calcular_sensibilidade(self):
        self.assertAlmostEqual(calcular_sensibilidade(self.vp, self.fn), self.sens)

    def test_calcular_especificidade(self):
        self.assertAlmostEqual(calcular_especificidade(self.vn, self.fp), self.esp)

    def test_calcular_acuracia(self):
        self.assertAlmostEqual(calcular_acuracia(self.vp, self.fn, self.fp, self.vn), self.acur)

    def test_calcular_precisao(self):
        self.assertAlmostEqual(calcular_precisao(self.vp, self.fp), self.prec)

    def test_calcular_fscore(self):
        self.assertAlmostEqual(calcular_fscore(self.prec, self.sens), self.f1)

    def test_calcular_mcc(self):
        """Testa o cálculo do Matthews Correlation Coefficient (MCC)."""
        # Formula: (VP*VN - FP*FN) / sqrt((VP+FP)*(VP+FN)*(VN+FP)*(VN+FN))
        # Num: (80*90) - (10*20) = 7200 - 200 = 7000
        # Den: sqrt((80+10)*(80+20)*(90+10)*(90+20)) = sqrt(90*100*100*110) = sqrt(99000000) = 9949.87437
        # MCC = 7000 / 9949.87437 = 0.70353
        expected_mcc = 0.7035302486670661
        self.assertAlmostEqual(calcular_mcc(self.vp, self.fn, self.fp, self.vn), expected_mcc)
        self.assertAlmostEqual(calcular_mcc(0, 0, 0, 0), 0.0) # Teste com todos zero

    def test_calcular_auc_roc_exemplo(self):
        """Testa o cálculo da AUC-ROC de exemplo."""
        # Como é uma aproximação, o teste verifica se está dentro de um range razoável
        # ou se corresponde ao valor esperado para os inputs.
        # Teste com valores que resultam em AUC = 1 (se fosse ideal)
        # Exemplo: Sensibilidade=1, Especificidade=1 -> AUC = (1+1)/2 = 1.0
        self.assertAlmostEqual(calcular_auc_roc_exemplo(1.0, 1.0), 1.0)
        # Teste com valores que resultam em AUC = 0.5 (random guessing)
        self.assertAlmostEqual(calcular_auc_roc_exemplo(0.5, 0.5), 0.5)
        # Teste com os valores do nosso caso
        expected_auc_exemplo = (self.sens + self.esp) / 2 # Usando a aproximação definida
        self.assertAlmostEqual(calcular_auc_roc_exemplo(self.sens, self.esp), expected_auc_exemplo)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
