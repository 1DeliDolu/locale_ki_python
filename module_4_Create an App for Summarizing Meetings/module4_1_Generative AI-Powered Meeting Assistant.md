
---

### 🎥 Proje Tanıtımı: Yapay Zeka Destekli Toplantı Asistanı

Bu video, üretken yapay zeka destekli bir toplantı asistanı projesine genel bir bakış sunar. Kendinizi bir beyin fırtınası toplantısında hayal edin: fikirler hızla uçuşuyor ve bilgi parçacıkları paylaşılıyor. Notlar alıyorsunuz ama her şeyi yakalayabiliyor musunuz? Daha sonra, önemli kararları veya belirli eylem maddelerini hatırlamak zorlayıcı hale gelebilir.

---

### 🧠 İhtiyaca Cevap Veren Uygulama: ASR ve LLM

Bu noktada, toplantı tartışmalarını yazıya döküp özetleyebilen yenilikçi, üretken yapay zeka tabanlı bir uygulama faydalı olabilir. Hayal edin: bir uygulama, toplantı konuşmalarını doğru bir şekilde metne dönüştürebiliyor ve ardından önemli noktaları ve alınan kararları öne çıkaran kısa bir özet sunuyor.

Bu, otomatik konuşma tanıma (ASR) teknolojisi ile üretken büyük dil modellerinin (LLM'ler) birleşiminin gücüdür. ASR teknolojisi konuşulan dili okunabilir metne dönüştürür. Ardından bir LLM, bu metni anlayarak etkili bir şekilde özetler. LLM aynı zamanda konuşmadan metne dönüştürülmüş çıktıyı küçük hataları düzelterek daha anlaşılır ve doğru hale getirebilir.

---

### 🛠 Proje Adımları: Araçlar ve Teknolojiler

Bu proje, böyle bir uygulamayı nasıl inşa edeceğinizi adım adım anlatır. Aşağıdaki araçları kullanacaksınız:

* **OpenAI Whisper** : Sesin metne dönüştürülmesi için kullanılacak ASR aracı.
* **Llama 2** : Meta tarafından geliştirilen güçlü bir açık kaynak dil modeli; özetleme ve anahtar noktaları çıkartmak için kullanılacak.
* **Gradio** : Uygulama için sezgisel ve kullanıcı dostu bir arayüz oluşturmak için kullanılacak.
* **IBM watsonx** : Llama 2 modelinin barındırıldığı platform.
* **IBM Code Engine** : Uygulamayı çevrim içi dağıtmak için sunucusuz (serverless) bir platform.

---

### 💻 Uygulamanın İşleyişi

İlk olarak, örnek bir ses dosyası kullanarak OpenAI Whisper ile sesi metne dönüştüreceksiniz. Ardından, Gradio kullanarak sezgisel bir arayüz oluşturacaksınız. Sonraki adımda, IBM watsonx üzerinde barındırılan Llama 2 modeli ile bu metni özetleyeceksiniz. Bu süreçte, modeli kullanmak ve çıktısını etkileyen bazı temel parametreleri anlamak için bir Python betiği geliştireceksiniz.

Son olarak, uygulamayı IBM Code Engine aracılığıyla çevrim içi dağıtmayı öğreneceksiniz. Tüm bu adımlarda Python diliyle kodlama yapılacağı için temel seviyede Python bilgisine sahip olmanız gerekmektedir.

---

### 📱 Uygulama Arayüzü ve Çıktılar

Uygulamanın arayüzünde "Audio Transcription App" başlığı yer alır. Kayıtlı ses dosyasını yüklemek için yükleme simgesine tıklayabilir ve ardından “Submit” düğmesine basabilirsiniz. Uygulama, ses dosyasının içeriğine dair özet ve önemli noktaları çıktı olarak gösterecektir.

---

### 🎯 Proje Hedefleri ve Kazanımlar

Bu projeyi tamamladığınızda aşağıdaki hedeflere ulaşmış olacaksınız:

* LLM’lerin metin üretme, düzeltme ve özetleme süreçlerine nasıl katkı sağladığını açıklayabilme
* Konuşmayı metne dönüştürmek için otomatik konuşma tanıma teknolojisini uygulama
* Kullanıcı dostu bir uygulama arayüzü tasarlama
* Bir uygulamayı bulut tabanlı bir platformda çevrim içi dağıtma

---

### 🚀 Yetkinlik Gelişimi

Bu proje sayesinde, metin üretimi ve özetleme görevleri için LLM kullanımı konusunda sağlam bir temel atacak ve Python programlama becerilerinizi sergileme fırsatı bulacaksınız. Yapay zeka destekli konuşma-metne dönüştürme ve üretken yapay zeka teknolojilerinden yararlanarak bir uygulama geliştirme ve dağıtma deneyimi kazanacaksınız.

Hazır olun, becerilerinizi uygulayın ve bir üst seviyeye taşıyın!
