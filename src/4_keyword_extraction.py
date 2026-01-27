import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

# Veri setini yükle
df = pd.read_csv("data/cleaned_turkish_reviews.csv")
yorumlar = df["cleaned"].dropna().tolist()

# Türkçe stopwords
stop_words = stopwords.words("turkish")

# TF-IDF vektörleştirici
vectorizer = TfidfVectorizer(stop_words=stop_words, max_features=10)

# İlk 10 yorumun analizini yap
print("🔑 Örnek Anahtar Kelimeler (İlk 10 yorumdan):\n")

for i, yorum in enumerate(yorumlar[:10], 1):
    try:
        tfidf_matrix = vectorizer.fit_transform([yorum])
        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]
        top_keywords = sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)
        kelimeler = [k for k, s in top_keywords if s > 0]
        print(f"🔸 Yorum {i}: {', '.join(kelimeler[:5])}")
    except Exception as e:
        print(f"❌ Yorum {i} analiz edilemedi: {e}")