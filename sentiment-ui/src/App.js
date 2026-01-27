import React, { useState } from "react";
import axios from "axios";

function App() {
  const [yorum, setYorum] = useState("");
  const [sonuc, setSonuc] = useState(null);
  const [goster, setGoster] = useState(false);

  const tahminEt = async () => {
    setGoster(false);
    try {
      const response = await axios.post("http://127.0.0.1:5000/tahmin", { yorum });
      setSonuc(response.data);
      setTimeout(() => setGoster(true), 100);
    } catch (error) {
      console.error("Hata:", error);
      setSonuc(null);
      setGoster(false);
    }
  };

  return (
    <div
      style={{
        backgroundColor: "#000",
        color: "#fff",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        paddingTop: "60px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h2 style={{ marginBottom: "20px", textAlign: "center" }}>
        🛍️ Ürün Yorumları Üzerinden Duygu Analizi
      </h2>

      <textarea
        value={yorum}
        onChange={(e) => setYorum(e.target.value)}
        placeholder="Yorumunuzu buraya yazın..."
        style={{
          width: "600px",
          height: "120px",
          padding: "10px",
          fontSize: "16px",
          borderRadius: "8px",
          border: "none",
          resize: "vertical",
          marginBottom: "20px",
        }}
      />

      <button
        onClick={tahminEt}
        style={{
          backgroundColor: "#007bff",
          color: "white",
          padding: "10px 24px",
          border: "none",
          borderRadius: "6px",
          fontSize: "16px",
          cursor: "pointer",
          marginBottom: "30px",
        }}
      >
        Tahmin Et
      </button>

      {/* Sonuç kutusu her zaman aynı pozisyonda görünür */}
      <div
        style={{
          backgroundColor: "#1e1e1e",
          padding: "20px 30px",
          borderRadius: "16px",
          boxShadow: "0 0 10px rgba(255, 255, 255, 0.1)",
          width: "600px",
          textAlign: "left",
          opacity: goster ? 1 : 0,
          transform: goster ? "translateY(0px)" : "translateY(20px)",
          transition: "opacity 0.5s ease, transform 0.5s ease",
          minHeight: "120px",
        }}
      >
        {sonuc ? (
          <>
            <h3 style={{ display: "flex", alignItems: "center", gap: "8px" }}>
              🔍 Tahmin Sonucu
            </h3>
            <p><strong>📄 Yorum:</strong> {sonuc.yorum}</p>
            <p>
              <strong>📌 Tahmin:</strong>{" "}
              <span style={{ color: sonuc.tahmin === "positive" ? "lightgreen" : "red" }}>
                {sonuc.tahmin}
              </span>
            </p>
            <p><strong>✏️ Güven:</strong> {sonuc.guven}</p>
          </>
        ) : (
          <p style={{ color: "#888" }}>Henüz bir tahmin yapılmadı.</p>
        )}
      </div>
    </div>
  );
}

export default App;