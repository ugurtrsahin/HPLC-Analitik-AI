import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer

class HPLCColumnPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.numeric_imputer = SimpleImputer(strategy='mean')
        self.categorical_imputer = SimpleImputer(strategy='most_frequent')
        self.hsm_parameters = ['H', 'S', 'A', 'B', 'C28', 'C70']
        
    def preprocess_data(self, df):
        """Veri ön işleme fonksiyonu"""
        # Sayısal ve kategorik kolonları ayır
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        categorical_columns = df.select_dtypes(exclude=[np.number]).columns
        
        # Eksik değerleri doldur
        df[numeric_columns] = self.numeric_imputer.fit_transform(df[numeric_columns])
        df[categorical_columns] = self.categorical_imputer.fit_transform(df[categorical_columns])
        
        # Kategorik değişkenleri one-hot encoding ile dönüştür
        df_encoded = pd.get_dummies(df, columns=['type', 'USPtype', 'phase'])
        
        return df_encoded
        
    def train(self, data_path):
        """Modeli eğiten fonksiyon"""
        # Veriyi yükle
        df = pd.read_csv(data_path, encoding='latin-1')
        
        # Veriyi ön işle
        df_processed = self.preprocess_data(df)
        
        # Özellikler ve hedef değişkeni ayır
        X = df_processed.drop(['id', 'name', 'manufacturer', 'retention'], axis=1)
        y = df_processed['retention']
        
        # Eğitim ve test setlerini ayır
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Verileri ölçeklendir
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Modeli eğit
        self.model.fit(X_train_scaled, y_train)
        
        # Model performansını hesapla
        y_pred = self.model.predict(X_test_scaled)
        self.r2_score = r2_score(y_test, y_pred)
        self.mse = mean_squared_error(y_test, y_pred)
        
        return self.r2_score, self.mse
    
    def predict(self, features):
        """Yeni bir kolon için tahmin yapan fonksiyon"""
        # Özellikleri DataFrame'e çevir
        df = pd.DataFrame([features])
        
        # Eksik HSM parametrelerini kontrol et
        for param in self.hsm_parameters:
            if param not in features:
                raise ValueError(f"Missing HSM parameter: {param}")
        
        # Verileri ölçeklendir
        scaled_features = self.scaler.transform(df)
        
        # Tahmin yap
        prediction = self.model.predict(scaled_features)
        
        return prediction[0]
    
    def get_feature_importance(self):
        """Özellik önemliliklerini döndüren fonksiyon"""
        feature_importance = pd.DataFrame({
            'feature': self.model.feature_names_in_,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        return feature_importance
