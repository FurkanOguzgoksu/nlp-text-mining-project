import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

df = pd.read_csv("data/turkish_reviews.csv")

def temizle(metin):
    metin = metin.lower()
    metin = re.sub(r"http\S+|www\S+|https\S+", "", metin)
    metin = metin.translate(str.maketrans('', '', string.punctuation))
    metin = re.sub(r'\d+', '', metin)
    kelimeler = metin.split()  # Burada word_tokenize yerine split kullandık
    kelimeler = [k for k in kelimeler if k not in stopwords.words('turkish')]
    return " ".join(kelimeler)

df["cleaned"] = df["text"].apply(temizle)
df.to_csv("data/cleaned_turkish_reviews.csv", index=False)

print("✅ Temizleme tamamlandı. Yeni dosya: data/cleaned_turkish_reviews.csv")