import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image


image = cv2.imread("D:/project/test1.jpg")
pytesseract.pytesseract.tesseract_cmd = r'D:\Python\Scripts\Tesseract-OCR\tesseract.exe'
string = pytesseract.image_to_string(image, lang="rus")
image_copy = image.copy()
target_word = "dog"
data = pytesseract.image_to_data(image, lang="rus", output_type=pytesseract.Output.DICT)
word_occurences = [ i for i, word in enumerate(data["text"]) if word.lower() == target_word ]
for occ in word_occurences:
    # извлекаем ширину, высоту, верхнюю и левую позицию для обнаруженного слова
    w = data["width"][occ]
    h = data["height"][occ]
    l = data["left"][occ]
    t = data["top"][occ]
    # определяем все точки окружающей рамки
    p1 = (l, t)
    p2 = (l + w, t)
    p3 = (l + w, t + h)
    p4 = (l, t + h)
    # рисуем 4 линии (прямоугольник)
    image_copy = cv2.line(image_copy, p1, p2, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p2, p3, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p3, p4, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p4, p1, color=(255, 0, 0), thickness=2)
print(string)
plt.imsave("all_dog_words.png", image_copy)
plt.imshow(image_copy)
plt.show()