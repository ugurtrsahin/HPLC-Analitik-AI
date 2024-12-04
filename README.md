# HPLC-Analitik-AI

Yüksek Performanslı Sıvı Kromatografisi (HPLC) kolon seçimi ve metod optimizasyonunu hızlandırmak için derin öğrenme tabanlı bir açık kaynak projesi. Alıkonma zamanı tahmini, kolon önerisi ve metod optimizasyonu gibi özellikler içerir. İlaç keşfi ve geliştirme süreçlerini hızlandırmayı hedefler.

**Hakkında**

Bu proje, yapay zeka ve makine öğrenimi araçlarını kullanarak HPLC analizlerini kolaylaştırmak için geliştirilmiştir. Bir yazılım geliştiricisi veya yapay zeka uzmanı olmasam da, bu araçların gücünden yararlanarak karmaşık analizleri otomatikleştirmenin mümkün olduğunu gördüm.

**Proje Detayları**

Bu çalışma, Python ve çeşitli veri bilimi kütüphaneleri kullanılarak gerçekleştirilmiştir. HPLC kolonlarının özelliklerinin alıkonma süreleri üzerindeki etkilerini analiz eden bir model geliştirilmiştir. Proje aşağıdaki özellikleri içermektedir:

* **Eksik Veri Analizi:** Veri setindeki eksik değerler analiz edilmiş ve ortalama/en sık görülen değer ile doldurulmuştur.
* **Görselleştirme Teknikleri:** Verileri ve analiz sonuçlarını anlamak için `matplotlib` ve `seaborn` kütüphaneleri kullanılmıştır.  HSM parametrelerinin dağılımları, retention süreleri ile ilişkileri ve özellik önemlilikleri görselleştirilmiştir.
* **İstatistiksel Analizler (ANOVA):** Farklı kolon tiplerinin alıkonma süreleri üzerindeki etkisi ANOVA testi ile analiz edilmiştir.
* **Random Forest Regressor Modeli:** Alıkonma süresini tahmin etmek için bir Random Forest Regressor modeli eğitilmiştir. Model, hiperparametre ayarlaması yapılmadan `n_estimators=100` ve `random_state=42` ile kullanılmıştır.
* **Özellik Önemliliği Analizi:** Kolon parametrelerinin alıkonma süresi üzerindeki etkileri, Random Forest modelinin özellik önemliliği değerleri kullanılarak incelenmiştir.

**Kullanılan Teknolojiler**

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Scipy

**Kurulum**

1. Projeyi klonlayın: `git clone https://github.com/ugurtrsahin/HPLC-Analitik-AI.git`
2. Gerekli kütüphaneleri yükleyin: `pip install -r requirements.txt` (requirements.txt dosyasını oluşturmanız ve gerekli kütüphaneleri eklemeniz gerekmektedir.)
3. `kolon.csv` dosyasını projenin ana dizinine yerleştirin.

**Kullanım**

1. `kolon.csv` dosyasını uygun şekilde düzenleyin ve kaydedin.
2. Python scriptini çalıştırın: `python hplc_analiz.py` (Scriptinizin adını uygun şekilde değiştirin.)

**Katkıda Bulunma**

Projeye katkıda bulunmak isteyenler, pull request gönderebilir veya issue açabilirler.

**Lisans**

[MIT Lisansı](https://choosealicense.com/licenses/mit/)

**İletişim**

Uğur Şahin - [ugursahin@example.com](mailto:ugursahin@example.com) (E-posta adresinizi ekleyin)

**Çalışma Sayfası**

[Notion Sayfası](https://ugurtrsahin.notion.site/HPLC-Kolon-Se-iminde-Derin-renme-Yakla-m-H-zland-r-lm-Metod-Geli-tirme-ve-Validasyon-111b6792444f807facc9c4b82de81d94?pvs=4)
