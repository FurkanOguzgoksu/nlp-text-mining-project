import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Veriyi yükle
df = pd.read_csv("data/cleaned_turkish_reviews.csv")

# 🔥 NaN satırları kaldır
df = df.dropna(subset=["cleaned", "label"])

# Giriş ve çıkışları ayır
X = df["cleaned"]
y = df["label"]

# Vektörleştir
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Eğitim/test böl
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Modeli eğit
model = MultinomialNB()
model.fit(X_train, y_train)

# Tahmin yap
y_pred = model.predict(X_test)

# Sonuçları yazdır
print("🎯 Doğruluk:", accuracy_score(y_test, y_pred))
print("🧾 Sınıflandırma Raporu:\n", classification_report(y_test, y_pred))