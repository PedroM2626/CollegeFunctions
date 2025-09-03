import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
import joblib
from typing import Dict, List, Tuple, Optional

class StudentPerformancePredictor:
    """
    Sistema de predição de desempenho estudantil usando machine learning.
    """
    
    def __init__(self):
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        self.regressor = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def prepare_training_data(self, student_data: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """
        Prepara dados para treinamento.
        
        Args:
            student_data: DataFrame com dados dos alunos
            
        Returns:
            Tupla (features, target)
        """
        # Features típicas para análise
        feature_columns = [
            'attendance_rate', 'study_hours_per_week', 'previous_gpa',
            'assignments_completed', 'participation_score', 'quiz_average',
            'difficulty_level', 'extracurricular_activities'
        ]
        
        # Garantir que temos todas as colunas
        for col in feature_columns:
            if col not in student_data.columns:
                student_data[col] = 0
        
        features = student_data[feature_columns].fillna(0)
        
        # Target: performance category (0: baixo, 1: médio, 2: alto)
        if 'final_grade' in student_data.columns:
            target = pd.cut(student_data['final_grade'], 
                          bins=[0, 60, 80, 100], 
                          labels=[0, 1, 2])
        else:
            target = student_data.get('performance_category', 1)
        
        return features.values, target.values
    
    def train_models(self, student_data: pd.DataFrame) -> Dict[str, float]:
        """
        Treina os modelos de predição.
        
        Args:
            student_data: DataFrame com dados históricos
            
        Returns:
            Dict com métricas de performance
        """
        X, y = self.prepare_training_data(student_data)
        
        # Split dos dados
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Normalizar features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Treinar classificador
        self.classifier.fit(X_train_scaled, y_train)
        y_pred = self.classifier.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Treinar regressor para previsão de nota
        if 'final_grade' in student_data.columns:
            y_reg = student_data['final_grade'].values
            X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
                X, y_reg, test_size=0.2, random_state=42
            )
            X_train_reg_scaled = self.scaler.transform(X_train_reg)
            X_test_reg_scaled = self.scaler.transform(X_test_reg)
            
            self.regressor.fit(X_train_reg_scaled, y_train_reg)
            y_pred_reg = self.regressor.predict(X_test_reg_scaled)
            mse = mean_squared_error(y_test_reg, y_pred_reg)
        else:
            mse = 0.0
        
        self.is_trained = True
        
        return {
            'accuracy': accuracy,
            'mse': mse,
            'classification_report': classification_report(y_test, y_pred)
        }
    
    def predict_student_risk(self, student_features: Dict) -> Dict[str, any]:
        """
        Prediz risco de desempenho para um estudante.
        
        Args:
            student_features: Dict com features do estudante
            
        Returns:
            Dict com predições e probabilidades
        """
        if not self.is_trained:
            raise ValueError("Modelo não treinado. Execute train_models() primeiro.")
        
        # Converter para array
        feature_array = np.array([[
            student_features.get('attendance_rate', 0),
            student_features.get('study_hours_per_week', 0),
            student_features.get('previous_gpa', 0),
            student_features.get('assignments_completed', 0),
            student_features.get('participation_score', 0),
            student_features.get('quiz_average', 0),
            student_features.get('difficulty_level', 1),
            student_features.get('extracurricular_activities', 0)
        ]])
        
        # Normalizar
        feature_scaled = self.scaler.transform(feature_array)
        
        # Predizer categoria
        category = self.classifier.predict(feature_scaled)[0]
        probabilities = self.classifier.predict_proba(feature_scaled)[0]
        
        # Predizer nota final
        predicted_grade = self.regressor.predict(feature_scaled)[0]
        
        risk_levels = {0: "Alto risco", 1: "Risco médio", 2: "Baixo risco"}
        
        return {
            'risk_level': risk_levels[category],
            'risk_category': int(category),
            'risk_probabilities': {
                'high_risk': float(probabilities[0]),
                'medium_risk': float(probabilities[1]),
                'low_risk': float(probabilities[2])
            },
            'predicted_final_grade': float(predicted_grade),
            'recommendations': self._generate_recommendations(category, predicted_grade)
        }
    
    def identify_at_risk_students(self, student_data: pd.DataFrame) -> pd.DataFrame:
        """
        Identifica todos os alunos em risco.
        
        Args:
            student_data: DataFrame com dados dos alunos
            
        Returns:
            DataFrame com alunos em risco
        """
        if not self.is_trained:
            # Usar dados para treinar
            self.train_models(student_data)
        
        results = []
        for idx, row in student_data.iterrows():
            features = row.to_dict()
            prediction = self.predict_student_risk(features)
            results.append({
                'student_id': idx,
                'risk_level': prediction['risk_level'],
                'predicted_grade': prediction['predicted_final_grade'],
                'recommendations': prediction['recommendations']
            })
        
        return pd.DataFrame(results)
    
    def _generate_recommendations(self, risk_category: int, predicted_grade: float) -> List[str]:
        """
        Gera recomendações baseadas no risco.
        
        Args:
            risk_category: Categoria de risco (0, 1, 2)
            predicted_grade: Nota prevista
            
        Returns:
            Lista de recomendações
        """
        recommendations = []
        
        if risk_category == 0:  # Alto risco
            recommendations.extend([
                "Buscar monitoria ou reforço imediatamente",
                "Aumentar horas de estudo semanal",
                "Participar mais das aulas",
                "Revisar conceitos básicos"
            ])
        elif risk_category == 1:  # Risco médio
            recommendations.extend([
                "Manter consistência nos estudos",
                "Focar em áreas de maior dificuldade",
                "Participar de grupos de estudo",
                "Buscar feedback do professor"
            ])
        else:  # Baixo risco
            recommendations.extend([
                "Manter excelente desempenho",
                "Auxiliar colegas em dúvidas",
                "Explorar conteúdos avançados",
                "Considerar monitoria"
            ])
        
        return recommendations
    
    def save_model(self, filepath: str):
        """
        Salva o modelo treinado.
        
        Args:
            filepath: Caminho para salvar o modelo
        """
        if not self.is_trained:
            raise ValueError("Modelo não treinado")
        
        model_data = {
            'classifier': self.classifier,
            'regressor': self.regressor,
            'scaler': self.scaler,
            'is_trained': self.is_trained
        }
        
        joblib.dump(model_data, filepath)
        print(f"Modelo salvo em {filepath}")
    
    def load_model(self, filepath: str):
        """
        Carrega um modelo previamente treinado.
        
        Args:
            filepath: Caminho do modelo salvo
        """
        model_data = joblib.load(filepath)
        self.classifier = model_data['classifier']
        self.regressor = model_data['regressor']
        self.scaler = model_data['scaler']
        self.is_trained = model_data['is_trained']
        print(f"Modelo carregado de {filepath}")

# Função auxiliar para gerar dados simulados
class DataGenerator:
    """
    Gera dados simulados para treinamento e teste.
    """
    
    @staticmethod
    def generate_student_data(n_students: int = 100) -> pd.DataFrame:
        """
        Gera dados de estudantes para treinamento.
        
        Args:
            n_students: Número de estudantes a gerar
            
        Returns:
            DataFrame com dados simulados
        """
        np.random.seed(42)
        
        data = {
            'attendance_rate': np.random.uniform(0.5, 1.0, n_students),
            'study_hours_per_week': np.random.uniform(5, 40, n_students),
            'previous_gpa': np.random.uniform(2.0, 4.0, n_students),
            'assignments_completed': np.random.randint(50, 100, n_students),
            'participation_score': np.random.uniform(60, 100, n_students),
            'quiz_average': np.random.uniform(50, 100, n_students),
            'difficulty_level': np.random.randint(1, 5, n_students),
            'extracurricular_activities': np.random.randint(0, 3, n_students),
            'final_grade': np.random.uniform(0, 100, n_students)
        }
        
        # Adicionar correlação entre features e nota final
        weights = np.array([0.2, 0.15, 0.15, 0.15, 0.1, 0.15, -0.05, -0.05])
        features = np.array([data[col] for col in list(data.keys())[:-1]]).T
        
        # Ajustar nota final baseada nas features
        base_grade = np.dot(features, weights) * 100 + 50
        base_grade = np.clip(base_grade, 0, 100)
        data['final_grade'] = base_grade + np.random.normal(0, 5, n_students)
        data['final_grade'] = np.clip(data['final_grade'], 0, 100)
        
        return pd.DataFrame(data)

if __name__ == "__main__":
    # Exemplo de uso
    predictor = StudentPerformancePredictor()
    
    # Gerar dados de treino
    generator = DataGenerator()
    training_data = generator.generate_student_data(200)
    
    # Treinar modelo
    metrics = predictor.train_models(training_data)
    print("Métricas de treinamento:", metrics)
    
    # Testar predição
    test_student = {
        'attendance_rate': 0.85,
        'study_hours_per_week': 15,
        'previous_gpa': 3.2,
        'assignments_completed': 85,
        'participation_score': 78,
        'quiz_average': 82,
        'difficulty_level': 3,
        'extracurricular_activities': 1
    }
    
    prediction = predictor.predict_student_risk(test_student)
    print("Predição do estudante:", prediction)
    
    # Identificar todos os alunos em risco
    all_students = generator.generate_student_data(50)
    at_risk = predictor.identify_at_risk_students(all_students)
    print("Alunos em risco:", len(at_risk[at_risk['risk_level'] == "Alto risco"]))