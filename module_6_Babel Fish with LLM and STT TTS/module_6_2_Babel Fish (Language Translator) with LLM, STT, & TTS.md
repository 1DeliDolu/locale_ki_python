### 🎯 Proje Tanıtımı: Babel Fish ile Sesli Çeviri Asistanı

Bu yönlendirmeli projeye hoş geldiniz! "Babel Fish", Douglas Adams'ın "Otostopçunun Galaksi Rehberi" adlı serisinde geçen kurgusal bir yaratıktan esinlenen bir çeviri hizmeti veya aracı için kullanılan bir metafordur.

Bu projede, Watsonx ve IBM Watson Speech Libraries for Embed teknolojilerini kullanarak sesli bir çeviri asistanı oluşturacaksınız. Proje boyunca, sesli girişleri metne dönüştüren, bu metni Watsonx’in flan-ul2 modeline gönderip farklı dillerde yanıt alarak metinden konuşmaya çeviren ve son olarak kullanıcıya bu sesi oynatan bir çeviri asistanı geliştireceksiniz. Bu sesli çeviri sistemi, HTML, CSS ve JavaScript ile geliştirilen duyarlı bir ön yüze ve Flask ile geliştirilen güvenilir bir arka yüze sahip olacak.

---

### 🧪 Proje Sonucu: Ne Öğreneceksiniz?

Bu kursun sonunda, sesli giriş alabilen ve farklı dillere çeviri sunabilen kendi yapay zekâ destekli çeviri asistanınızı oluşturmak için gerekli becerilere sahip olacaksınız. Ayrıca Python, Flask, HTML, CSS ve JavaScript kullanarak web geliştirme konusunda sağlam bir temel kazanmış olacaksınız. Ortaya çıkacak olan tam işlevli full-stack uygulama, etkileşimde bulunan herkesi etkileyecek düzeyde olacaktır.

---

### 🧠 Watsonx Nedir?

Watsonx, güvenilir verilerle işletmenizde yapay zekânın etkisini ölçeklendirmeye ve hızlandırmaya yardımcı olmak için tasarlanmış bir yapay zekâ ve veri platformudur.

Ana bileşenleri; yeni temel modeller, üretken yapay zekâ ve makine öğrenimi için bir stüdyo, açık veri gölü mimarisine dayalı amaca uygun bir veri deposu ve sorumluluk, şeffaflık ve açıklanabilirlik esaslarına dayalı yapay zekâ iş akışlarını hızlandıran bir araç setidir. Watsonx AI asistanları, uzman bilgiye ihtiyaç duymadan çeşitli iş süreçlerinde otomasyon sağlar (müşteri hizmetleri, kod üretimi, İK süreçleri gibi).

---

### 🗣️ IBM Watson Speech Libraries for Embed

IBM Watson® Speech Libraries for Embed, metinden konuşmaya ve konuşmadan metne çeviri yetenekleri sunan, kapsayıcılar halinde sunulan kütüphanelerdir. IBM iş ortaklarına IBM Research® teknolojilerini kendi çözümlerine entegre etmede daha fazla esneklik sunar. Bu gömülebilir AI teknolojileri sayesinde sesli yazılım çözümleri daha hızlı geliştirilebilir ve hibrit çoklu bulut ortamlarında dağıtılabilir. Bu teknolojiler, asistanın kullanıcılarla sesli iletişim kurmasını sağlar.

---

### 🤖 Sesli Asistanlar Hakkında

Sanal asistanlar, insan sesiyle doğal bir şekilde etkileşim kurmak üzere tasarlanmış programlardır. Genellikle internet üzerinden kullanılır ve müşteri hizmetleri, e-ticaret, eğitim gibi pek çok sektörde kullanılabilir.

---

### 🐍 Python ve Flask

Python, web geliştirme ve veri bilimi alanlarında yaygın olarak kullanılan popüler bir programlama dilidir. Flask ise Python ile web uygulamaları geliştirmeyi kolaylaştıran hafif bir web çatısıdır. Bu projede sesli asistanın arka ucunu oluşturmak için Python ve Flask kullanılacaktır. Python öğrenmesi kolay ve güçlü bir dildir; geniş bir kütüphane ve araç ekosistemine sahiptir.

---

### 🌐 HTML - CSS - JavaScript

HTML (Hypertext Markup Language), web üzerindeki içerikleri yapılandırmak için kullanılan işaretleme dilidir. CSS (Cascading Style Sheets), HTML belgelerinin görünümünü ve biçimini belirlemek için kullanılır. JavaScript ise web sayfalarına etkileşim kazandırmak için yaygın olarak kullanılan bir programlama dilidir. Bu üçlü teknoloji, sesli asistanın kullanıcı arayüzünü oluşturmak için kullanılacaktır. Kullanıcılar, HTML, CSS ve JavaScript ile oluşturulmuş bu web arayüzü aracılığıyla asistanla etkileşimde bulunabilecektir.

---

### 🎓 Öğrenim Hedefleri

Bu projenin sonunda şunları yapabileceksiniz:

* Sesli asistanların temelini ve çeşitli kullanım alanlarını açıklamak
* Python, Flask, HTML, CSS ve JavaScript kullanarak geliştirme ortamını kurmak
* Kullanıcılardan sesli giriş almak için konuşmadan metne (STT) işlevselliğini uygulamak
* Watsonx'in flan-ul2 modeli ile entegrasyon sağlayarak asistanınıza zekâ kazandırmak
* Metinden konuşmaya (TTS) işlevselliğini uygulayarak asistanın sesli yanıt verebilmesini sağlamak
* Tüm bu bileşenleri bir araya getirerek sesli giriş alıp konuşma yanıtı verebilen işlevsel bir asistan oluşturmak
* Uygulamayı geliştirici modda bir sunucu çalıştırarak web uygulaması olarak dağıtmak

---

### 📋 Ön Koşullar

Bu projede çalışmak için Python konusunda temel bilgiye sahip olmalısınız. HTML, CSS ve JavaScript hakkında temel bilgiye sahip olmak faydalı olacaktır ancak zorunlu değildir. Süreç boyunca tüm adımları ve kodları ayrıntılı şekilde açıklayacağız.

İşte metnin Türkçeye çevrilmiş ve paragraflara ayrılmış hali, başlıklarla birlikte:

---

### 🖥️ Adım 1: Arayüzü Anlamak

Bu projede amaç, bir sesli asistanla iletişim kurmayı sağlayan bir arayüz oluşturmak ve yanıtların gönderilip alınmasını yönetecek bir arka uç yapısı kurmaktır.

---

### 🌐 Kullanıcı Arayüzü Teknolojileri

Ön yüz, HTML, CSS ve JavaScript kullanılarak oluşturulacak ve stil verme için Bootstrap, simgeler için Font Awesome, işlemleri verimli bir şekilde yönetmek için JQuery gibi popüler kütüphanelerden yararlanılacaktır. Kullanıcı arayüzü, Google Asistan gibi diğer sesli asistan uygulamalarına benzeyecek. Arayüz için gereken kodlar sağlanmıştır ve bu kursun odak noktası, sesli asistanı inşa etmek ve çeşitli servisler ve API’lerle entegre etmektir.

---

### 🔄 Ön Yüz ve Arka Uç Etkileşimi

Verilen kodlar sayesinde ön yüz ile arka uç arasındaki etkileşimin nasıl gerçekleştiğini anlayacaksınız. Kodları incelerken, önemli parçaları nasıl çalıştıklarını görecek ve bu basit web sayfasını oluşturmanın mantığını kavrayacaksınız.

---

### ⚙️ Ortamın Kurulumu

Öncelikle aşağıdaki komutları çalıştırarak geliştirme ortamını kurun:

```bash
python3.11 -m venv my_env
source my_env/bin/activate  # my_env sanal ortamını etkinleştir
```

---

### 📁 Proje Klonlama ve Dizine Geçiş

Aşağıdaki komutları terminalde çalıştırarak proje yapısını alın, isterseniz ismini değiştirin ve proje dizinine geçin:

```bash

git clone https://github.com/ibm-developer-skills-network/translator-with-voice-and-watsonx
cd translator-with-voice-and-watsonx
```

![1748503692287](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748503692287.png)

---

### 📦 Gereksinimlerin Kurulumu

Projeye başlamadan önce gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

☕ Bir fincan kahve alabilirsiniz, çünkü gereksinimlerin yüklenmesi 5-10 dakika sürebilir. (Bu süre zarfında projeye devam edebilirsiniz.)

```
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
```

---

### 🧩 Bir Sonraki Adım: Ön Yüzün Yapısı

Bir sonraki bölümde, HTML, CSS ve JavaScript kullanılarak oluşturulan ön yüzün nasıl çalıştığına dair kısa bir açıklama yer alıyor.

---

### 🗂️ index.html Dosyası

`index.html` dosyası, web arayüzünün yapısını ve düzenini tanımlar. Bu dosya, JQuery, Bootstrap ve FontAwesome simgeleri gibi harici kütüphanelerin yanı sıra stil ve etkileşim için gerekli olan `style.css` ve `script.js` dosyalarını da içerir.

---

### 🎨 style.css Dosyası

`style.css` dosyası, sayfa bileşenlerinin görsel görünümünü özelleştirir. Ayrıca CSS keyframe (anahtar çerçeve) animasyonlarını kullanarak yükleme animasyonlarını yönetir. Keyframe animasyonları, belirli zaman noktalarındaki stil değişikliklerini tanımlayarak pürüzsüz geçişler ve dinamik efektler oluşturmayı sağlar.

---

### 💡 script.js Dosyası

`script.js` dosyası, sayfanın etkileşimli özelliklerinden ve işlevselliğinden sorumludur. Kodun büyük kısmı burada yer alır ve şunları gerçekleştirir:

* Açık ve koyu mod arasında geçiş
* Mesaj gönderme
* Yeni mesajları ekranda gösterme
* Kullanıcının ses kaydetmesini sağlama

---

### 🖼️ Arayüz Görselleri

Ön yüz ile ilgili bazı görseller aşağıda gösterilmiştir.

#### ☀️ Açık Mod

Bu görüntü, temel kodun nasıl çalıştığını gösterir. Bu haliyle sadece boş (null) bir yanıt döndürecektir.

---

![1748503752920](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748503752920.png)



### 🌑 Koyu Mod

Projeyi tamamladığınızda, asistan işlevsel hale gelecek ve aşağıda gösterildiği gibi net yanıtlar verebilecektir.

---

![1748503786929](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748503786929.png)


---

### 🧠 Adım 2: Sunucuyu Anlamak

Sunucu, uygulamanın çalıştığı ve tüm servislerle iletişim kurduğu yerdir. Flask, Python için geliştirilmiş bir web geliştirme çatısıdır ve bu projede uygulamanın arka ucu olarak kullanılacaktır. Hafif ve basit bir yapı sunar, bu da web uygulamalarını hızlı ve kolay şekilde geliştirmenizi sağlar.

---

### 🔧 Flask ile Arka Uç Geliştirme

Flask ile karmaşık kodlara ya da ek araç/kütüphanelere gerek kalmadan web sayfaları ve uygulamaları oluşturabilirsiniz. Kendi yollarınızı (route) tanımlayabilir, kullanıcı isteklerini işleyebilir, harici API’lere ve servislere veri gönderip alabilirsiniz.

Bu yönlendirmeli projede, sesli asistanınızın arka ucunu yönetmek için Flask kullanılacaktır. Yani, HTTP isteklerini ve yanıtlarını işlemek için Flask ile yollar oluşturacaksınız. Kullanıcı ön yüz arayüzü aracılığıyla sesli asistanla etkileşime geçtiğinde, bu istek Flask sunucusuna gönderilecek. Flask bu isteği işleyecek ve ilgili servise yönlendirecektir.

---

### 📄 server.py Dosyasının Yapısı

Sunucuya ait kodlar `server.py` dosyasında yer almaktadır.

Dosyanın en üstünde bazı `import` (içe aktarma) ifadeleri bulunur. Bu ifadeler, dış kütüphane ve modülleri bu dosyaya dahil eder. Örneğin, `speech_text` fonksiyonu `worker.py` dosyasında tanımlıdır. `ibm_watson_machine_learning` ise Watsonx'in flan-ul2 modelini kullanmak için kurmanız gereken bir pakettir. Bu dış modüller sayesinde konuşmadan metne ve flan-ul2 modelleriyle kolayca etkileşim kurabilirsiniz.

---

### 🔐 CORS Politikası ve Uygulama Başlatma

İçe aktarmaların hemen ardından Flask uygulaması başlatılır ve bir CORS (Cross-Origin Resource Sharing) politikası tanımlanır. CORS, web sayfalarının kendi sunucusundan farklı bir domaine istek göndermesine izin verir veya engeller. Şu anda * olarak ayarlanmıştır, yani her isteğe izin verilmektedir.

---

### 🚦 Yönlendirme (Routing) ve Sunucuyu Başlatma

`server.py` dosyası 3 adet yönlendirme (route) fonksiyonu ve sunucuyu başlatma kodunu içerir.

İlk route'u aşağıdaki kodla değiştirin:

```python
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
```

#### 📌 Fonksiyon Açıklaması

Bir kullanıcı uygulamayı yüklemeye çalıştığında, `/` (ana dizin) adresine bir istek gönderir. Bu da yukarıdaki `index` fonksiyonunu tetikler ve `index.html` dosyasını (ön yüz arayüzü) kullanıcıya gösterir.

İkinci ve üçüncü route'lar, uygulamalar arası veri alışverişi ve işleme görevini üstlenecektir.

---

### ▶️ Sunucuyu Başlatma

Sunucuyu başlatmak için şu komutu çalıştırın:

```bash
python server.py
```

Terminalde aşağıdaki gibi bir çıktı göreceksiniz. Bu, sunucunun çalıştığını gösterir.

---

![1748503872880](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748503872880.png)

---

### 🚀 Uygulama Çalışıyor: localhost:8000

Uygulama artık **localhost:8000** adresinde çalışıyor. Uygulamaya erişmek için aşağıdaki bağlantıya tıklayabilirsiniz:

📎 Eğer dosyayı kendi bilgisayarınızda çalıştırıyorsanız, tarayıcınızı açıp şu URL'yi yapıştırabilirsiniz:

👉 `http://127.0.0.1:8000`

---

### 🖼️ Arayüz Açılıyor

Bu noktada, uygulamanın arayüzü açılacak ve görüntülenecektir. Ancak şu anda uygulama çalışıyor olsa da henüz herhangi bir çıktı üretmeyecektir.

---

### ⏹️ Uygulamayı Durdurma

Uygulama üzerinde biraz çalıştıktan sonra, uygulamayı durdurmak için terminalde **Ctrl + C** tuşlarına (Mac için Control (^) tuşu) aynı anda basın.

---

### 🔜 Sıradaki Adımlar

Sonraki bölümlerde, `server.py` dosyasındaki `process_message_route` ve `speech_to_text_route` fonksiyonlarını tamamlamayı öğreneceksiniz. Bu fonksiyonlar, çeşitli paketleri ve API uç noktalarını (endpoints) nasıl kullanacağınızı anlamanızı sağlayacaktır.

---


---

### 🧠 Adım 3: Watsonx API Entegrasyonu

Şimdi sesli asistanınıza bir "beyin" kazandırma zamanı! Watsonx API’nin gücüyle, yazıya dökülen metni işleyip sorularınıza yanıt verebilecek bir sistem oluşturabilirsiniz.

---

### 🔐 Programatik Erişim için Kimlik Doğrulama

Bu projede, aşağıdaki `worker.py` koduna kendi `Watsonx_API` anahtarınızı ve `Project_id`’nizi girmenize gerek yoktur. Aşağıdaki gibi sadece `project_id="skills-network"` belirterek ve `Watsonx_API` boş bırakarak kullanabilirsiniz. Çünkü bu Cloud IDE ortamında, API’ye erişim izni zaten sizin için tanımlanmıştır.

> ⚠️ Bu erişim yöntemi sadece bu Cloud IDE ortamı için geçerlidir. Eğer modeli veya API’yi kendi yerel ortamınızda kullanmak isterseniz, ayrıntılı talimatlar bu eğitimin başka bölümlerinde sunulmaktadır.

---

### 🧩 Kodun En Üstüne Eklenmesi Gerekenler

Aşağıdaki kod bloğunu `worker.py` dosyasının en üst kısmına ekleyin:

```python
# Watsonx'in LLM'ini çağırmak için IBM Watson Machine Learning kütüphanesini içe aktarıyoruz
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model

# Watsonx_API ve Project_id için yer tutucu (harici kullanım için)
# API_KEY = "Your WatsonX API"
PROJECT_ID = "skills-network"

# Kimlik bilgilerini tanımlıyoruz
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
    # "apikey": API_KEY
}

# Kullanılacak model kimliğini belirliyoruz
model_id = ModelTypes.FLAN_UL2

# Model parametrelerini tanımlıyoruz
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods

parameters = {
    GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.MAX_NEW_TOKENS: 1024
}

# LLM (Büyük Dil Modeli)'i tanımlıyoruz
model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=PROJECT_ID
)
```

---

![1748503961894](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748503961894.png)

---

### 🧠 Watsonx Mesaj İşleme Fonksiyonu

Şimdi `watsonx_process_message` adlı fonksiyonu güncelleyeceğiz. Bu fonksiyon, kullanıcıdan gelen mesajı alıp Watsonx’in flan-ul2 API’sine gönderecek ve karşılık olarak bir yanıt alacak. Temelde bu işlem, ChatGPT’de “gönder” tuşuna basmaya eşdeğerdir.

---

### 🛠️ worker.py Dosyasını Güncelleyin

Aşağıdaki kodu `worker.py` dosyasındaki `watsonx_process_message` fonksiyonuyla değiştirin:

```python
def watsonx_process_message(user_message):
    # Watsonx API için prompt ayarlanıyor
    prompt = f"""Respond to the query: ```{user_message}```"""
    response_text = model.generate_text(prompt=prompt)
    print("wastonx response:", response_text)
    return response_text
```

---

### 🧹 Prompt Geliştirme (İyileştirme)

Çeviri asistanımızı daha akıllı hale getirebiliriz. Kullanıcıların her seferinde "translate" yazmasına gerek kalmamalı. Bu nedenle, `watsonx_process_message` fonksiyonundaki prompt’u daha açık ve amaca yönelik hale getiriyoruz.

Örneğin, İngilizce’den İspanyolca’ya çeviri yapmak istiyorsak, prompt’u şu şekilde güncelleyin:

```python
prompt = f"""You are an assistant helping translate sentences from English into Spanish.
Translate the query to Spanish: ```{user_message}```."""
```

Bu yeni prompt, kullanıcının amacının çeviri olduğunu açıkça belirtir ve "translate" yazma zorunluluğunu ortadan kaldırır.

> 🌍 Eğer hedef diliniz İspanyolca dışında başka bir dil olacaksa, prompt içindeki “Spanish” kelimesini istediğiniz hedef dilin adıyla değiştirebilirsiniz. Bu sayede çevirici, farklı diller için de kolayca kullanılabilir hale gelir.

---

### 🧩 Fonksiyon Açıklaması

Fonksiyon oldukça basittir, çünkü `ibm_watson_machine_learning` kütüphanesi kullanımı oldukça kolaydır.

`model.generate_text` fonksiyonuyla Watsonx’in API’si çağrılır ve belirlenen prompt gönderilir. Buradaki `model`, daha önce tanımladığımız LLM (flan-ul2 modeli)’yi temsil eder.

🧪 Kendi ihtiyaçlarınıza göre parametreleri özelleştirebilir ve IBM Watsonx Prompt Lab ortamında gerçek zamanlı olarak bu parametreleri test edebilirsiniz.

---


![1748504014641](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748504014641.png)


İşte bu cümlenin Türkçesi, önceki bölümle uyumlu şekilde dahil edilmiştir:

---

### 🔁 Yanıtı Döndürme

Son olarak, oluşturulan yanıtı içeren `response_text` değişkenini döndürüyoruz. Bu değişken, oluşturduğumuz prompt’a verilen cevabı saklar.

---


İşte bu bölümün Türkçeye çevrilmiş ve konu başlıklarına ayrılmış hali:

---

### 🎙️ Adım 4: Watson Speech-to-Text Entegrasyonu

**Speech-to-Text (Konuşmadan Metne)** teknolojisi, konuşmayı makine öğrenmesi kullanarak metne dönüştüren bir teknolojidir. Bu teknoloji; erişilebilirlik, verimlilik, kullanım kolaylığı, çok dillilik desteği ve uygun maliyetli çözümler sunar. Örneğin, bir sohbet uygulamasında kullanıcının sesli girdisini almak için oldukça kullanışlıdır.

Daha önce dağıtılan gömülebilir Watson Speech-to-Text yapay zekâ modeli sayesinde, basit bir API ile sesli veriyi metne kolayca dönüştürebiliriz. Bu metin sonucunu daha sonra Watsonx API’sine göndererek yanıt oluşturabiliriz.

---

### 🚀 Speech-to-Text Servisini Başlatma

 **Skills Network** , bu ortamda otomatik olarak çalışan kendi Watson Speech-to-Text imajını sağlar. Bu servise şu uç nokta üzerinden erişebilirsiniz:

👉 `https://sn-watson-stt.labs.skills.network`

Servisin çalıştığını test etmek için şu komutu çalıştırabilirsiniz:

```bash
curl https://sn-watson-stt.labs.skills.network/speech-to-text/api/v1/models
```

Bu komutla tanınan dillerin bir listesini göreceksiniz. Örnek çıktı:

```json
{
   "models": [
       {
         "name": "es-LA_Telephony",
         "language": "es-LA",
         "description": "Latin American Spanish telephony model for narrowband audio (8kHz)"
       },
       {
         "name": "en-US_Multimedia",
         "language": "en-US",
         "description": "US English multimedia model for broadband audio (16kHz or more)"
       }
   ]
}
```

---

### 🔊 Örnek Ses Dosyasını Test Etme

Örnek bir ses dosyası indirip testi deneyebilirsiniz:

```bash
curl "https://github.com/watson-developer-cloud/doc-tutorial-downloads/raw/master/speech-to-text/0001.flac" -sLo example.flac
```

Ses dosyasını servise gönderin:

```bash
curl "https://sn-watson-stt.labs.skills.network/speech-to-text/api/v1/recognize" \
--header "Content-Type: audio/flac" \
--data-binary @example.flac
```

Örnek yanıt:

```json
{
   "result_index": 0,
   "results": [
      {
         "final": true,
         "alternatives": [
            {
               "transcript": "several tornadoes touched down as a line of severe thunderstorms swept through colorado on sunday ",
               "confidence": 0.99
            }
         ]
      }
   ]
}
```

---

### 🌐 Alternatif Model ve Biçimler

Farklı bir model kullanmak için `model` parametresini URL’ye ekleyin. Ses formatını da değiştirebilirsiniz, sadece `Content-Type` başlığının ses formatıyla eşleştiğinden emin olun:

```bash
curl "https://sn-watson-stt.labs.skills.network/speech-to-text/api/v1/recognize?model=es-LA_Telephony" \
--header "Content-Type: audio/flac" \
--data-binary @example.flac
```

---

### 🧱 Uygulama: speech_to_text Fonksiyonu

Şimdi `worker.py` dosyasındaki `speech_to_text` fonksiyonunu aşağıdaki şekilde tanımlayalım. Bu fonksiyon, tarayıcıdan alınan ses verisini Watson Speech-to-Text API’sine gönderir ve karşılık olarak metin dönüşümünü alır:

```python
import requests

def speech_to_text(audio_binary):
    # Watson STT API URL'sini tanımlıyoruz
    base_url = 'https://sn-watson-stt.labs.skills.network'
    api_url = base_url + '/speech-to-text/api/v1/recognize'

    # Model parametresi
    params = {
        'model': 'en-US_Multimedia',
    }

    # HTTP POST isteği gönderiyoruz
    response = requests.post(api_url, params=params, data=audio_binary).json()

    # Yanıttan metni alıyoruz
    text = 'null'
    while bool(response.get('results')):
        print('Speech-to-Text response:', response)
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('recognised text: ', text)
        return text
```

---

### 📘 Fonksiyon Açıklaması

* `requests` kütüphanesi, HTTP istekleri yapmak için kullanılır.
* Fonksiyon, sadece `audio_binary` (ses verisi) parametresini alır ve bu veriyi POST isteği olarak gönderir.
* 3 temel unsur:
  * **API URL’si** : `api_url` değişkeninde tanımlıdır.
  * **Parametreler** : Hangi modeli kullanacağımızı belirtir. `'model': 'en-US_Multimedia'`.
  * **İstek gövdesi** : `audio_binary`, ses verisinin kendisidir.

Yanıt JSON formatında döner ve Python sözlüğü gibi kullanılabilir. Biz de buradan `"transcript"` alanını alıp kullanıcıya döndürürüz.

---

### 💡 Küçük Bir İpucu

`print('response', response)` gibi çıktı ifadeleri, dış servislerden alınan verileri görmek ve hata ayıklamak için çok faydalıdır. Bu nedenle geliştirme sürecinde sıkça kullanmanız önerilir.

---


---




İşte bu bölümün Türkçeye çevrilmiş ve konu başlıklarına ayrılmış hali:

---

### 🔗 Adım 6: Flask API Uç Noktalarını Oluşturarak Her Şeyi Birleştirme

Artık önceki bölümlerde tanımladığımız fonksiyonları kullanarak her şeyi bir araya getirebilir ve sesli asistanımızı tamamlayabiliriz.

Bu adımda yapılacak değişiklikler `server.py` dosyasındadır.

---

### 🧩 Fonksiyonların Dahil Edilmesi

`worker.py` dosyasındaki fonksiyonlar zaten `server.py` dosyasına aktarılmıştır. Böylece sunucu tarafında bu fonksiyonları doğrudan kullanabilirsiniz:

```python
from worker import speech_to_text, text_to_speech, watsonx_process_message
```

---

### 🗣️ Speech-to-Text Route

Bu rota, kullanıcının sesini alır ve bunu yazıya döndürür. Aşağıdaki kodla `speech_to_text_route` fonksiyonunu değiştirin:

```python
@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print("processing Speech-to-Text")
    audio_binary = request.data  # Kullanıcının ses verisini alıyoruz
    text = speech_to_text(audio_binary)  # Konuşmayı metne çeviriyoruz
    # JSON formatında cevap döndürüyoruz
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    print(response)
    print(response.data)
    return response
```

#### 🧾 Fonksiyon Açıklaması

* `request.data`: Tarayıcıdan gelen ses verisini `audio_binary` olarak alır.
* `speech_to_text(audio_binary)`: Konuşma verisini metne çevirir.
* `json.dumps({'text': text})`: Yanıtı JSON formatında döndürmek için.
* `status=200`: İşlemin başarılı olduğunu belirtir.
* `mimetype='application/json'`: Yanıtın tipi JSON’dur.

---

### 💬 process_message_route: Mesajı İşleme ve Yanıtı Seslendirme

Kullanıcının mesajını alır, Watsonx ile işler, sonra yanıtı sese dönüştürerek kullanıcıya hem metin hem ses olarak döndürür.

Aşağıdaki kodla `process_message_route` fonksiyonunu değiştirin:

```python
@app.route('/process-message', methods=['POST'])
def process_message_route():
    user_message = request.json['userMessage']
    print('user_message', user_message)
    voice = request.json['voice']
    print('voice', voice)
  
    # Watsonx ile mesajı işleyip metin yanıt al
    watsonx_response_text = watsonx_process_message(user_message)
    # Boş satırları temizle
    watsonx_response_text = os.linesep.join([s for s in watsonx_response_text.splitlines() if s])
    # Yanıtı ses verisine dönüştür
    watsonx_response_speech = text_to_speech(watsonx_response_text, voice)
    # Ses verisini base64 string'e çevir
    watsonx_response_speech = base64.b64encode(watsonx_response_speech).decode('utf-8')
  
    # JSON yanıtı oluştur ve döndür
    response = app.response_class(
        response=json.dumps({
            "watsonxResponseText": watsonx_response_text,
            "watsonxResponseSpeech": watsonx_response_speech
        }),
        status=200,
        mimetype='application/json'
    )
    print(response)
    return response
```

#### 🧾 Fonksiyon Açıklaması

* `request.json['userMessage']`: Kullanıcının mesajını alır.
* `request.json['voice']`: Tercih edilen sesi alır.
* `watsonx_process_message()`: Mesajı işler, yanıt üretir.
* `os.linesep.join(...)`: Yanıttaki boş satırları temizler.
* `text_to_speech(...)`: Metni sese çevirir.
* `base64.b64encode(...)`: Ses verisini metne (base64) çevirerek JSON içinde gönderilebilir hale getirir.
* `json.dumps(...)`: Yanıtı JSON formatına dönüştürür ve döndürür.

---

Bu adımla artık sesli asistanınız; sesi yazıya çeviren, yazıyı anlayıp yanıt oluşturan ve bu yanıtı sesli olarak ileten eksiksiz bir sistem haline gelmiştir. ✅

### 🔊 Adım 5: Watson Text-to-Speech Entegrasyonu

Şimdi sıra asistanımıza bir ses kazandırmaya geldi! Watsonx ile kullanıcının mesajını işledikten sonra, yanıtı sese dönüştürmek için son `worker.py` fonksiyonumuzu ekleyeceğiz. Böylece, Google, Alexa, Siri gibi sanal asistanlar gibi, yanıtı kullanıcıya sesli olarak iletebileceğiz.

---

### 🚀 Text-to-Speech Servisini Başlatma

 **Skills Network** , bu ortamda otomatik olarak çalışan kendi Watson Text-to-Speech servisini sağlar. Bu servise erişim için uç nokta:

👉 `https://sn-watson-tts.labs.skills.network`

Servisin çalışıp çalışmadığını test etmek için şu komutu kullanabilirsiniz:

```bash
curl https://sn-watson-tts.labs.skills.network/text-to-speech/api/v1/voices
```

Bu komut, kullanılabilir ses modellerinin bir listesini verir. Örnek çıktı:

```json
{
   "voices": [
      {
         "name": "en-US_OliviaV3Voice",
         "language": "en-US",
         "gender": "female",
         "description": "Olivia: American English female voice. Dnn technology."
      },
      {
         "name": "es-ES_EnriqueV3Voice",
         "language": "en-GB",
         "gender": "male",
         "description": "Enrique: Castilian Spanish male voice. Dnn technology."
      }
   ]
}
```

---

### 🧪 Test: Metinden Sese Dönüştürme

Aşağıdaki komutla örnek bir metni ses dosyasına dönüştürebilirsiniz:

```bash
curl "https://sn-watson-tts.labs.skills.network/text-to-speech/api/v1/synthesize" \
--header "Content-Type: application/json" \
--data '{"text":"Hello world"}' \
--header "Accept: audio/wav" \
--output output.wav
```

Belirli bir ses ve format kullanmak isterseniz örnek:

```bash
curl "https://sn-watson-tts.labs.skills.network/text-to-speech/api/v1/synthesize?voice=es-LA_SofiaV3Voice" \
--header "Content-Type: application/json" \
--data '{"text":"Hola! Hoy es un dia muy bonito."}' \
--header "Accept: audio/mp3" \
--output hola.mp3
```

Bu komut sonunda `"translator-with-voice-and-watsonx"` dizininde `hola.mp3` dosyasını göreceksiniz.

---

### 🧱 text_to_speech Fonksiyonu

Şimdi `worker.py` dosyasına `text_to_speech` fonksiyonunu ekleyelim. Bu fonksiyon, verilen metni Watson Text-to-Speech API’sine göndererek sesli çıktıyı döndürür.

```python
def text_to_speech(text, voice=""):
    # Watson TTS API URL'sini tanımlıyoruz
    base_url = 'https://sn-watson-tts.labs.skills.network'
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'
  
    # Kullanıcı özel bir ses seçmişse API URL'sine ekliyoruz
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice
  
    # HTTP isteği için başlıklar
    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }

    # İstek gövdesi
    json_data = {
        'text': text,
    }

    # HTTP POST isteği gönderiliyor
    response = requests.post(api_url, headers=headers, json=json_data)
    print('Text-to-Speech response:', response)
    return response.content
```

---

### 🧾 Fonksiyon Açıklaması

Bu fonksiyon iki parametre alır: `text` (metin) ve `voice` (isteğe bağlı ses seçimi). Eğer `voice` parametresi boş değilse, API URL’sine eklenir. İstek gövdesine metin yerleştirilir.

HTTP POST isteği yapmak için üç ana bileşene ihtiyaç vardır:

* **API URL’si** : `api_url`, Watson’ın Text-to-Speech servisini işaret eder.
* **Headers (Başlıklar)** :
* `'Accept': 'audio/wav'` → dönecek dosya formatı,
* `'Content-Type': 'application/json'` → gönderilen verinin formatı.
* **Gövde (Body)** : `'text': text` anahtar-değeri ile bir JSON veri yapısıdır.

İstek gönderildikten sonra, `response.content` kullanılarak gelen sesli veri döndürülür.

---

### 💡 İpucu

API'den gelen yanıtları `print` ile ekrana yazdırmak (örneğin `print('response', response)`) hata ayıklamada oldukça yararlıdır. Bu, özellikle harici servislerle çalışırken önemlidir.

---


---

### ☁️ Adım 7: Uygulamayı CloudIDE Ortamında Çalıştırmak

Asistan artık tamamlandı ve kullanıma hazır!

Text-to-Speech ve Speech-to-Text model URL’leri doğru şekilde ayarlandıysa, tek yapmanız gereken `server.py` dosyasını çalıştırarak uygulamayı başlatmak.

---

### ▶️ Sunucuyu Başlatma

Terminalde aşağıdaki komutu çalıştırın:

```bash
python server.py
```

Bu komutla birlikte terminalde uygulamanın çalıştığını gösteren bir çıktı göreceksiniz.

---

![1748507334934](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748507334934.png)


---

### 🌐 Uygulama localhost:8000 Üzerinde Çalışıyor

Uygulama artık **localhost:8000** adresinde çalışıyor. Uygulamaya erişmek için aşağıdaki bağlantıya tıklayabilir veya tarayıcınıza bu adresi kopyalayabilirsiniz:

👉 `http://127.0.0.1:8000`

---

### 🧪 Uygulamayı Test Etme

Arayüz açıldığında, geliştirdiğiniz sesli asistanı test etmek için bu arayüzü kullanabilirsiniz.

---

### ⏹️ Uygulamayı Durdurma

Uygulamayı durdurmak için terminalde **Ctrl + C** tuşlarına basın.

---

![1748507379134](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748507379134.png)


İşte bu bölümün Türkçeye çevrilmiş hali, başlıkla birlikte:

---

### ✅ Özellikleri ve Girdileri Test Etmeyi Unutmayın

Tüm farklı giriş türlerini ve uygulama özelliklerini test ettiğinizden emin olun.

🔄 **En önemlisi:**

Ses ayarını İspanyolca bir sese geçirmeyi deneyin.

🧑‍💻 Ayrıca:

* Mesaj kutusunu kullanarak bir mesaj yazın,
* Mikrofona tıklayarak sesli mesaj göndermeyi deneyin.

---

### ⚠️ Not

Tarayıcınız yeni sekmeyi açmayı engelleyebilir.

Uygulamanın düzgün çalışabilmesi için buna izin vermeniz gerekebilir.


---

### ☁️ Adım 9: Code Engine Üzerine Yayınlama (İSTEĞE BAĞLI)

📌 **ÖNEMLİ NOT:**

Yayına alma (deploy) işlemi yaparken, **kendi API anahtarınızı (API KEY)** ve **Watsonx Proje ID’nizi** kullanmanız gerekmektedir.

---

### 🌍 Uygulamanızı Yayınlamak İster misiniz?

Uygulamanızı herkesin erişimine açmak ve çevrimiçi olarak barındırmak isterseniz, aşağıdaki adımları izleyerek bunu gerçekleştirebilirsiniz. Yayınlama işlemi **IBM Cloud’un Code Engine** hizmeti üzerinden yapılacaktır.

 **IBM Cloud Code Engine** , konteynerleştirilmiş iş yüklerini çalıştırmak için güvenli, ölçeklenebilir ve sunucusuz bir ortam sağlayan, tam yönetilen bir bulut hizmetidir. Geliştiricilerin altyapı yönetimiyle uğraşmadan kodlarını yayınlamasını sağlar.

---

### 🧪 Bölüm 1: Skills Network Code Engine Ortamına Geçici Yayınlama

Bu bölümdeki adımlar, uygulamanızın düzgün çalışıp çalışmadığını test etmek için **Skills Network Code Engine ortamına** geçici olarak yayına alınmasını sağlar. Bu ortam birkaç gün içinde otomatik olarak silinir.

---

### 🛠️ Adım 1: Code Engine Projesi Oluşturma

1. Sol taraftaki gezinme panelinde **Skills Network Toolbox** seçeneğini bulun.
2. Bu menüyü açın ve **CLOUD** bölümünü genişletin.
3. Ardından **Code Engine** seçeneğine tıklayın.
4. Son olarak **Create Project (Proje Oluştur)** butonuna tıklayın.

---

![1748507481687](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748507481687.png)


---

### 💻 Adım 2: Code Engine CLI Butonuna Tıklayın

Aynı sayfa üzerinden **Code Engine CLI** butonuna tıklayın.

Bu işlem, yeni bir terminal penceresi açar ve her şey önceden ayarlanmış şekilde sizi bir Code Engine projesine otomatik olarak giriş yapmış hâlde başlatır.

---

![1748507528023](image/module_6_2_BabelFish(LanguageTranslator)withLLM,STT,&TTS/1748507528023.png)


---

### 🚀 Adım 9: Code Engine Üzerinden Yayınlama (İSTEĞE BAĞLI)

📌 **DİKKAT:** Yayınlama sırasında mutlaka **kendi API anahtarınızı** ve **Watsonx Proje ID’nizi** kullanmanız gerekir.

---

## 🔹 Bölüm 1: Skills Network Ortamında Test Amaçlı Yayınlama

---

### ☁️ Adım 1: Code Engine Projesi Oluşturma

* Sol menüde **Skills Network Toolbox** > **CLOUD** > **Code Engine** yolunu izleyin.
* **Create Project** butonuna tıklayın.

---

### 💻 Adım 2: Code Engine CLI Terminalini Açma

* Aynı sayfada **Code Engine CLI** butonuna tıklayın.
* Yeni terminal otomatik olarak açılır ve gerekli ayarlarla bir projeye giriş yapar.

---

### 🗣️ Adım 3: Speech-to-Text Servisini Yayınlama

Terminalde şu komutu çalıştırın:

```bash
ibmcloud ce application create --name speech-to-text \
  --env ACCEPT_LICENSE=true \
  --image us.icr.io/sn-labsassets/speech-standalone:latest \
  --port 1080 \
  --registry-secret icr-secret \
  --min-scale 1 \
  --visibility project
```

✔ Komut tamamlandığında terminalde bir URL dönecek.

Bu URL’yi `worker.py` dosyasındaki `speech_to_text` fonksiyonunda `base_url` olarak güncelleyin.

---

### 🔊 Adım 4: Text-to-Speech Servisini Yayınlama

Benzer şekilde şu komutu çalıştırın:

```bash
ibmcloud ce application create --name text-to-speech \
  --env ACCEPT_LICENSE=true \
  --image us.icr.io/sn-labsassets/tts-standalone:latest \
  --port 1080 \
  --registry-secret icr-secret \
  --min-scale 1 \
  --visibility project
```

✔ Bu servis için dönen URL’yi `worker.py` dosyasındaki `text_to_speech` fonksiyonuna ekleyin.

---

### 🧠 Adım 5: Ana Uygulamayı Yayınlama

```bash
# Önce API_KEY ve PROJECT_ID bilgilerinizi worker.py içine ekleyin

ibmcloud ce application create --name personal-assistant \
  --build-source . \
  --build-context-dir . \
  --image us.icr.io/${SN_ICR_NAMESPACE}/personal-assistant:latest \
  --registry-secret icr-secret \
  --port 8000 \
  --min-scale 1 \
  --visibility project
```

✔ Yayınlama tamamlandığında terminalde size canlı bir uygulama bağlantısı dönecektir.

---

## 🔹 Bölüm 2: Kendi IBM Cloud Hesabınıza Yayınlama

---

### 👤 Adım 1: IBM Cloud Hesabınıza Giriş Yapın

```bash
ibmcloud login -u YOUR_EMAIL
```

🔐 Eğer federated ID kullanıyorsanız:

```bash
ibmcloud login --sso
```

💼 Kaynak grubunu hedefleyin:

```bash
ibmcloud target -g Default
```

---

### 🔑 Adım 2: IBM Entitled Registry'ye Giriş

IBM Container Library’den **Entitlement Key** alın.

Yalnızca bir yıl süreyle geçerli olan bu anahtar ile özel Watson konuşma imajlarını indirebilirsiniz.

```bash
IBM_ENTITLEMENT_KEY="YOUR_IBM_ENTITLEMENT_KEY"
echo $IBM_ENTITLEMENT_KEY | docker login -u cp --password-stdin cp.icr.io
```

---

### 🏗️ Adım 3–4: Speech-to-Text ve Text-to-Speech İmajlarını Oluşturma

```bash
cd /home/project/translator-with-voice-and-watsonx/models/stt
docker build ./speech-to-text -t stt-standalone:latest

cd /home/project/translator-with-voice-and-watsonx/models/tts
docker build ./text-to-speech -t tts-standalone:latest
```

---

### 📦 Adım 5: Namespace Oluştur ve ICR'ye Giriş

```bash
NAMESPACE=personal-assistant
ibmcloud cr region-set global
ibmcloud cr namespace-add ${NAMESPACE}
ibmcloud cr login
```

---

### 📤 Adım 6: Watson İmajlarını Pusha Gönderme

```bash
TTS_APPNAME=tts-standalone
STT_APPNAME=stt-standalone
REGISTRY=icr.io

docker tag ${TTS_APPNAME}:latest ${REGISTRY}/${NAMESPACE}/${TTS_APPNAME}:latest
docker push ${REGISTRY}/${NAMESPACE}/${TTS_APPNAME}:latest

docker tag ${STT_APPNAME}:latest ${REGISTRY}/${NAMESPACE}/${STT_APPNAME}:latest
docker push ${REGISTRY}/${NAMESPACE}/${STT_APPNAME}:latest
```

---

### 🧱 Adım 7: Ana Uygulama İmajını Oluştur ve Yayınla

```bash
APP_NAME=watsonx-personal-assistant

cd /home/project/translator-with-voice-and-watsonx
docker build . -t ${APP_NAME}:latest
docker tag ${APP_NAME}:latest ${REGISTRY}/${NAMESPACE}/${APP_NAME}:latest
docker push ${REGISTRY}/${NAMESPACE}/${APP_NAME}:latest
```

---

### 🌍 Adım 8: Uygulama ve Servisleri Code Engine'e Yayınlama

#### Bölge ve kaynak grubu hedefle:

```bash
REGION=us-south
RESOURCE_GROUP=Default
ibmcloud target -r ${REGION} -g ${RESOURCE_GROUP}
```

#### Code Engine projesi oluştur:

```bash
ibmcloud ce project create --name personal-assistant
ibmcloud ce project select --name personal-assistant
```

#### Watson STT ve TTS Servislerini Yayınla:

```bash
ibmcloud ce application create \
  --name ${STT_APPNAME} \
  --port 1080 --min-scale 1 --max-scale 2 \
  --cpu 2 --memory 8G \
  --image private.${REGISTRY}/${NAMESPACE}/${STT_APPNAME}:latest \
  --registry-secret ce-auto-icr-private-${REGION} \
  --visibility project \
  --env ACCEPT_LICENSE=true

ibmcloud ce application create \
  --name ${TTS_APPNAME} \
  --port 1080 --min-scale 1 --max-scale 2 \
  --cpu 2 --memory 8G \
  --image private.${REGISTRY}/${NAMESPACE}/${TTS_APPNAME}:latest \
  --registry-secret ce-auto-icr-private-${REGION} \
  --visibility project \
  --env ACCEPT_LICENSE=true
```

🎯 URL çıktısını `worker.py` dosyasındaki `base_url` değerleriyle değiştirin.

---

#### Ana Uygulamayı Yayınla:

```bash
ibmcloud ce application create \
  --name ${APP_NAME} \
  --port 8000 --min-scale 1 --max-scale 2 \
  --cpu 1 --memory 4G \
  --image private.${REGISTRY}/${NAMESPACE}/${APP_NAME}:latest \
  --registry-secret ce-auto-icr-private-${REGION} \
  --env ACCEPT_LICENSE=true
```

⏳ Yayınlama birkaç dakika sürebilir. Başarılı olursa terminalde URL çıktısı alırsınız.

---

### 🔍 Adım 9: Yayınlamayı Kontrol Etme

Durum, log ve olayları kontrol etmek için:

```bash
ibmcloud ce app list
ibmcloud ce app logs --application ${APP_NAME}
ibmcloud ce app events --application ${APP_NAME}
```

---


---

### 🎉 Sonuç

Tebrikler! Watsonx kullanarak kendi sesli asistanınızı oluşturduğunuz bu yönlendirmeli projeyi başarıyla tamamladınız!

Umarız asistanlar ve web geliştirme hakkında yeni şeyler öğrenmekten keyif almışsınızdır ve artık bu projeyi geliştirecek bilgi ve becerilere sahipsinizdir.

---

### 🧩 Neler Öğrendiniz?

Bu proje boyunca bir asistanın temel bileşenlerini öğrendiniz:

* **Speech-to-Text (Konuşmadan Metne)** teknolojisi
* **flan-ul2 ile Doğal Dil İşleme (NLP)**
* **Text-to-Speech (Metinden Konuşmaya)** teknolojisi
* **Python, Flask, HTML, CSS ve JavaScript** ile web geliştirme

---

### 💡 Gelecek İçin İlham

Bu yolculukta bizimle olduğunuz için teşekkür ederiz. Yapay zekâ alanını keşfetmeye ve öğrenmeye devam etmenizi teşvik ediyoruz.

Becerilerinizi kullanarak **sorumlu, etik ve faydalı** asistanlar oluşturmanızı diliyoruz.

Gelecekte neler geliştireceğinizi görmek için sabırsızlanıyoruz!

---

### 🔜 Sıradaki Adımlar

Artık Speech-to-Text ve Text-to-Speech yeteneklerini kullanan bir uygulama geliştirdiniz.

Kendi projelerinizde **IBM Watson Speech Libraries for Embed** kullanmak isterseniz, aşağıdaki bağlantılar üzerinden ücretsiz deneme sürümüne kaydolabilirsiniz:

* [Speech-to-Text](#)
* [Text-to-Speech](#)

---

### 🎯 Prompt Engineering ile Daha Fazlasını Yapabilirsiniz

Bu projede oluşturduğunuz sesli asistan, **prompt engineering** sayesinde çok daha fazlasını yapabilecek kapasitededir.

 **Prompt engineering** , doğal dil işleme modellerine verilen girdileri dikkatlice tasarlayarak belirli türde çıktılar elde etme sürecidir. Aşağıda birkaç örnek kullanım senaryosu bulabilirsiniz:

---

#### 🧠 Terapist Asistan

Zihinsel sağlık desteği sunmak için şu tür bir prompt kullanılabilir:

🗣️ *"Merhaba, bugün çok stresliyim ve bunalmış hissediyorum. Bu duygularla başa çıkmama yardımcı olur musun?"*

💬 Asistan: Empati, tavsiye ve cesaretlendirici yanıtlar sunar.

---

#### 🔧 Otomobil Teknisyeni

Araç arızalarını analiz etmek için şu tür bir prompt kullanılabilir:

🗣️ *"Arabam hızlanırken garip bir ses çıkarıyor. Bunun nedeni ne olabilir?"*

💬 Asistan: Olası nedenleri ve çözümleri önerir.

---

#### 📖 Hikâye Anlatıcısı

Özgün hikâyeler oluşturmak için şu tür bir prompt kullanılabilir:

🗣️ *"Bir zamanlar bir kalede yaşayan genç bir prenses varmış. Bir gün hayatını sonsuza dek değiştiren büyülü bir hediye almış. Bu hediye neydi ve hayatını nasıl değiştirdi?"*

💬 Asistan: Eşsiz ve etkileyici bir hikâye üretir.

---

#### 👩‍🏫 Profesör Asistan

Eğitim amaçlı kullanım için şu tür bir prompt kullanılabilir:

🗣️ *"Bu derste maddenin özelliklerini öğreneceğiz. Maddenin üç hâli nelerdir?"*

💬 Asistan: Açıklamalar yapar, ardından mini bir sınav sunar.

---

### 💼 Son Söz

Doğru şekilde tasarlanmış prompt’lar ve flan-ul2’nin gücü ile çok çeşitli görevleri yerine getiren bir asistan geliştirebilirsiniz.

İhtiyacınız olan tek şey, kullanıcıya hangi çıktıyı vermek istediğinizi düşünerek doğru prompt’ları oluşturmaktır.

💡 Artık geriye sadece bu prompt’ları çevreleyecek güzel bir kullanıcı arayüzü tasarlamak kalıyor…

ve belki de bu, sizi milyon dolarlık bir iş fikrine götürebilir 😉!

---
