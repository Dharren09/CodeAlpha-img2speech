# CodeAlpha Image to Speech Generator

## Description

CodeAlpha Image to Speech Generator is a Python-based tool that allows you to convert text found in images to spoken words. It utilizes Optical Character Recognition (OCR) to extract text from images and then uses a Text-to-Speech (TTS) engine to convert the extracted text into audio. It's my first Task as a python intern at CodeAlpha

## Features

- Easy conversion of image text to speech.
- Supports various image formats.
- Customizable TTS settings.
- User-friendly command-line interface.

## Prerequisites

- Python 3.x
- sudo apt-get install
  - tesseract-ocr
  - mpg123
- Required Python packages (install using `pip`):
  - pytesseract
  - Pillow
  - gTTS

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/CodeAlpha-img2speech.git

2. Navigate the directory

   ```bash
   cd CodeAlpha-img2speech

2. Install the packages

   ```bash
   pip install pytesseract pillow
   pip install gTTS

4. Run the script

   ```bash
   python3 img2speech.py your_image.png

NB: your_image.png == path to your image you want to convert

## Contributing
Contributions are welcome! Feel free to open issues and pull requests to suggest improvements or report bugs.

## Contact
For questions or feedback, you can reach me at dharrydharrenzerah@gmail.com

Happy coding!
