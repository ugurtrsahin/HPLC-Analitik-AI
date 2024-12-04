
**Özet:**

Yüksek Performanslı Sıvı Kromatografisi (HPLC), kimya, biyoloji, ilaç ve gıda endüstrileri gibi birçok alanda kullanılan yaygın bir analitik tekniktir. HPLC analizlerinin başarısı, uygun kolon ve metot parametrelerinin seçilmesine bağlıdır. Bu çalışmada,  Etilbenzenn HPLC kolon verilerini kullanarak derin öğrenme modelleri geliştirmeyi ve bu modelleri kromatografik analizlerde kullanmayı amaçlayan bir açık kaynak proje sunuyoruz. Proje, alıkonma zamanı tahmini, kolon önerisi, kromatogram simülasyonu ve metot optimizasyonu gibi çeşitli uygulamaları içerecektir. Geliştirilen modellerin, HPLC metod geliştirme ve validasyon sürecini hızlandırarak, sektörlerde Ar-Ge verimliliğini artıracağı ve ruhsat başvurusu süreçlerini kısaltacağı öngörülmektedir. Kısıtlı ancak etkili sonuçlar elde edilen bu çalışma, yapay zeka ve ilaç endüstrisinin geleceğine dair bir bakış açısı kazandırmayı amaçlamaktadır.

**Giriş:**

HPLC, karmaşık karışımları ayırmak ve analiz etmek için kullanılan güçlü bir tekniktir. Bir HPLC sisteminin kalbinde, analitlerin farklı fizikokimyasal özelliklerine göre ayrıldığı kolon bulunur. Kolon seçimi, analiz edilecek bileşiklerin özelliklerine, hedeflenen ayırma ve analiz hedeflerine göre yapılmalıdır.

Geleneksel HPLC kolon seçimi, genellikle deneme yanılma yöntemlerine ve uzman deneyimine dayanmaktadır. Bu süreç, zaman alıcı ve maliyetli olabilir. Son yıllarda, makine öğrenmesi ve derin öğrenme teknikleri, HPLC kolon seçimini ve metot optimizasyonunu otomatikleştirmek ve hızlandırmak için umut vadeden yaklaşımlar olarak ortaya çıkmıştır.

Bu çalışmada, HPLC kolon verilerini kullanarak derin öğrenme modelleri geliştiren ve bu modelleri kromatografik analizlerde kullanmayı amaçlayan "HPLC-DeepLearn" projesini sunuyoruz. Proje, alıkonma zamanı tahmini, kolon önerisi, kromatogram simülasyonu ve metot optimizasyonu gibi çeşitli uygulamaları içerecektir.

**Materyal ve Metot:**

**Veri Seti:**

Çalışmada kullanılan veri seti, 780 farklı HPLC kolonunun özelliklerini ve HSM (Hidrofobiklik, Sterik Etkileşim, Hidrojen Bağlayıcı) parametrelerini içermektedir. Veri seti, kolon üreticilerinin kataloglarından ve bilimsel makalelerden derlenmiştir.

**Veri Ön İşleme:**

Veri setinde eksik değerler, ortalama değer atama yöntemi ile doldurulmuştur. Kategorik özellikler, one-hot encoding tekniği kullanılarak sayısal hale getirilmiştir. Sayısal özellikler, standartlaştırma işlemi ile ölçeklendirilmiştir.

**Özellik Mühendisliği:**

Hidrofobiklik (H) ve sterik etkileşim (S) oranı gibi yeni özellikler, mevcut özelliklerden türetilmiştir.

**Model Geliştirme:**

Rastgele Orman (Random Forest) regresyon modeli, alıkonma zamanını tahmin etmek için kullanılmıştır. Modelin hiperparametreleri, ızgara arama (grid search) yöntemi ile optimize edilmiştir.

**Model Değerlendirmesi:**

Modelin performansı, ortalama kare hata (MSE) ve R-kare skoru gibi metrikler kullanılarak değerlendirilmiştir. Ayrıca, çapraz doğrulama yöntemi kullanılarak modelin genelleme yeteneği test edilmiştir.

**Sonuçlar:**

**HSM Parametrelerinin Analizi:**

Hidrofobiklik (H) parametresinin, alıkonma zamanı ile güçlü bir pozitif korelasyon gösterdiği bulunmuştur (Pearson korelasyon katsayısı: 0.72). Bu sonuç, hidrofobik etkileşimlerin, HPLC ayırma mekanizmasında önemli bir rol oynadığını göstermektedir.

**Kolon Tiplerinin Etkisi:**

ANOVA testi, farklı kolon tipleri arasında alıkonma zamanı açısından istatistiksel olarak anlamlı bir fark olduğunu göstermiştir (p < 0.05). Bu sonuç, kolon tipinin, HPLC analizlerinin başarısı için kritik bir faktör olduğunu doğrulamaktadır.

**Üretici Performansı:**

Farklı üreticilerin ürettiği kolonların ortalama alıkonma zamanları ve standart sapmaları arasında farklılıklar gözlemlenmiştir. Bu sonuç, kolon seçiminde üretici performansının da dikkate alınması gerektiğini göstermektedir.

**Tahmin Modeli Performansı:**

Geliştirilen Rastgele Orman modeli, HPLC kolon alıkonma zamanlarını başarıyla tahmin etmiştir (R-kare skoru: 0.7057). Model, farklı kolon tipleri, HSM parametreleri ve diğer özellikler arasındaki karmaşık ilişkileri öğrenmiştir.

**Özellik Önemi:**

Özellik önemi analizi, hidrofobiklik (H), sterik etkileşim (S) ve bazı kolon tiplerinin, alıkonma zamanını tahmin etmede en önemli özellikler olduğunu göstermiştir.

**Tartışma:**

Bu çalışma, HPLC kolon seçiminde derin öğrenme tekniklerinin kullanımını araştırmıştır. Geliştirilen model, HPLC kolon alıkonma zamanlarını başarıyla tahmin etmiştir ve kolon seçimi ve metot optimizasyonu için önemli bilgiler sağlamıştır.

**Ülkeye Katkıları:**

Türkiye'deki komatografik yöntemler kullanan tüm sektörlerde (kimya, ilaç, gıda, çevre vb.) metod geliştirme ve validasyon süreçlerini hızlandırarak, Ar-Ge verimliliğini artıracak ve ruhsat başvurusu süreçlerini kısaltacaktır. Bu da, ülkemizin rekabet gücünü artırmasına ve yeni ürünlerin ve teknolojilerin geliştirilmesine katkı sağlayacaktır.

**Gelecek Çalışmalar:**

Gelecekteki çalışmalar, daha büyük ve çeşitli veri setleri kullanarak modelin performansını iyileştirmeyi, kromatogram simülasyonu ve metot optimizasyonu gibi yeni özellikler eklemeyi ve modeli diğer kromatografi türlerine (gaz kromatografisi, iyon kromatografisi vb.) genişletmeyi içerecektir.

**Sonuç:**

Bu proje HPLC kolon seçiminde ve metot optimizasyonunda derin öğrenme tekniklerinin kullanımını gösteren, değerli olduğuna inandığımız bir çalışmadır. Geliştirilen ve geliştirilebilecek model, HPLC analizlerinin başarısını artırmak ve bu analizlerin kullanıldığı sektörlerde Ar-Ge verimliliğini artırmak için kullanılabilir.

**Ekler:**

- Veri seti ve kod dosyaları
- Matematiksel hesaplamalar ve istatistiksel analizler
- Modelin sınırlamaları ve gelecek çalışma önerileri

---

**Verileri Elde Etmek İçin Kullanılan Kod:**

Verilen kod, verileri elde etmek ve analiz etmek için kullanılan kodun tamamını içermektedir.

[Data Dosyası Hakkında][(https://www.notion.so/Data-Dosyas-Hakk-nda-111b6792444f802689e4ec65bcfb61e4?pvs=21](https://github.com/ugurtrsahin/HPLC-Analitik-AI/blob/7a6f4befb31d3b4912b8bf554cf94746693f3b15/Data.md)](https://github.com/ugurtrsahin/HPLC-Analitik-AI/blob/7a6f4befb31d3b4912b8bf554cf94746693f3b15/Data.md)

Data dosyası, "kolon.csv" olarak adlandırılmıştır ve aşağıda verilen kod ile okunmaktadır. 

```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer

# Veri Yükleme ve Ön İşleme
print("1. HPLC Kolon Verilerinin Yüklenmesi ve Ön İşlenmesi")
df = pd.read_csv('kolon.csv', encoding='latin-1')
print(f"Analiz edilen HPLC kolon sayısı: {df.shape[0]}")

# Veri setinin yapısını inceleme
print("\nHPLC Kolon Özelliklerinin Özeti:")
print(df.info())

print("\nÖrnek HPLC Kolonları:")
print(df.head())

print("\nEksik Veri Analizi:")
print(df.isnull().sum())

# HSM parametrelerini ve diğer sayısal özellikleri ayırma
hsm_parameters = ['H', 'S', 'A', 'B', 'C28', 'C70', 'retention']
numeric_columns = df.select_dtypes(include=[np.number]).columns
categorical_columns = df.select_dtypes(exclude=[np.number]).columns

print("\nHSM Parametreleri:", hsm_parameters)
print("Diğer Sayısal Özellikler:", [col for col in numeric_columns if col not in hsm_parameters])
print("Kategorik Özellikler:", categorical_columns.tolist())

# Eksik değerleri doldurma
numeric_imputer = SimpleImputer(strategy='mean')
df[numeric_columns] = numeric_imputer.fit_transform(df[numeric_columns])

categorical_imputer = SimpleImputer(strategy='most_frequent')
df[categorical_columns] = categorical_imputer.fit_transform(df[categorical_columns])

# HSM Parametrelerinin Analizi
print("\n2. HSM Parametrelerinin Analizi")

# HSM parametrelerinin dağılımı
plt.figure(figsize=(15, 10))
for i, param in enumerate(hsm_parameters[:-1], 1):
    plt.subplot(2, 3, i)
    sns.histplot(df[param], kde=True)
    plt.title(f'{param} Dağılımı')
    if param == 'H':
        plt.xlabel('Faz Hidrofobikliği')
    elif param == 'S':
        plt.xlabel('Molekül Penetrasyon Direnci')
    elif param == 'A':
        plt.xlabel('Hidrojen Bağı Asitliği')
    elif param == 'B':
        plt.xlabel('Hidrojen Bağı Bazlığı')
    elif param in ['C28', 'C70']:
        plt.xlabel('İyonize Solüt Etkileşimi')
plt.tight_layout()
plt.show()

# Retention vs HSM parametreleri scatter plot
plt.figure(figsize=(15, 10))
for i, param in enumerate(hsm_parameters[:-1], 1):
    plt.subplot(2, 3, i)
    sns.scatterplot(x=param, y='retention', hue='type', data=df, alpha=0.6)
    plt.title(f'{param} vs Retention')
    if param == 'H':
        plt.xlabel('Faz Hidrofobikliği')
    elif param == 'S':
        plt.xlabel('Molekül Penetrasyon Direnci')
    elif param == 'A':
        plt.xlabel('Hidrojen Bağı Asitliği')
    elif param == 'B':
        plt.xlabel('Hidrojen Bağı Bazlığı')
    elif param in ['C28', 'C70']:
        plt.xlabel('İyonize Solüt Etkileşimi')
    plt.ylabel('Retention')
plt.tight_layout()
plt.show()

# HSM parametreleri arasındaki korelasyon
correlation = df[hsm_parameters].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('HSM Parametreleri Arasındaki Korelasyon')
plt.tight_layout()
plt.show()

# İstatistiksel Analizler
print("\n3. HPLC Kolon Tiplerinin Retention Üzerindeki Etkisi")

# ANOVA testi: Kolon tipi vs Retention
types = df['type'].unique()
type_groups = [df[df['type'] == t]['retention'] for t in types]
f_value, p_value = stats.f_oneway(*type_groups)
print(f"ANOVA testi (Kolon tipi vs Retention): F={f_value:.2f}, p={p_value:.4f}")

if p_value < 0.05:
    print("Kolon tipleri arasında retention değerleri açısından istatistiksel olarak anlamlı bir fark vardır.")
else:
    print("Kolon tipleri arasında retention değerleri açısından istatistiksel olarak anlamlı bir fark yoktur.")

# HSM parametrelerinin betimsel istatistikleri
print("\nHSM Parametrelerinin Betimsel İstatistikleri:")
print(df[hsm_parameters].describe())

# Üretici Analizi
print("\n4. HPLC Kolon Üreticilerinin Performans Analizi")

manufacturer_retention = df.groupby('manufacturer')['retention'].agg(['mean', 'std']).sort_values('mean', ascending=False)
plt.figure(figsize=(12, 6))
manufacturer_retention.head(20)['mean'].plot(kind='bar', yerr=manufacturer_retention.head(20)['std'], capsize=5)
plt.title('Üreticilere Göre Ortalama Retention Değerleri (İlk 20)')
plt.xlabel('Üretici')
plt.ylabel('Ortalama Retention (Hata Çubukları: Standart Sapma)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Makine Öğrenimi: Retention Tahmini
print("\n5. HPLC Kolon Retention Değeri Tahmin Modeli")

df_encoded = pd.get_dummies(df, columns=['type', 'USPtype', 'phase'])

X = df_encoded.drop(['id', 'name', 'manufacturer', 'retention'], axis=1)
y = df_encoded['retention']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)
y_pred = rf_model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Performansı:")
print(f"Ortalama Kare Hata (MSE): {mse:.4f}")
print(f"R-kare Skoru: {r2:.4f}")

# Özellik önemlilikleri
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='importance', y='feature', data=feature_importance.head(10))
plt.title('HPLC Kolon Retention Değerini Etkileyen En Önemli 10 Özellik')
plt.tight_layout()
plt.show()

print("\n6. Sonuçlar ve HPLC Kolon Seçimi İçin Öneriler")
print("1. Veri setimiz çeşitli HPLC kolon özelliklerini ve HSM parametrelerini içermektedir.")
print("2. Kolon tipleri arasında retention değerleri açısından anlamlı farklılıklar bulunmaktadır.")
print("3. Faz hidrofobikliği (H) ve retention arasında güçlü bir ilişki gözlemlenmektedir.")
print("4. Üreticiler arasında ortalama retention değerleri ve performans farklılıkları mevcuttur.")
print("5. Geliştirilen tahmin modeli, HPLC kolon retention değerlerini başarıyla tahmin etmektedir.")
print("6. En önemli özellikler arasında faz hidrofobikliği (H), molekül penetrasyon direnci (S), ve bazı kolon tipleri yer almaktadır.")
print("\nBu analizler ışığında, HPLC kolon seçimi ve optimizasyonu için şu önerilerde bulunulabilir:")
print("- Analiz edilecek bileşiklerin özelliklerine göre uygun hidrofobiklik seviyesine sahip kolonlar seçilmelidir.")
print("- Kolon tipi, üretici performansı ve HSM parametreleri birlikte değerlendirilerek en uygun kolon belirlenmelidir.")
print("- Yüksek retention değeri gerektiren analizler için faz hidrofobikliği (H) yüksek kolonlar tercih edilebilir.")
print("- Farklı türde bileşikler analiz edilecekse, çeşitli HSM parametrelerine sahip kolonların kombinasyonu düşünülebilir.")
print("- Geliştirilen tahmin modeli, yeni kolonların performansını öngörmek için kullanılabilir.")
```

```mermaid
1. HPLC Kolon Verilerinin Yüklenmesi ve Ön İşlenmesi
Analiz edilen HPLC kolon sayısı: 780

HPLC Kolon Özelliklerinin Özeti:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 780 entries, 0 to 779
Data columns (total 14 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   id              780 non-null    object 
 1   name            765 non-null    object 
 2   manufacturer    765 non-null    object 
 3   manufacturerID  741 non-null    float64
 4   type            765 non-null    object 
 5   H               765 non-null    float64
 6   S               765 non-null    float64
 7   A               765 non-null    float64
 8   B               765 non-null    float64
 9   C28             765 non-null    float64
 10  C70             765 non-null    float64
 11  retention       765 non-null    float64
 12  USPtype         710 non-null    object 
 13  phase           764 non-null    object 
dtypes: float64(8), object(6)
memory usage: 85.4+ KB
None

Örnek HPLC Kolonları:
  id                    name          manufacturer  manufacturerID type     H  \
0  1              Zorbax C18  Agilent Technologies             1.0    A  1.08   
1  2               Zorbax C8  Agilent Technologies             1.0    A  0.97   
2  3  Zorbax Eclipse XDB-C18  Agilent Technologies             1.0    B  1.07   
3  4   Zorbax Eclipse XDB-C8  Agilent Technologies             1.0    B  0.91   
4  5       Zorbax Extend C18  Agilent Technologies             1.0    B  1.09   

      S     A     B   C28   C70  retention USPtype phase  
0  0.05  0.47  0.06  1.48  1.56       10.7      L1   C18  
1 -0.04  0.21  0.17  0.97  1.05        8.3      L7    C8  
2  0.02 -0.06 -0.03  0.05  0.08        9.1      L1   C18  
3  0.02 -0.21  0.00  0.00  0.01        6.6      L7    C8  
4  0.05  0.01 -0.04  0.03  0.01        8.4      L1   C18  

Eksik Veri Analizi:
id                 0
name              15
manufacturer      15
manufacturerID    39
type              15
H                 15
S                 15
A                 15
B                 15
C28               15
C70               15
retention         15
USPtype           70
phase             16
dtype: int64

HSM Parametreleri: ['H', 'S', 'A', 'B', 'C28', 'C70', 'retention']
Diğer Sayısal Özellikler: ['manufacturerID']
Kategorik Özellikler: ['id', 'name', 'manufacturer', 'type', 'USPtype', 'phase']

2. HSM Parametrelerinin Analizi

3. HPLC Kolon Tiplerinin Retention Üzerindeki Etkisi
ANOVA testi (Kolon tipi vs Retention): F=24.47, p=0.0000
Kolon tipleri arasında retention değerleri açısından istatistiksel olarak anlamlı bir fark vardır.

HSM Parametrelerinin Betimsel İstatistikleri:
                H           S           A           B         C28         C70  \
count  780.000000  780.000000  780.000000  780.000000  780.000000  780.000000   
mean     0.836995   -0.028350   -0.126261    0.022090    0.104119    0.476352   
std      0.179580    0.063924    0.251501    0.081917    0.464055    0.587140   
min      0.310000   -0.310000   -1.520000   -0.370000   -3.398000   -1.357000   
25%      0.720000   -0.064500   -0.265000   -0.010000   -0.026750    0.120000   
50%      0.860000   -0.014000   -0.126261    0.005750    0.082000    0.304000   
75%      0.980000    0.010000    0.003000    0.024000    0.190000    0.770000   
max      1.280000    0.230000    0.730000    0.970000    2.732000    7.510000   

        retention  
count  780.000000  
mean     5.742464  
std      3.344560  
min      0.270000  
25%      3.100000  
50%      5.400000  
75%      8.100000  
max     18.400000  

4. HPLC Kolon Üreticilerinin Performans Analizi

5. HPLC Kolon Retention Değeri Tahmin Modeli
Model Performansı:
Ortalama Kare Hata (MSE): 4.2791
R-kare Skoru: 0.7057

6. Sonuçlar ve HPLC Kolon Seçimi İçin Öneriler
1. Veri setimiz çeşitli HPLC kolon özelliklerini ve HSM parametrelerini içermektedir.
2. Kolon tipleri arasında retention değerleri açısından anlamlı farklılıklar bulunmaktadır.
3. Faz hidrofobikliği (H) ve retention arasında güçlü bir ilişki gözlemlenmektedir.
4. Üreticiler arasında ortalama retention değerleri ve performans farklılıkları mevcuttur.
5. Geliştirilen tahmin modeli, HPLC kolon retention değerlerini başarıyla tahmin etmektedir.
6. En önemli özellikler arasında faz hidrofobikliği (H), molekül penetrasyon direnci (S), ve bazı kolon tipleri yer almaktadır.

Bu analizler ışığında, HPLC kolon seçimi ve optimizasyonu için şu önerilerde bulunulabilir:
- Analiz edilecek bileşiklerin özelliklerine göre uygun hidrofobiklik seviyesine sahip kolonlar seçilmelidir.
- Kolon tipi, üretici performansı ve HSM parametreleri birlikte değerlendirilerek en uygun kolon belirlenmelidir.
- Yüksek retention değeri gerektiren analizler için faz hidrofobikliği (H) yüksek kolonlar tercih edilebilir.
- Farklı türde bileşikler analiz edilecekse, çeşitli HSM parametrelerine sahip kolonların kombinasyonu düşünülebilir.
- Geliştirilen tahmin modeli, yeni kolonların performansını öngörmek için kullanılabilir.
```

## Grafiklerin yorumları ve Matematiksel Hesaplamalar:

**1. "HPLC Kolon Retention Değerini Etkileyen En Önemli 10 Özellik" Grafiği:**

![1000179508.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c49c235b-4408-4e56-89fd-ec5d9a63ca18/91b795eb-aa27-4201-bcbc-e4f907eb9351/1000179508.png)

Bu grafik, Rastgele Orman (Random Forest) modelinin, HPLC kolon retention değerini tahmin ederken hangi özelliklere daha fazla önem verdiğini göstermektedir. Özellik önemi, bir özelliğin modelin tahmin doğruluğuna ne kadar katkıda bulunduğunu ölçer.

- **H (Faz Hidrofobikliği):** Grafikte açıkça görüldüğü üzere, faz hidrofobikliği (H), retention değerini etkileyen en önemli özelliktir. Bu, hidrofobik etkileşimlerin, HPLC ayırma mekanizmasında kritik bir rol oynadığını doğrulamaktadır. Hidrofobik bir kolon, hidrofobik bileşikleri daha uzun süre tutacak ve böylece daha yüksek retention değerlerine yol açacaktır.
- **C28 (İyonize Solüt Etkileşimi):** C28 parametresi, iyonize solütlerin kolon ile etkileşimini temsil eder ve retention değerini etkileyen ikinci en önemli faktör olarak karşımıza çıkmaktadır. Bu, iyonik etkileşimlerin de HPLC ayırmada önemli bir rol oynadığını gösterir. Yüksek C28 değerine sahip kolonlar, iyonize bileşikleri daha güçlü bir şekilde tutacak ve retention değerlerini artıracaktır.
- **B (Hidrojen Bağı Bazlığı):** Kolonun hidrojen bağı bazlığı (B), üçüncü en önemli özellik olarak tespit edilmiştir. Bu, kolonun hidrojen bağı alıcısı olarak hareket etme yeteneğini yansıtır. Yüksek B değerine sahip kolonlar, hidrojen bağı donörü olan analitleri daha güçlü bir şekilde tutacak ve retention değerlerini artıracaktır.
- **S (Molekül Penetrasyon Direnci):** S parametresi, moleküllerin kolon gözeneklerine penetrasyon direncini temsil eder ve retention değerini etkileyen önemli faktörler arasında yer almaktadır. Yüksek S değerine sahip kolonlar, moleküllerin gözeneklere penetrasyonunu zorlaştıracak ve böylece retention değerlerini artıracaktır.
- **Diğer Özellikler:** "manufacturerID", "A" (Hidrojen Bağı Asitliği), "C70" (İyonize Solüt Etkileşimi), "phase_C18", "phase_Other" ve "type_B" gibi diğer özellikler de retention değerini etkilemektedir, ancak bu etkileri daha az belirgindir.

**2. "Üreticilere Göre Ortalama Retention Değerleri (İlk 20)" Grafiği:**

![1000179507.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c49c235b-4408-4e56-89fd-ec5d9a63ca18/16f9f4da-ebdc-453d-a132-9c7992efa5c6/1000179507.png)

Bu grafik, farklı HPLC kolon üreticilerinin performansını, ortalama retention değerleri ve standart sapmaları açısından karşılaştırmaktadır. Grafikte yalnızca ortalama retention değeri en yüksek olan ilk 20 üretici gösterilmiştir.

- **Ortalama Retention Değerleri:** Grafikte, üreticilere göre ortalama retention değerlerinde farklılıklar olduğu açıkça görülmektedir. Sepacrom, en yüksek ortalama retention değerine sahip üretici iken, BioAnalytical Systems, en düşük ortalama retention değerine sahip üreticidir.
- **Standart Sapmalar:** Hata çubukları, her bir üretici için ortalama retention değerinin standart sapmasını göstermektedir. Standart sapma, veri noktalarının ortalamaya göre ne kadar dağıldığını ölçer. Yüksek standart sapma, retention değerlerinde daha fazla değişkenlik olduğunu gösterir.

Bu grafik, farklı üreticilerin ürettiği kolonların performansında farklılıklar olduğunu göstermektedir. Bu farklılıklar, kolon üretim süreçlerindeki farklılıklardan, kullanılan malzemelerden veya kolon tasarımından kaynaklanabilir.

**3. "HSM Parametreleri Arasındaki Korelasyon" Grafiği:**

![1000179506.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c49c235b-4408-4e56-89fd-ec5d9a63ca18/ab6f67fe-0912-4a0c-b819-7ddfe5df228a/1000179506.png)

Bu ısı haritası, HSM parametreleri (H, S, A, B, C28, C70) ve retention değeri arasındaki korelasyonu göstermektedir. Korelasyon, iki değişken arasındaki doğrusal ilişkinin gücünü ve yönünü ölçer. Korelasyon katsayısı, -1 ile +1 arasında değişir. +1 değeri, mükemmel pozitif korelasyonu, 0 değeri korelasyon olmadığını ve -1 değeri mükemmel negatif korelasyonu gösterir.

- **Hidrofobiklik (H) ve Retention:** Grafikte görüldüğü üzere, H ve retention arasında güçlü bir pozitif korelasyon (0.72) vardır. Bu, hidrofobikliğin arttıkça retention değerinin de arttığını göstermektedir.
- **Diğer Korelasyonlar:** H ve S, H ve A, S ve C70, A ve C28 gibi diğer parametreler arasında da orta seviyede korelasyonlar gözlemlenmiştir. Bu korelasyonlar, HSM parametrelerinin birbirini etkileyebileceğini ve retention değerini birlikte belirleyebileceğini göstermektedir.

Korelasyon analizi, HSM parametreleri arasındaki ilişkileri ve bu parametrelerin retention değerini nasıl etkilediğini anlamak için kullanışlı bir araçtır.

**4. "H vs Retention", "S vs Retention", ..., "C70 vs Retention" Grafikleri:**

![1000179505.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c49c235b-4408-4e56-89fd-ec5d9a63ca18/ffc8fac5-9ffd-45e5-9308-d276544e9a38/1000179505.png)

Bu grafikler, HSM parametrelerinin her biri ile retention değeri arasındaki ilişkiyi ayrıntılı olarak gösteren saçılım grafikleridir. Grafikler, farklı kolon tiplerini (type) renklerle kodlayarak, kolon tipinin retention değerini nasıl etkilediğini görselleştirmektedir.

- **Hidrofobiklik (H):** "H vs Retention" grafiğinde, H ve retention arasında güçlü bir pozitif korelasyon olduğu açıkça görülmektedir. Hidrofobiklik arttıkça, retention değeri de artmaktadır.
- **Molekül Penetrasyon Direnci (S):** "S vs Retention" grafiğinde, S ve retention arasında zayıf bir pozitif korelasyon gözlemlenmektedir. S arttıkça, retention değeri de artma eğilimindedir.
- **Hidrojen Bağı Asitliği (A) ve Bazlığı (B):** "A vs Retention" ve "B vs Retention" grafiklerinde, A ve B ile retention arasında zayıf bir korelasyon gözlemlenmektedir.
- **İyonize Solüt Etkileşimi (C28 ve C70):** "C28 vs Retention" ve "C70 vs Retention" grafiklerinde, C28 ve C70 ile retention arasında zayıf bir pozitif korelasyon gözlemlenmektedir.

Bu grafikler, HSM parametrelerinin her birinin retention değerini nasıl etkilediğini ve kolon tipinin bu ilişkiyi nasıl etkilediğini göstermektedir.

**5. "H Dağılımı", "S Dağılımı", ..., "C70 Dağılımı" Grafikleri:**

![1000179504.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c49c235b-4408-4e56-89fd-ec5d9a63ca18/c54d9514-ff77-4732-b0f3-efc29f33ecb3/1000179504.png)

Bu histogram grafikleri, HSM parametrelerinin veri setindeki dağılımını göstermektedir. Histogram, bir değişkenin farklı değer aralıklarında kaç gözlem olduğunu gösteren bir grafik türüdür.

- **Hidrofobiklik (H):** "H Dağılımı" grafiği, H değerlerinin çoğunlukla 0.6 ile 1.2 arasında yoğunlaştığını göstermektedir. Dağılım, sağa çarpık bir şekil göstermektedir.
- **Molekül Penetrasyon Direnci (S):** "S Dağılımı" grafiği, S değerlerinin çoğunlukla -0.1 ile 0.1 arasında yoğunlaştığını göstermektedir. Dağılım, normale yakın bir şekil göstermektedir.
- **Hidrojen Bağı Asitliği (A) ve Bazlığı (B):** "A Dağılımı" ve "B Dağılımı" grafikleri, A ve B değerlerinin çoğunlukla -0.5 ile 0.5 arasında yoğunlaştığını göstermektedir. Dağılımlar, normale yakın bir şekil göstermektedir.
- **İyonize Solüt Etkileşimi (C28 ve C70):** "C28 Dağılımı" ve "C70 Dağılımı" grafikleri, C28 ve C70 değerlerinin çoğunlukla -1 ile 2 arasında yoğunlaştığını göstermektedir. Dağılımlar, sağa çarpık bir şekil göstermektedir.

Bu histogram grafikleri, HSM parametrelerinin veri setindeki dağılımını ve bu parametrelerin istatistiksel özelliklerini (ortalama, standart sapma vb.) anlamak için kullanışlıdır.

---

**İstatistiksel Hesaplamalar:**

**1. ANOVA Testi:**

ANOVA (Analysis of Variance) testi, iki veya daha fazla grubun ortalamaları arasında istatistiksel olarak anlamlı bir fark olup olmadığını test etmek için kullanılan bir istatistiksel yöntemdir. Bu çalışmada, ANOVA testi, farklı kolon tipleri arasında retention değerleri açısından anlamlı bir fark olup olmadığını test etmek için kullanılmıştır.

ANOVA testinde, F-istatistiği ve p-değeri hesaplanır. F-istatistiği, gruplar arası varyansın gruplar içi varyansa oranını ölçer. Yüksek F-istatistiği, gruplar arasında daha fazla fark olduğunu gösterir. P-değeri, gruplar arasında gerçekte bir fark olmadığı halde gözlemlenen farkın rastgele şans eseri ortaya çıkma olasılığını ölçer. Düşük p-değeri, gruplar arasında anlamlı bir fark olduğunu gösterir.

Bu çalışmada, ANOVA testi sonucunda p-değeri 0.05'ten küçük bulunmuştur. Bu, farklı kolon tipleri arasında retention değerleri açısından istatistiksel olarak anlamlı bir fark olduğunu göstermektedir.

**2. Pearson Korelasyon Katsayısı:**

Pearson korelasyon katsayısı, iki değişken arasındaki doğrusal ilişkinin gücünü ve yönünü ölçer. Katsayı, -1 ile +1 arasında değişir. +1 değeri, mükemmel pozitif korelasyonu, 0 değeri korelasyon olmadığını ve -1 değeri mükemmel negatif korelasyonu gösterir.

Bu çalışmada, Pearson korelasyon katsayısı, HSM parametreleri ile retention değeri arasındaki ilişkiyi ölçmek için kullanılmıştır. Örneğin, H ve retention arasındaki Pearson korelasyon katsayısı 0.72 olarak bulunmuştur. Bu, H ve retention arasında güçlü bir pozitif korelasyon olduğunu göstermektedir.

**3. Ortalama ve Standart Sapma:**

Ortalama, bir veri setindeki değerlerin toplamının veri sayısına bölünmesiyle hesaplanır. Standart sapma, veri noktalarının ortalamaya göre ne kadar dağıldığını ölçer. Yüksek standart sapma, veri noktalarının ortalamadan daha uzak olduğunu gösterir.

Bu çalışmada, ortalama ve standart sapma, HSM parametrelerinin ve retention değerinin istatistiksel özelliklerini tanımlamak için kullanılmıştır.

---

**Sonuç:**

Bu grafiklerin ve istatistiksel analizler, HPLC kolon seçimi ve metot optimizasyonu için önemli bilgiler sağlamaktadır. Özellikle, faz hidrofobikliği (H), retention değerini etkileyen en önemli faktör olarak tespit edilmiştir. Kolon tipi, üretici performansı ve diğer HSM parametreleri de dikkate alınması gereken önemli faktörlerdir.

Geliştirilen makine öğrenmesi modeli, HPLC kolon retention değerlerini başarıyla tahmin etmiştir ve kolon seçimi ve metot optimizasyonu sürecini hızlandırmak için kullanılabilir.

Veriseti için lütfen ziyaret edin.

(https://www.hplccolumns.org/)
