# 🇹🇷 Turkish Sentiment Analysis - NLP Text Mining Project 🧠

Bu proje, Türkçe metinler üzerinde kapsamlı Doğal Dil İşleme (NLP) analizleri gerçekleştiren, makine öğrenmesi ve derin öğrenme tekniklerini kullanarak duygu analizi yapan entegre bir sistemdir. Geliştirilen sistem, hem ham veri üzerinde çeşitli metin madenciliği tekniklerini uygular hem de eğitilen modeli modern bir web arayüzü üzerinden son kullanıcıya sunar.

Proje, veri bilimciler ve geliştiriciler için uçtan uca bir NLP pipeline'ı (boru hattı) örneği teşkil eder. Veri toplama, temizleme, modelleme ve canlıya alma (deployment) aşamalarının tamamını kapsar.

---

## 🚀 Temel Özellikler

### 🌐 Web Uygulaması (Sentiment UI & API)
- **BERT Tabanlı Analiz:** Google'ın BERT mimarisi kullanılarak eğitilmiş `bert-base-turkish-sentiment-cased` modeli ile yüksek doğruluklu (state-of-the-art) duygu analizi.
- **Güven Skoru (Confidence Score):** Modelin yaptığı tahminin ne kadar güvenilir olduğunu gösteren yüzdelik skor.
- **Etkileşimli Arayüz:** Kullanıcı deneyimi odaklı, React ile geliştirilmiş, sonuçları renk kodlarıyla (Yeşil/Kırmızı) görselleştiren arayüz.
- **RESTful Mimari:** Flask ile hazırlanmış, kolayca genişletilebilir ve başka uygulamalarla entegre edilebilir JSON tabanlı API.

### 🔬 İleri Seviye NLP Analizleri (src/)
- **Kapsamlı Veri Ön İşleme:** Metin temizliği, küçük harfe çevirme, noktalama işareti temizliği ve stopwords (etkisiz kelimeler) filtreleme işlemleri.
- **Konu Modelleme (LDA):** Latent Dirichlet Allocation algoritması kullanılarak binlerce yorumun otomatik olarak konu başlıklarına ayrıştırılması.
- **Anahtar Kelime Çıkarımı (RAKE):** Rapid Automatic Keyword Extraction algoritması ile metinlerde geçen en kritik ve belirleyici ifadelerin istatistiksel olarak tespiti.
- **Karşılaştırmalı Analiz:** Lojistik Regresyon, Naive Bayes gibi geleneksel ML modelleri ile Transformer tabanlı modellerin performans karşılaştırması.

---

## 📂 Detaylı Proje Yapısı

```
nlp-text-mining-project/
├── app/                              # Flask Backend Servisi
│   └── app.py                        # Uygulamanın giriş noktası. BERT modelini yükler ve 
│                                     # '/tahmin' endpoint'ini dış dünyaya açar.
│
├── data/                             # Veri Deposu
│   ├── turkish_reviews.csv           # Ham, işlenmemiş kullanıcı yorumlarını içeren orijinal veri seti.
│   └── cleaned_turkish_reviews.csv   # Ön işleme (preprocessing) adımlarından geçirilmiş, 
│                                     # model eğitimine hazır temizlenmiş veri seti.
│
├── sentiment-ui/                     # React Frontend Uygulaması
│   ├── src/                          # React bileşenleri, sayfalar ve stil dosyaları.
│   ├── public/                       # HTML şablonu ve favicon gibi statik varlıklar.
│   └── package.json                  # Frontend proje bağımlılıkları ve scriptleri.
│
├── src/                              # NLP ve Veri Bilimi Scriptleri
│   ├── 1_data_preprocessing.py       # Ham veriyi temizleyip 'cleaned_turkish_reviews.csv' 
│   |                                 # dosyasına dönüştüren script.
│   ├── 2_sentiment_classification.py # TF-IDF ve geleneksel ML algoritmaları (Logistic Regression vb.)
│   |                                 # ile temel sınıflandırma modellerini eğitir.
│   ├── 3_topic_modeling.py           # LDA algoritması ile yorumlardaki gizli konu öbeklerini
│   |                                 # keşfeder ve görselleştirir.
│   ├── 4_keyword_extraction.py       # RAKE algoritması kullanarak metinlerdeki önemli
│   |                                 # anahtar kelimeleri ve öbekleri çıkarır.
│   ├── 5_transformer_sentiment.py    # BERT modeli ile ileri seviye duygu analizi ve
│   |                                 # modelin performans değerlendirmesini yapar.
│   └── download_dataset.py           # Hugging Face üzerinden gerekli veri setini otomatik
|                                      # olarak indiren yardımcı araç.
|
├── project-detail.jpeg               # Proje mimarisi veya akışını gösteren detaylı görsel.
└── requirements.txt                  # Projenin çalışması için gerekli tüm Python kütüphaneleri
                                      # (Flask, Torch, Transformers, Pandas, NLTK vb.).
```

---

## 🛠️ Kurulum ve Çalıştırma Rehberi

Projeyi yerel ortamınızda eksiksiz çalıştırmak için aşağıdaki adımları sırasıyla uygulayın.

### Ön Gereksinimler
- **Python 3.8** veya üzeri
- **Node.js** (Frontend için)
- **Git**

### 1. Projeyi Kopyalayın (Clone)
```bash
git clone https://github.com/FurkannOguz/nlp-text-mining-project.git
cd nlp-text-mining-project-main
```

### 2. Backend (API) Kurulumu
API sunucusu, yapay zeka modelini barındırır ve frontend'den gelen isteklere cevap verir.

```bash
# Sanal ortam oluşturma (Opsiyonel ama önerilir)
python -m venv venv
# Windows için aktivasyon: venv\Scripts\activate
# Mac/Linux için aktivasyon: source venv/bin/activate

# Gerekli Python kütüphanelerini yükleyin
pip install -r requirements.txt

# API sunucusunu başlatın
python app/app.py
```
*Not: İlk çalıştırmada BERT modeli (~440MB) indirileceği için internet hızınıza bağlı olarak biraz bekleyebilirsiniz. Sunucu açıldığında `http://127.0.0.1:5000` adresinde aktif olacaktır.*

### 3. Frontend (Arayüz) Kurulumu
Kullanıcı arayüzünü çalıştırmak için yeni bir terminal penceresi açın.

```bash
cd sentiment-ui

# Gerekli Node modüllerini yükleyin
npm install

# Geliştirme sunucusunu başlatın
npm start
```
*Komut sonrası tarayıcınızda otomatik olarak `http://localhost:3000` adresi açılacaktır. Açılmazsa manuel olarak gidebilirsiniz.*

### 4. Analiz Scriptlerini Çalıştırma (Opsiyonel)
Eğer modelin nasıl eğitildiğini görmek veya veriyi kendiniz işlemek isterseniz `src` klasöründeki scriptleri sırasıyla çalıştırabilirsiniz.

**Örnek: Veriyi Temizleme**
```bash
python src/1_data_preprocessing.py
# Bu işlem sonucunda data/cleaned_turkish_reviews.csv dosyası oluşur/güncellenir.
```

**Örnek: Konu Analizi Yapma**
```bash
python src/3_topic_modeling.py
# Yorumların konulara göre dağılımını analiz eder.
```

**Örnek: Anahtar Kelime Çıkarımı (RAKE)**
```bash
python src/4_keyword_extraction.py
# Metinlerdeki öne çıkan anahtar kelimeleri RAKE algoritması ile listeler.
```

---

## 📌 Kullanılan Teknolojiler ve Kütüphaneler

| Alan | Teknoloji / Kütüphane | Kullanım Amacı |
|------|-----------------------|----------------|
| **Backend** | Python, Flask, Flask-CORS | REST API Servisi, Backend mantığı |
| **Frontend** | React.js, Axios, CSS3 | Dinamik Kullanıcı Arayüzü |
| **Derin Öğrenme** | Hugging Face Transformers, PyTorch | BERT Model Entegrasyonu |
| **NLP** | NLTK (Natural Language Toolkit) | Metin işleme, Stopwords temizliği |
| **Veri Bilimi** | Pandas, NumPy, Scikit-learn | Veri manipülasyonu ve ML modelleri |
| **Algoritmalar** | LDA, RAKE, TF-IDF | Konu modelleme ve anahtar kelime çıkarımı |

---

## ✨ Ekran Görüntüsü

Aşağıda projenin çalışan arayüzünden bir örnek görülmektedir:

<img width="973" alt="Uygulama Ekran Görüntüsü" src="https://github.com/user-attachments/assets/dc34c0f4-6c1b-4145-a72a-00ca510abc2c" />

---

## 📚 Kaynakça ve Atıflar

Projede kullanılan veri setleri ve temel modeller:

- **BERT Modeli:** [savasy/bert-base-turkish-sentiment-cased](https://huggingface.co/savasy/bert-base-turkish-sentiment-cased) - Türkçe duygu analizi için özelleştirilmiş model.
- **Veri Seti:** [Turkish Sentiment Analysis Dataset](https://huggingface.co/datasets/winvoker/turkish-sentiment-analysis-dataset) - Çeşitli alanlardan toplanmış etiketli Türkçe yorumlar.
- **Algoritma:** [RAKE (Rapid Automatic Keyword Extraction)](https://github.com/csurfer/rake-nltk) - Anahtar kelime çıkarımı için kullanılan algoritma kütüphanesi.
