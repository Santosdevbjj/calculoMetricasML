# tests/test_metrics.py
import unittest
from src.metrics_calculator import (
    calcular_sensibilidade,
    calcular_especificidade,
    calcular_acuracia,
    calcular_precisao,
    calcular_fscore
)

class TestMetricsCalculator(unittest.TestCase):

    def setUp(self):
        """Configura valores comuns para os testes."""
        self.vp = 80
        self.fn = 20
        self.fp = 10
        self.vn = 90

    def test_calcular_sensibilidade(self):
        """Testa o cálculo da Sensibilidade."""
        # Formula: VP / (VP + FN) = 80 / (80 + 20) = 80 / 100 = 0.8
        self.assertAlmostEqual(calcular_sensibilidade(self.vp, self.fn), 0.8)
        self.assertAlmostEqual(calcular_sensibilidade(0, 10), 0.0) # Teste com VP=0
        self.assertAlmostEqual(calcular_sensibilidade(10, 0), 1.0) # Teste com FN=0
        self.assertAlmostEqual(calcular_sensibilidade(0, 0), 0.0) # Teste com VP=0 e FN=0

    def test_calcular_especificidade(self):
        """Testa o cálculo da Especificidade."""
        # Formula: VN / (VN + FP) = 90 / (90 + 10) = 90 / 100 = 0.9
        self.assertAlmostEqual(calcular_especificidade(self.vn, self.fp), 0.9)
        self.assertAlmostEqual(calcular_especificidade(0, 10), 0.0) # Teste com VN=0
        self.assertAlmostEqual(calcular_especificidade(10, 0), 1.0) # Teste com FP=0
        self.assertAlmostEqual(calcular_especificidade(0, 0), 0.0) # Teste com VN=0 e FP=0

    def test_calcular_acuracia(self):
        """Testa o cálculo da Acurácia."""
        # Formula: (VP + VN) / (VP + FN + FP + VN) = (80 + 90) / (80 + 20 + 10 + 90) = 170 / 200 = 0.85
        self.assertAlmostEqual(calcular_acuracia(self.vp, self.fn, self.fp, self.vn), 0.85)
        self.assertAlmostEqual(calcular_acuracia(0, 0, 0, 0), 0.0) # Teste com todos zero

    def test_calcular_precisao(self):
        """Testa o cálculo da Precisão."""
        # Formula: VP / (VP + FP) = 80 / (80 + 10) = 80 / 90 = 0.8888...
        self.assertAlmostEqual(calcular_precisao(self.vp, self.fp), 80/90)
        self.assertAlmostEqual(calcular_precisao(0, 10), 0.0) # Teste com VP=0
        self.assertAlmostEqual(calcular_precisao(10, 0), 1.0) # Teste com FP=0
        self.assertAlmostEqual(calcular_precisao(0, 0), 0.0) # Teste com VP=0 e FP=0

    def test_calcular_fscore(self):
        """Testa o cálculo do F-score."""
        prec = calcular_precisao(self.vp, self.fp) # 80/90
        sens = calcular_sensibilidade(self.vp, self.fn) # 0.8
        # Formula: 2 * (P * S) / (P + S) = 2 * ((80/90) * 0.8) / ((80/90) + 0.8)
        # (80/90) * 0.8 = 0.8888... * 0.8 = 0.7111...
        # (80/90) + 0.8 = 0.8888... + 0.8 = 1.6888...
        # 2 * 0.7111... / 1.6888... = 1.4222... / 1.6888... = 0.8421...
        expected_fscore = 2 * (prec * sens) / (prec + sens)
        self.assertAlmostEqual(calcular_fscore(prec, sens), expected_fscore)
        self.assertAlmostEqual(calcular_fscore(0.0, 0.0), 0.0) # Teste com precisão e sensibilidade zero

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # Para rodar em ambientes como notebooks
