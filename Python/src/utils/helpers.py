import os
import json
from datetime import datetime
from typing import Dict, List, Any
import pandas as pd

def save_to_json(data: Any, filename: str, directory: str = "data") -> str:
    """
    Salva dados em formato JSON.
    
    Args:
        data: Dados a serem salvos
        filename: Nome do arquivo
        directory: Diretório para salvar
        
    Returns:
        Caminho completo do arquivo salvo
    """
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    
    return filepath

def load_from_json(filename: str, directory: str = "data") -> Any:
    """
    Carrega dados de arquivo JSON.
    
    Args:
        filename: Nome do arquivo
        directory: Diretório do arquivo
        
    Returns:
        Dados carregados ou None se arquivo não existir
    """
    filepath = os.path.join(directory, filename)
    
    if not os.path.exists(filepath):
        return None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_data_summary(df: pd.DataFrame) -> Dict:
    """
    Cria um resumo estatístico de um DataFrame.
    
    Args:
        df: DataFrame pandas
        
    Returns:
        Dict com estatísticas
    """
    summary = {
        'shape': df.shape,
        'columns': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'numeric_summary': df.describe().to_dict() if df.select_dtypes(include=[np.number]).columns.any() else {}
    }
    
    return summary

def format_date(date_str: str, input_format: str = "%Y-%m-%d", output_format: str = "%d/%m/%Y") -> str:
    """
    Formata data de um formato para outro.
    
    Args:
        date_str: String da data
        input_format: Formato de entrada
        output_format: Formato de saída
        
    Returns:
        Data formatada
    """
    try:
        date_obj = datetime.strptime(date_str, input_format)
        return date_obj.strftime(output_format)
    except ValueError:
        return date_str

def calculate_gpa(grades: List[float], credit_hours: List[int] = None) -> float:
    """
    Calcula GPA (Grade Point Average).
    
    Args:
        grades: Lista de notas (0-100)
        credit_hours: Lista de créditos (opcional)
        
    Returns:
        GPA calculado
    """
    if not grades:
        return 0.0
    
    # Converter notas para sistema 4.0
    def grade_to_gpa(grade):
        if grade >= 90:
            return 4.0
        elif grade >= 85:
            return 3.7
        elif grade >= 80:
            return 3.3
        elif grade >= 75:
            return 3.0
        elif grade >= 70:
            return 2.7
        elif grade >= 65:
            return 2.3
        elif grade >= 60:
            return 2.0
        else:
            return 0.0
    
    gpa_values = [grade_to_gpa(grade) for grade in grades]
    
    if credit_hours:
        weighted_gpa = sum(g * c for g, c in zip(gpa_values, credit_hours))
        return weighted_gpa / sum(credit_hours)
    else:
        return sum(gpa_values) / len(gpa_values)

def validate_student_data(data: Dict) -> bool:
    """
    Valida dados de estudante.
    
    Args:
        data: Dict com dados do estudante
        
    Returns:
        True se dados são válidos
    """
    required_fields = ['name', 'student_id', 'grades']
    
    for field in required_fields:
        if field not in data:
            return False
    
    if not isinstance(data['grades'], list):
        return False
    
    if not all(0 <= grade <= 100 for grade in data['grades']):
        return False
    
    return True

def create_student_report(student_data: Dict) -> str:
    """
    Cria relatório formatado para estudante.
    
    Args:
        student_data: Dict com dados do estudante
        
    Returns:
        String com relatório
    """
    if not validate_student_data(student_data):
        return "Dados do estudante inválidos"
    
    name = student_data['name']
    student_id = student_data['student_id']
    grades = student_data['grades']
    
    average = sum(grades) / len(grades)
    gpa = calculate_gpa(grades)
    highest = max(grades)
    lowest = min(grades)
    
    report = f"""
    📋 RELATÓRIO DO ESTUDANTE
    
    Nome: {name}
    Matrícula: {student_id}
    
    📊 DESEMPENHO:
    - Média das notas: {average:.2f}
    - GPA: {gpa:.2f}
    - Maior nota: {highest}
    - Menor nota: {lowest}
    - Total de avaliações: {len(grades)}
    
    📈 ANÁLISE:
    {"Excelente desempenho!" if average >= 90 else 
     "Bom desempenho, continue assim!" if average >= 75 else
     "Precisa melhorar, busque ajuda!" if average >= 60 else
     "Atenção urgente necessária!"}
    """
    
    return report.strip()

class AcademicCalendar:
    """
    Utilitário para gerenciar calendário acadêmico.
    """
    
    def __init__(self):
        self.academic_events = []
    
    def add_event(self, name: str, date: str, event_type: str, description: str = ""):
        """
        Adiciona evento ao calendário.
        
        Args:
            name: Nome do evento
            date: Data do evento (YYYY-MM-DD)
            event_type: Tipo de evento (prova, trabalho, etc)
            description: Descrição opcional
        """
        event = {
            'name': name,
            'date': date,
            'type': event_type,
            'description': description
        }
        self.academic_events.append(event)
    
    def get_upcoming_events(self, days_ahead: int = 30) -> List[Dict]:
        """
        Retorna eventos próximos.
        
        Args:
            days_ahead: Dias a frente
            
        Returns:
            Lista de eventos próximos
        """
        today = datetime.now().date()
        cutoff = today + timedelta(days=days_ahead)
        
        upcoming = []
        for event in self.academic_events:
            event_date = datetime.strptime(event['date'], "%Y-%m-%d").date()
            if today <= event_date <= cutoff:
                event['days_until'] = (event_date - today).days
                upcoming.append(event)
        
        return sorted(upcoming, key=lambda x: x['date'])
    
    def save_calendar(self, filename: str = "academic_calendar.json"):
        """Salva calendário em arquivo."""
        save_to_json(self.academic_events, filename)
    
    def load_calendar(self, filename: str = "academic_calendar.json"):
        """Carrega calendário de arquivo."""
        data = load_from_json(filename)
        if data:
            self.academic_events = data

if __name__ == "__main__":
    # Exemplos de uso
    print("=== UTILS EXAMPLES ===")
    
    # Exemplo de dados de estudante
    student = {
        'name': 'João Silva',
        'student_id': '2024001',
        'grades': [85, 92, 78, 95, 88]
    }
    
    print(create_student_report(student))
    
    # Exemplo de calendário
    calendar = AcademicCalendar()
    calendar.add_event("Prova de Cálculo", "2024-12-15", "prova")
    calendar.add_event("Entrega trabalho", "2024-12-20", "trabalho")
    
    upcoming = calendar.get_upcoming_events()
    print("\nPróximos eventos:")
    for event in upcoming:
        print(f"- {event['name']} em {event['date']} ({event['type']})")