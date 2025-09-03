import numpy as np
import pandas as pd
from typing import List, Dict, Optional

class GradeCalculator:
    """
    Calculadora de notas acadêmicas com funcionalidades avançadas.
    """
    
    def __init__(self):
        self.grade_weights = {}
        self.gpa_scale = {
            range(90, 101): 4.0,
            range(85, 90): 3.7,
            range(80, 85): 3.3,
            range(75, 80): 3.0,
            range(70, 75): 2.7,
            range(65, 70): 2.3,
            range(60, 65): 2.0,
            range(0, 60): 0.0
        }
    
    def calculate_weighted_average(self, grades: List[float], weights: List[float]) -> float:
        """
        Calcula média ponderada das notas.
        
        Args:
            grades: Lista de notas
            weights: Lista de pesos correspondentes
            
        Returns:
            Média ponderada
        """
        if len(grades) != len(weights):
            raise ValueError("Grades and weights must have the same length")
        
        if abs(sum(weights) - 1.0) > 0.01:
            raise ValueError("Weights must sum to 1.0")
        
        return np.average(grades, weights=weights)
    
    def simulate_final_grade_needed(self, current_grades: List[float], 
                                  current_weights: List[float], 
                                  desired_final_grade: float, 
                                  final_exam_weight: float) -> float:
        """
        Calcula nota necessária na prova final para atingir a média desejada.
        
        Args:
            current_grades: Notas atuais
            current_weights: Pesos das notas atuais
            desired_final_grade: Média desejada
            final_exam_weight: Peso da prova final
            
        Returns:
            Nota necessária na prova final
        """
        current_weight_sum = sum(current_weights)
        if abs(current_weight_sum + final_exam_weight - 1.0) > 0.01:
            raise ValueError("Weights must sum to 1.0")
        
        current_contribution = np.average(current_grades, weights=current_weights)
        needed_final = (desired_final_grade - current_contribution * (1 - final_exam_weight)) / final_exam_weight
        
        return max(0, min(100, needed_final))
    
    def calculate_gpa(self, grades: List[float]) -> float:
        """
        Calcula GPA baseado no sistema 4.0 americano.
        
        Args:
            grades: Lista de notas (0-100)
            
        Returns:
            GPA calculado
        """
        if not grades:
            return 0.0
        
        points = []
        for grade in grades:
            for grade_range, point in self.gpa_scale.items():
                if int(grade) in grade_range:
                    points.append(point)
                    break
            else:
                points.append(0.0)
        
        return np.mean(points)
    
    def calculate_semester_statistics(self, grades_data: Dict[str, List[float]]) -> Dict:
        """
        Calcula estatísticas do semestre.
        
        Args:
            grades_data: Dict com disciplinas e suas notas
            
        Returns:
            Dict com estatísticas calculadas
        """
        all_grades = []
        for subject, grades in grades_data.items():
            all_grades.extend(grades)
        
        if not all_grades:
            return {}
        
        return {
            'total_subjects': len(grades_data),
            'total_grades': len(all_grades),
            'average_grade': np.mean(all_grades),
            'median_grade': np.median(all_grades),
            'std_deviation': np.std(all_grades),
            'min_grade': np.min(all_grades),
            'max_grade': np.max(all_grades),
            'gpa': self.calculate_gpa(all_grades)
        }
    
    def create_grade_report(self, student_name: str, grades_data: Dict[str, List[float]]) -> str:
        """
        Gera um relatório completo de desempenho acadêmico.
        
        Args:
            student_name: Nome do estudante
            grades_data: Dict com disciplinas e notas
            
        Returns:
            String formatada com o relatório
        """
        stats = self.calculate_semester_statistics(grades_data)
        
        report = f"""
=== RELATÓRIO DE DESEMPENHO ACADÊMICO ===
Estudante: {student_name}

ESTATÍSTICAS GERAIS:
- Disciplinas: {stats['total_subjects']}
- Total de avaliações: {stats['total_grades']}
- Média geral: {stats['average_grade']:.2f}
- Mediana: {stats['median_grade']:.2f}
- Desvio padrão: {stats['std_deviation']:.2f}
- Nota mínima: {stats['min_grade']:.2f}
- Nota máxima: {stats['max_grade']:.2f}
- GPA: {stats['gpa']:.2f}

DESEMPENHO POR DISCIPLINA:
"""
        
        for subject, grades in grades_data.items():
            subject_avg = np.mean(grades)
            subject_gpa = self.calculate_gpa(grades)
            report += f"{subject}: Média {subject_avg:.2f} (GPA: {subject_gpa:.2f})\n"
        
        return report

if __name__ == "__main__":
    # Exemplo de uso
    calc = GradeCalculator()
    
    # Dados de exemplo
    grades_data = {
        "Cálculo I": [85, 90, 78],
        "Programação": [92, 88, 95],
        "Física": [75, 82, 80]
    }
    
    # Simulação de nota necessária
    nota_necessaria = calc.simulate_final_grade_needed([85, 90], [0.4, 0.3], 85, 0.3)
    print(f"Nota necessária na final: {nota_necessaria:.1f}")
    
    # Relatório completo
    print(calc.create_grade_report("João Silva", grades_data))