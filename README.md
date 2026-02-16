# use OCR to search photos for specific content using regular expressions

Formato da expressão regular:
- mês/ano

Configurações e instruções para instalar e executar no Linux (Python 3).

## Requisitos
- Linux com apt
- Python 3

## Instalação (sistema + ambiente Python)
```bash
sudo apt update
sudo apt install -y tesseract-ocr tesseract-ocr-por
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install opencv-python pytesseract notebook
```

## Baixar linguagem (Português e inglês)
Crie a pasta `tessdata` (se necessário) e baixe o arquivo:
```bash
mkdir -p tessdata
wget -O tessdata/por.traineddata "https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata?raw=true"
wget -O tessdata/eng.traineddata "https://github.com/tesseract-ocr/tessdata/blob/main/eng.traineddata?raw=true"
```

## Executar o projeto
```bash
python3 main.py
```

## Saída
Uma imagem será gerada no diretório raiz:
- `regular.png`

![Select text boxes](regular.png)