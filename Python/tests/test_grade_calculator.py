import pytest
import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_analysis.grade_calculator import GradeCalculator

class TestGradeCalculator:
    
    def setup_method(self):
        self.calc = GradeCalculator()
    
    def test_calculate_weighted_average(self):
        grades = [85, 90, 78]
        weights = [0.3, 0.4, 0.3]
        result = self.calc.calculate_weighted_average(grades, weights)
        expected = 85.4
        assert abs(result - expected) < 0.01
    
    def test_calculate_weighted_average_invalid_weights(self):
        grades = [85, 90, 78]
        weights = [0.3, 0.4, 0.4]  # Soma > 1
        
        with pytest.raises(ValueError):
            self.calc.calculate_weighted_average(grades, weights)
    
    def test_simulate_final_grade_needed(self):
        current_grades = [85, 90]
        current_weights = [0.4, 0.3]
        desired_final = 85
        final_weight = 0.3
        
        result = self.calc.simulate_final_grade_needed(
            current_grades, current_weights, desired_final, final_weight
        )
        
        assert 0 <= result <= 100
    
    def test_calculate_gpa(self):
        grades = [95, 87, 92, 78]
        gpa = self.calc.calculate_gpa(grades)
        assert 2.0 <= gpa <= 4.0
    
    def test_calculate_semester_statistics(self):
        grades_data = {
            "Cálculo I": [85, 90, 78],
            "Programação": [92, 88, 95]
        }
        
        stats = self.calc.calculate_semester_statistics(grades_data)
        
        assert stats['total_subjects'] == 2
        assert stats['total_grades'] == 6
        assert 0 <= stats['average_grade'] <= 100
        assert 0 <= stats['gpa'] <= 4.0
    
    def test_create_grade_report(self):
        grades_data = {
            "Cálculo I": [85, 90, 78],
            "Programação": [92, 88, 95]
        }
        
        report = self.calc.create_grade_report("João Silva", grades_data)
        
        assert "João Silva" in report
        assert "Cálculo I" in report
        assert "Programação" in report
        assert "ESTATÍSTICAS GERAIS" in report

if __name__ == "__main__":
    pytest.main([__file__])