import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Modell und Prozessor laden
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Bildbeschriftungsfunktion
def caption_image(input_image: np.ndarray):
    # numpy → PIL → RGB
    raw_image = Image.fromarray(input_image).convert('RGB')

    # Vorverarbeitung
    inputs = processor(images=raw_image, text="the image of", return_tensors="pt")

    # Bildbeschreibung erzeugen
    outputs = model.generate(**inputs, max_length=50)

    # Ausgabe dekodieren
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return caption

# Gradio-Interface
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="🖼️ Bildbeschreibung mit KI",
    description="Ein einfaches Web-Interface zur automatischen Beschreibung von Bildern mithilfe eines vortrainierten Transformers."
)

# App starten
iface.launch()
