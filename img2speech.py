from PIL import Image
import pytesseract
from gtts import gTTS

# specifies the path to tesseract on your machine
pytesseract.pytesseract.tesseract_cmd = 'tesseract'

# upload of the image in which text shall be extracted
image = Image.open('/home/iamdharrenzug/projects/CodeAlpha-img2speech/cat.jpeg')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

#
print("Extracted Text:")
print(text)

# Converting the extracted text to speech
tts = gTTS(text)
tts.save('output.mp3')

# Play the generated speech
import os
os.system('mpg123 output.mp3')