
---

### ⏱️ Tahmini Okuma Süresi: 15 dakika

---

### 🎯 Öğrenme Hedefleri

Bu okumayı tamamladıktan sonra şunları yapabileceksiniz:

* Flask’ın temel özelliklerini açıklamak
* Bir Flask uygulamasının kurulum kodunu göstermek

---

### 📘 Giriş

Flask, Python ile yazılmış bir mikro web çatısıdır (framework). Mikro-çatı olarak adlandırılmasının sebebi, araçlar veya kütüphaneler gerektirmemesidir. Ancak, Flask'a entegre edilmiş gibi çalışan genişletmeler (extensions) sayesinde uygulama özellikleri eklenebilir. Bu genişletmeler; nesne-ilişkisel eşleyiciler (ORM), form doğrulama, dosya yükleme işlemleri, çeşitli açık kimlik doğrulama teknolojileri ve diğer yaygın framework araçlarını kapsar. Bu esneklik, Flask’ı geliştirme ihtiyaçlarına uyumlu hale getirir ve küçük projelerden karmaşık, veri odaklı sitelere kadar birçok web uygulamasının temeli olarak kullanılmasını sağlar.

---

### 🌟 Flask’ın Temel Özellikleri

* **Basitlik** : Flask’ın anlaşılması kolay ve sade sözdizimi, onu hem yeni başlayanlar hem de deneyimli geliştiriciler için erişilebilir ve güçlü kılar.
* **Esneklik** : Veritabanı entegrasyonu, kimlik doğrulama ve dosya yükleme gibi özellikleri eklemek için genişletmelerle büyütülebilir.
* **Geliştirme sunucusu ve hata ayıklayıcı** : Flask, yerleşik bir geliştirme sunucusu ve hata ayıklayıcıya sahiptir. Hafif ve kullanımı kolay bu sunucu, geliştirme ve test aşamaları için idealdir.
* **Birim test desteği** : Flask, birim test desteğini yerleşik olarak sunar. Bu sayede geliştiriciler uygulamalarının güvenilirliğini testlerle doğrulayabilir.
* **RESTful istek yönlendirme** : Flask, modern web uygulamaları ve mobil servisler için önemli olan RESTful API’lerin kolayca oluşturulmasını sağlar.
* **Jinja2 şablonlama** : Flask, HTML ile dinamik web sayfaları oluşturmayı kolaylaştıran Jinja2 şablon motorunu kullanır. Jinja2 güçlü ve esnektir; şablon miras alma ve otomatik HTML kaçış gibi güvenlik özellikleri sunar.

---

### 🚀 Flask ile Başlarken

Flask uygulaması kurmak birkaç temel adım içerir:

* **Kurulum** : Flask, Python’un paket yöneticisi olan pip ile kurulabilir. Terminal veya komut istemcisine `pip install Flask` komutunu yazmanız yeterlidir.
* **Flask uygulaması oluşturma** :
* Flask paketinden Flask sınıfını içe aktarın ve bu sınıftan bir örnek oluşturun. Bu örnek, WSGI uygulamanız olacaktır.
* `@app.route()` dekoratörünü kullanarak rotalar tanımlayın. Rotalar, belirli bir URL'den gelen isteğe karşılık hangi işlevin çağrılacağını Flask’a bildirir.
* Her işlev, istemciye gönderilecek yanıt içeriğini döner.
* **Flask uygulamasını çalıştırma** : Uygulamayı çalıştırmak için terminalde `flask run` komutunu kullanın. Bu komut, uygulamanızı test etmek için yerel bir geliştirme sunucusu başlatır.

---

### 💡 Örnek: Flask Uygulaması

Bu basit uygulama, kök URL’ye erişildiğinde “Hello, World!” yanıtı dönen bir web sunucusu oluşturur:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 🧾 Sonuç

Flask, Python ekosisteminde hafif, esnek bir çatı olarak öne çıkar ve geliştiricilere basit web sayfalarından karmaşık, veri odaklı sitelere kadar geniş yelpazede uygulamalar geliştirme gücü verir. Sadeliği ve genişletilebilirliği sayesinde Flask, hem yeni başlayanlar hem de deneyimli geliştiriciler için mükemmel bir tercihtir. Flask’ın sunduğu olanakları ve zengin genişletme ekosistemini kullanarak, web geliştirme projelerinizi verimli ve kolay şekilde hayata geçirebilirsiniz.

---
