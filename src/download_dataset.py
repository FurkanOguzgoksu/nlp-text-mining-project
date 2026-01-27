import os
from datasets import load_dataset
import pandas as pd

# Veri setini Hugging Face'den yükle
dataset = load_dataset("winvoker/turkish-sentiment-analysis-dataset")

# Sadece 'train' kısmını al ve DataFrame'e çevir
df = dataset['train'].to_pandas()

# 20.000 satır örnek seç (çok büyük olmasın diye)
df = df.sample(20000, random_state=42)

# Sadece gerekli sütunları al ve etiketleri daha okunur hale getir
df = df[['text', 'label']]
df['label'] = df['label'].replace({0: 'negative', 1: 'neutral', 2: 'positive'})

# CSV olarak kaydet (önce data/ klasörünün olduğuna emin ol)
df.to_csv("data/turkish_reviews.csv", index=False)

print("✅ Veri seti başarıyla indirildi ve data/turkish_reviews.csv dosyasına kaydedildi.")