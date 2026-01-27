<<<<<<< HEAD
# nlp-text-mining-project-main
=======
## Turkish Sentiment Analysis - NLP Text Mining Project 🇹🇷🧠

Bu proje, **Türkçe kullanıcı yorumlarının duygu analizi** için hazırlanmış bir metin madenciliği uygulamasıdır. Proje kapsamında veri ön işleme, konu modelleme, anahtar kelime çıkarımı ve BERT tabanlı duygu analizi gerçekleştirilmiştir. Sonuçlar React tabanlı şık bir arayüzde sunulmuştur.

---

## 📦 Kullanılan Veri Seti

- Dataset: [`winvoker/turkish-sentiment-analysis-dataset`](https://huggingface.co/datasets/winvoker/turkish-sentiment-analysis-dataset)
- İçerik: Türkçe ürün, otel, film vb. yorumlar
- Format: CSV dosyası (`data/turkish_reviews.csv`)
- Kolon: `text` (yorum metni), `label` (duygu etiketi)

---

## ⚙️ Uygulama Bileşenleri

### 1. Ön İşleme & Görselleştirme
- `1_preprocessing.py`: Temizlik, küçük harfe çevirme, durak kelimeleri kaldırma
- `2_visualization.py`: Kelime bulutu, etiket dağılımı grafikleri

### 2. Konu Modelleme
- `3_topic_modeling.py`: LDA ile yorumlardan başlıca konuların çıkarımı

### 3. Anahtar Kelime Çıkarımı
- `4_keyword_extraction.py`: RAKE algoritmasıyla yorumlardan anlamlı anahtar kelimeler

### 4. Transformer Tabanlı Duygu Analizi
- `5_transformer_sentiment.py`: Hugging Face `savasy/bert-base-turkish-sentiment-cased` modeliyle yorumların analiz edilmesi

---

## 🌐 Web Arayüzü

- React ile geliştirilmiş kullanıcı dostu arayüz
- Kullanıcı yorumu girildiğinde Flask API'ye istek gönderilir
- Yorumun pozitif/negatif olup olmadığı ekranda animasyonla gösterilir
- Siyah temalı modern UI

---

## 🚀 Başlatma Adımları

### 1. Backend (Flask)
```bash
cd nlp-text-mining-project
pip install -r requirements.txt
python app.py
```

### 2. Frontend (React)
```bash
cd sentiment-ui
npm install
npm start
```

---

## 📌 Kullanılan Teknolojiler

- Python (Flask, Pandas, NLTK, Transformers)
- React (Axios, Animate.css, Tailwind CSS)
- Hugging Face Transformers
- Turkish NLP Tools

---

## ✨ Ekran Görüntüsü

Ana sayfa + sonuç ekranı arayüzü:

<img width="973" alt="Ekran Resmi 2025-06-10 18 30 29" src="https://github.com/user-attachments/assets/dc34c0f4-6c1b-4145-a72a-00ca510abc2c" />



---

## 📚 Kaynakça

- [HuggingFace Datasets](https://huggingface.co/datasets)
- [Savasy - Turkish BERT](https://huggingface.co/savasy/bert-base-turkish-sentiment-cased)
- [RAKE Algorithm](https://github.com/aneesha/RAKE)

--- 
>>>>>>> 48c9a09 (Initial commit)
