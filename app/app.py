from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # CORS tanımı app'ten sonra gelmeli

# Modeli yüklemeyi deneyelim
try:
    classifier = pipeline("text-classification", model="savasy/bert-base-turkish-sentiment-cased")
except Exception as e:
    print(f"❌ Model yüklenemedi: {e}")
    classifier = None  # Model yüklenemediyse None yap

@app.route('/tahmin', methods=['POST'])
def tahmin():
    veri = request.get_json()
    yorum = veri.get("yorum")

    if not yorum:
        return jsonify({"hata": "Yorum metni eksik!"}), 400

    if classifier is None:
        return jsonify({"hata": "Model yüklenemedi, sunucu yeniden başlatılmalı!"}), 500

    try:
        sonuc = classifier(yorum)[0]
        return jsonify({
            "yorum": yorum,
            "tahmin": sonuc['label'],
            "guven": round(sonuc['score'], 3)
        })
    except Exception as e:
        return jsonify({"hata": f"Tahmin sırasında hata oluştu: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)