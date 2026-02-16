from pytesseract import Output
import cv2
import pytesseract
import re

def main():
    input_path = "img/testes.jpg"
    config_tesseract = "--tessdata-dir tessdata"
  
    img = cv2.imread(input_path)
    if img is None:
        print(f"Arquivo '{input_path}' não encontrado.")
        return
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    data=pytesseract.image_to_data(rgb,config=config_tesseract,lang="por", output_type=Output.DICT)
    pattern = r"\b(?:0?[1-9]|[12][0-9]|3[01])/(?:0?[1-9]|1[0-2])\b"
    img=draw_boxes(rgb, data, pattern)
    out_path = "regular.png"
    out_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(out_path, out_bgr) 

    
def draw_boxes(img, data, pattern, color=[255,100,0]):
    min_conf=0
    for i in range(0, len(data['text'])):
        if int(data['conf'][i]) > min_conf:
            text=data['text'][i]
            if re.match(pattern, text):
                (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    return img


if __name__ == "__main__":
    main()