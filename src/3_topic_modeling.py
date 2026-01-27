import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = list(stopwords.words('turkish'))  # <-- DÜZELTİLDİ

# Veriyi oku
df = pd.read_csv("data/cleaned_turkish_reviews.csv")
df = df.dropna(subset=["cleaned"])

# Vektörleştir
vectorizer = CountVectorizer(stop_words=stop_words, max_df=0.95, min_df=2)
X = vectorizer.fit_transform(df["cleaned"])

# LDA Modeli
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(X)

# Konuları yazdır
feature_names = vectorizer.get_feature_names_out()
for index, topic in enumerate(lda.components_):
    print(f"📌 Konu {index+1}:")
    print([feature_names[i] for i in topic.argsort()[:-11:-1]])
    print()