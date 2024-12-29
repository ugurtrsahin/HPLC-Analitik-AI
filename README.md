# HPLC Column Selection Using Machine Learning

[[![License: Apache](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)](https://opensource.org/license/apache-2-0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)

Bu proje, Yüksek Performanslı Sıvı Kromatografisi (HPLC) kolon seçim sürecini optimize etmek için makine öğrenimi tekniklerini kullanmaktadır. 780 farklı HPLC kolonunun özelliklerini analiz ederek, en uygun kolon seçimini otomatize etmeyi amaçlamaktadır.

## 🚀 Özellikler

- HPLC kolon özelliklerinin kapsamlı analizi
- Hidrofobik Çıkarma Modeli (HSM) parametrelerinin değerlendirilmesi
- Random Forest regresyon modeli ile retention zamanı tahmini
- Detaylı görselleştirmeler ve istatistiksel analizler
- Kolon seçimi için otomatik öneriler

## 📊 Performans

- Model R-kare skoru: 0.7057
- Ortalama Kare Hata (MSE): 4.2791

## 🛠️ Kurulum

```bash
# Repository'yi klonlayın
git clone https://github.com/yourusername/HPLC-Analitik-AI.git
cd HPLC-Column-Selection

# Sanal ortam oluşturun ve aktive edin
python -m venv venv
source venv/bin/activate  # Linux/Mac için
venv\Scripts\activate  # Windows için

# Gerekli paketleri yükleyin
pip install -r requirements.txt
```

## 💻 Kullanım

```python
from src.model import HPLCColumnPredictor

# Model nesnesini oluşturun
predictor = HPLCColumnPredictor()

# Veriyi yükleyin ve modeli eğitin
predictor.train('data/raw/kolon.csv')

# Yeni bir kolon için tahmin yapın
prediction = predictor.predict({
    'H': 1.08,
    'S': 0.05,
    'A': 0.47,
    'B': 0.06,
    'C28': 1.48,
    'C70': 1.56
})
```

## 📁 Veri Seti

Veri seti 780 HPLC kolonunun özelliklerini içermektedir:
- HSM parametreleri (H, S, A, B, C28, C70)
- Retention değerleri
- Kolon tipleri ve fazları
- Üretici bilgileri

## 📈 Sonuçlar

Projemizin ana bulguları:
1. Hidrofobiklik (H) parametresi retention zamanı üzerinde en etkili faktördür
2. Kolon tipleri arasında anlamlı performans farkları bulunmaktadır
3. Model, kolon seçimini optimize ederek zaman ve maliyet tasarrufu sağlamaktadır

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## ✉️ İletişim

Uğur Şahin - [ugur.tr.sahin@gmail.com](mailto:ugurtrsahin@gmail.com)

Project Link: [https://github.com/ugurtrsahin/HPLC-Analitik-AI](https://github.com/ugurtrsahin/HPLC-Analitik-AI)

[Notion Sayfası](https://ugurtrsahin.notion.site/HPLC-Kolon-Se-iminde-Derin-renme-Yakla-m-H-zland-r-lm-Metod-Geli-tirme-ve-Validasyon-111b6792444f807facc9c4b82de81d94?pvs=4)

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.



