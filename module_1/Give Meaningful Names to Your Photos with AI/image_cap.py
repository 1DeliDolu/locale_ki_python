import os
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Modell vorbereiten
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Bildpfad
img_path = "/home/project/my_env/67357898_354277512135149_6815123615596412928_n.jpg"

# Bild prüfen und laden
if not os.path.exists(img_path):
    raise FileNotFoundError(f"Bild nicht gefunden: {img_path}")

image = Image.open(img_path).convert('RGB')

# Eingabedaten vorbereiten
inputs = processor(images=image, text="the image of", return_tensors="pt")

# Bildbeschreibung erzeugen
outputs = model.generate(**inputs, max_length=50)
caption = processor.decode(outputs[0], skip_special_tokens=True)

# Ergebnis anzeigen
print("📸 Bildbeschreibung:", caption)
