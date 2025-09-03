import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from datetime import datetime, timedelta
import schedule
import time
from typing import Dict, List
import json
import os
from pathlib import Path

class AcademicScheduler:
    """
    Sistema de automação para tarefas acadêmicas.
    """
    
    def __init__(self, email_config: Dict = None):
        self.email_config = email_config or {}
        self.tasks_file = "academic_tasks.json"
        self.backup_dir = Path("backups")
        self.backup_dir.mkdir(exist_ok=True)
        
    def add_task(self, task: Dict) -> bool:
        """
        Adiciona uma nova tarefa acadêmica.
        
        Args:
            task: Dict com detalhes da tarefa
            
        Returns:
            True se adicionado com sucesso
        """
        required_fields = ['title', 'due_date', 'course', 'type']
        if not all(field in task for field in required_fields):
            raise ValueError("Campos obrigatórios faltando")
        
        tasks = self._load_tasks()
        task['id'] = len(tasks) + 1
        task['created_at'] = datetime.now().isoformat()
        task['completed'] = False
        task['priority'] = task.get('priority', 'medium')
        
        tasks.append(task)
        self._save_tasks(tasks)
        
        # Agendar lembretes
        self._schedule_reminders(task)
        
        return True
    
    def get_upcoming_tasks(self, days_ahead: int = 7) -> List[Dict]:
        """
        Retorna tarefas próximas.
        
        Args:
            days_ahead: Dias a frente para buscar
            
        Returns:
            Lista de tarefas
        """
        tasks = self._load_tasks()
        upcoming = []
        
        cutoff_date = datetime.now() + timedelta(days=days_ahead)
        
        for task in tasks:
            if not task['completed']:
                due_date = datetime.fromisoformat(task['due_date'])
                if due_date <= cutoff_date:
                    task['days_until_due'] = (due_date - datetime.now()).days
                    upcoming.append(task)
        
        return sorted(upcoming, key=lambda x: x['due_date'])
    
    def send_daily_summary(self):
        """
        Envia resumo diário de tarefas por email.
        """
        tasks = self.get_upcoming_tasks(3)
        
        if not tasks:
            return
        
        subject = f"📚 Resumo Acadêmico - {datetime.now().strftime('%d/%m/%Y')}"
        
        body = f"""
        Bom dia! Aqui está seu resumo de tarefas acadêmicas:
        
        TAREFAS PRÓXIMAS:
        """
        
        for task in tasks:
            days_left = task['days_until_due']
            urgency = "🔴" if days_left <= 1 else "🟡" if days_left <= 3 else "🟢"
            
            body += f"\n{urgency} {task['title']} ({task['course']})"
            body += f" - Vence em {days_left} dia(s)"
        
        body += f"""
        
        Dica: Organize seu tempo e não deixe para última hora!
        
        ---
        CollegeFunctions Academic Scheduler
        """
        
        self._send_email(subject, body)
    
    def backup_grades(self, grades_data: Dict):
        """
        Faz backup automático das notas.
        
        Args:
            grades_data: Dict com dados de notas
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.backup_dir / f"grades_backup_{timestamp}.json"
        
        backup_data = {
            'timestamp': datetime.now().isoformat(),
            'grades': grades_data,
            'total_courses': len(grades_data)
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, indent=2, ensure_ascii=False)
        
        print(f"Backup salvo: {filename}")
    
    def generate_weekly_report(self) -> str:
        """
        Gera relatório semanal de desempenho.
        
        Returns:
            String com o relatório
        """
        tasks = self._load_tasks()
        
        completed = [t for t in tasks if t['completed']]
        pending = [t for t in tasks if not t['completed']]
        
        # Análise por curso
        course_stats = {}
        for task in tasks:
            course = task['course']
            if course not in course_stats:
                course_stats[course] = {'total': 0, 'completed': 0}
            course_stats[course]['total'] += 1
            if task['completed']:
                course_stats[course]['completed'] += 1
        
        report = f"""
        📊 RELATÓRIO SEMANAL ACADÊMICO
        
        RESUMO GERAL:
        - Total de tarefas: {len(tasks)}
        - Tarefas concluídas: {len(completed)}
        - Tarefas pendentes: {len(pending)}
        - Taxa de conclusão: {(len(completed)/len(tasks)*100):.1f}%
        
        DESEMPENHO POR DISCIPLINA:
        """
        
        for course, stats in course_stats.items():
            completion_rate = (stats['completed'] / stats['total']) * 100
            report += f"\n{course}: {stats['completed']}/{stats['total']} ({completion_rate:.1f}% concluído)"
        
        # Tarefas próximas
        upcoming = self.get_upcoming_tasks(7)
        if upcoming:
            report += "\n\n📅 TAREFAS PRÓXIMAS (7 dias):"
            for task in upcoming:
                days_left = task['days_until_due']
                report += f"\n- {task['title']} ({task['course']}) - {days_left} dias"
        
        return report
    
    def _load_tasks(self) -> List[Dict]:
        """Carrega tarefas do arquivo."""
        try:
            if os.path.exists(self.tasks_file):
                with open(self.tasks_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Erro ao carregar tarefas: {e}")
            return []
    
    def _save_tasks(self, tasks: List[Dict]):
        """Salva tarefas no arquivo."""
        try:
            with open(self.tasks_file, 'w', encoding='utf-8') as f:
                json.dump(tasks, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar tarefas: {e}")
    
    def _schedule_reminders(self, task: Dict):
        """Agenda lembretes para uma tarefa."""
        # Implementação básica - em produção poderia usar agendamento mais sofisticado
        pass
    
    def _send_email(self, subject: str, body: str):
        """Envia email (simulado)."""
        if not self.email_config:
            print("Configuração de email não fornecida")
            print(f"Assunto: {subject}")
            print(f"Corpo: {body}")
            return
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['sender']
            msg['To'] = self.email_config['recipient']
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(self.email_config['smtp_server'], 587)
            server.starttls()
            server.login(self.email_config['username'], self.email_config['password'])
            server.send_message(msg)
            server.quit()
            
            print("Email enviado com sucesso!")
            
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

class TaskReminder:
    """
    Sistema de lembretes para tarefas específicas.
    """
    
    def __init__(self):
        self.reminders = []
    
    def add_reminder(self, task_name: str, reminder_time: datetime, message: str):
        """
        Adiciona um lembrete.
        
        Args:
            task_name: Nome da tarefa
            reminder_time: Quando lembrar
            message: Mensagem do lembrete
        """
        self.reminders.append({
            'task': task_name,
            'time': reminder_time,
            'message': message,
            'notified': False
        })
    
    def check_reminders(self):
        """Verifica e executa lembretes pendentes."""
        now = datetime.now()
        
        for reminder in self.reminders:
            if not reminder['notified'] and now >= reminder['time']:
                print(f"🔔 LEMBRETE: {reminder['message']}")
                reminder['notified'] = True

if __name__ == "__main__":
    # Exemplo de uso
    scheduler = AcademicScheduler()
    
    # Adicionar tarefas
    tasks = [
        {
            'title': 'Entregar trabalho de Cálculo',
            'due_date': (datetime.now() + timedelta(days=3)).isoformat(),
            'course': 'Cálculo I',
            'type': 'assignment',
            'priority': 'high'
        },
        {
            'title': 'Estudar para prova de Programação',
            'due_date': (datetime.now() + timedelta(days=7)).isoformat(),
            'course': 'Programação I',
            'type': 'exam',
            'priority': 'medium'
        }
    ]
    
    for task in tasks:
        scheduler.add_task(task)
    
    # Gerar relatório
    print(scheduler.generate_weekly_report())
    
    # Verificar tarefas próximas
    upcoming = scheduler.get_upcoming_tasks(7)
    print("\nTarefas próximas:")
    for task in upcoming:
        print(f"- {task['title']} ({task['days_until_due']} dias)")