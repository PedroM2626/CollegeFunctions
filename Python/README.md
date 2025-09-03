# Python - CollegeFunctions

## 📊 Camada de Alto Nível - Data Science & Automação

Python é a camada mais alta do projeto CollegeFunctions, focando em **análise de dados acadêmicos, machine learning, web scraping e automação** para estudantes universitários.

## 🚀 Instalação

```bash
cd Python
pip install -r requirements.txt
```

## 📁 Estrutura do Projeto

```
Python/
├── src/                          # Código-fonte principal
│   ├── data_analysis/            # Análise de dados acadêmicos
│   ├── web_scraping/            # Coleta de dados educacionais
│   ├── automation/              # Automação de tarefas
│   ├── machine_learning/        # IA aplicada à educação
│   └── utils/                   # Utilitários compartilhados
├── tests/                       # Testes unitários
├── notebooks/                   # Jupyter notebooks para análise
├── requirements.txt             # Dependências Python
└── README.md                    # Este arquivo
```

## 🎯 Funcionalidades

### 1. Análise de Dados Acadêmicos
- **Calculadora de Notas**: Médias ponderadas, simulações de nota final
- **Estatísticas de Desempenho**: GPA, percentis, tendências
- **Padrões de Estudo**: Análise de horas de estudo vs performance

### 2. Web Scraping Educacional
- **SIGAA Scraper**: Extrai horários e notas automaticamente
- **Busca de Material**: Coleta PDFs e slides das disciplinas
- **Monitoramento de Vagas**: Alertas para turmas cheias

### 3. Machine Learning
- **Previsão de Desempenho**: Prediz notas baseado em padrões históricos
- **Identificação de Risco**: Detecta alunos em risco de reprovação
- **Recomendação de Conteúdo**: Sugere materiais baseado em dificuldades

### 4. Automação
- **Lembretes Automáticos**: Emails com tarefas e provas
- **Backup de Notas**: Salva automaticamente progresso acadêmico
- **Relatórios Semanais**: Dashboards de desempenho

## 📋 Uso Rápido

### Análise de Notas
```python
from src.data_analysis.grade_calculator import GradeCalculator

calc = GradeCalculator()
minha_nota = calc.simulate_final_grade([85, 90, 78], 85, 0.3)
print(f"Preciso de {minha_nota:.1f} na final")
```

### Web Scraping
```python
from src.web_scraping.course_scraper import CourseScraper

scraper = CourseScraper()
horarios = scraper.get_schedule("2024.1")
```

### Machine Learning
```python
from src.machine_learning.student_performance import StudentPerformancePredictor

predictor = StudentPerformancePredictor()
risco = predictor.identify_at_risk_students(dados_alunos)
```

## 🧪 Desenvolvimento

### Executar Testes
```bash
pytest tests/
```

### Jupyter Notebooks
```bash
jupyter notebook notebooks/
```

## 📊 Progressão de Complexidade

- **C**: Funções matemáticas de baixo nível
- **Java**: Jogos e interfaces simples  
- **Python**: Data science e automação de alto nível

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo LICENSE para detalhes.

## 🆘 Suporte

Para dúvidas ou problemas, abra uma issue no GitHub ou entre em contato.

---

**CollegeFunctions** - Aprendizado de programação desde baixo nível até aplicações modernas de data science!