import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from typing import Dict, List, Optional
from datetime import datetime
import os

class CourseScraper:
    """
    Web scraper para coletar informações educacionais de plataformas acadêmicas.
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.base_urls = {
            'sigaa': 'https://sigaa.ufpb.br',
            'moodle': 'https://moodle.ufpb.br',
            'drive': 'https://drive.google.com'
        }
    
    def scrape_course_schedule(self, semester: str) -> Dict:
        """
        Simula scraping de horários de disciplinas.
        Em produção, conectaria ao SIGAA real.
        
        Args:
            semester: Período letivo (ex: "2024.1")
            
        Returns:
            Dict com informações de horários
        """
        # Dados simulados para demonstração
        mock_schedule = {
            "semester": semester,
            "courses": [
                {
                    "name": "Cálculo I",
                    "code": "MAT001",
                    "schedule": [
                        {"day": "Segunda", "time": "08:00-10:00", "room": "A101"},
                        {"day": "Quarta", "time": "08:00-10:00", "room": "A101"}
                    ],
                    "professor": "Dr. Silva"
                },
                {
                    "name": "Programação I",
                    "code": "INF001",
                    "schedule": [
                        {"day": "Terça", "time": "14:00-16:00", "room": "Lab1"},
                        {"day": "Quinta", "time": "14:00-16:00", "room": "Lab1"}
                    ],
                    "professor": "Dr. Santos"
                }
            ]
        }
        
        # Salvar para uso offline
        self._save_data(mock_schedule, f"schedule_{semester}.json")
        return mock_schedule
    
    def scrape_course_materials(self, course_code: str) -> List[Dict]:
        """
        Coleta materiais de uma disciplina específica.
        
        Args:
            course_code: Código da disciplina
            
        Returns:
            Lista de materiais disponíveis
        """
        # Dados simulados
        mock_materials = [
            {
                "title": "Apostila de Cálculo I",
                "type": "PDF",
                "size": "2.5MB",
                "date": "2024-03-15",
                "url": f"https://drive.google.com/file/d/example_{course_code}_1"
            },
            {
                "title": "Lista de Exercícios 1",
                "type": "PDF",
                "size": "1.2MB",
                "date": "2024-03-20",
                "url": f"https://drive.google.com/file/d/example_{course_code}_2"
            },
            {
                "title": "Slides Aula 1-5",
                "type": "PPTX",
                "size": "5.8MB",
                "date": "2024-03-10",
                "url": f"https://drive.google.com/file/d/example_{course_code}_3"
            }
        ]
        
        self._save_data(mock_materials, f"materials_{course_code}.json")
        return mock_materials
    
    def monitor_course_vacancies(self, course_code: str) -> Dict:
        """
        Monitora vagas disponíveis em uma turma.
        
        Args:
            course_code: Código da turma
            
        Returns:
            Informações sobre vagas
        """
        # Dados simulados
        mock_vacancy = {
            "course_code": course_code,
            "total_vacancies": 60,
            "occupied_vacancies": 58,
            "available_vacancies": 2,
            "waiting_list": 5,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self._save_data(mock_vacancy, f"vacancy_{course_code}.json")
        return mock_vacancy
    
    def scrape_professor_reviews(self, professor_name: str) -> List[Dict]:
        """
        Coleta avaliações de professores (simulado).
        
        Args:
            professor_name: Nome do professor
            
        Returns:
            Lista de avaliações
        """
        mock_reviews = [
            {
                "professor": professor_name,
                "course": "Cálculo I",
                "rating": 4.5,
                "comment": "Ótimo professor, explicações claras",
                "difficulty": "Média",
                "date": "2024-01-15"
            },
            {
                "professor": professor_name,
                "course": "Álgebra Linear",
                "rating": 4.8,
                "comment": "Muito atencioso com os alunos",
                "difficulty": "Alta",
                "date": "2024-02-20"
            }
        ]
        
        return mock_reviews
    
    def get_academic_calendar(self, year: int) -> Dict:
        """
        Obtém calendário acadêmico do ano.
        
        Args:
            year: Ano letivo
            
        Returns:
            Calendário acadêmico
        """
        calendar = {
            "year": year,
            "semesters": [
                {
                    "semester": "2024.1",
                    "start_date": "2024-03-04",
                    "end_date": "2024-07-12",
                    "breaks": [
                        {"name": "Semana Santa", "start": "2024-03-25", "end": "2024-03-29"},
                        {"name": "Tiradentes", "date": "2024-04-21"}
                    ]
                },
                {
                    "semester": "2024.2",
                    "start_date": "2024-08-05",
                    "end_date": "2024-12-13",
                    "breaks": [
                        {"name": "Independência", "date": "2024-09-07"},
                        {"name": "Nossa Senhora", "date": "2024-10-12"}
                    ]
                }
            ]
        }
        
        self._save_data(calendar, f"calendar_{year}.json")
        return calendar
    
    def _save_data(self, data: any, filename: str):
        """
        Salva dados localmente para uso offline.
        
        Args:
            data: Dados a serem salvos
            filename: Nome do arquivo
        """
        save_dir = "scraped_data"
        os.makedirs(save_dir, exist_ok=True)
        
        filepath = os.path.join(save_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def export_to_csv(self, data: List[Dict], filename: str):
        """
        Exporta dados para CSV.
        
        Args:
            data: Lista de dicionários
            filename: Nome do arquivo CSV
        """
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Dados exportados para {filename}")

if __name__ == "__main__":
    scraper = CourseScraper()
    
    # Exemplos de uso
    print("=== HORÁRIOS ===")
    schedule = scraper.scrape_course_schedule("2024.1")
    print(json.dumps(schedule, indent=2, ensure_ascii=False))
    
    print("\n=== MATERIAIS ===")
    materials = scraper.scrape_course_materials("MAT001")
    print(json.dumps(materials, indent=2, ensure_ascii=False))
    
    print("\n=== VAGAS ===")
    vacancies = scraper.monitor_course_vacancies("MAT001")
    print(json.dumps(vacancies, indent=2, ensure_ascii=False))