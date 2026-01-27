from transformers import pipeline
import pandas as pd
from rich import print

# Veri kümesini oku
df = pd.read_csv("data/turkish_reviews.csv")

# Yorumları al
yorumlar = df["text"].dropna().tolist()

# İlk 10 yorumu test için al
yorumlar = yorumlar[:10]

# Türkçe duygu analizi pipeline'ı (HuggingFace üzerinden)
sentiment_pipeline = pipeline("sentiment-analysis", model="savasy/bert-base-turkish-sentiment-cased")

print("🧠 [bold]Transformer Tabanlı Duygu Analizi Sonuçları (İlk 10 yorum):[/bold]\n")

for i, yorum in enumerate(yorumlar):
    try:
        sonuc = sentiment_pipeline(yorum[:512])[0]  # max 512 karakter
        print(f"🔸 [bold]Yorum {i+1}:[/bold] {yorum[:80]}...")
        print(f"    ➤ Tahmin: [green]{sonuc['label']}[/green], [yellow]{sonuc['score']:.2f}[/yellow]\n")
    except Exception as e:
        print(f"❌ Yorum {i+1} analiz edilemedi: {e}\n")