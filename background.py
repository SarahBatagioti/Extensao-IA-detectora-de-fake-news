import pyautogui
import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/texto')
def obter_texto():
    # Espera 2 segundos para dar tempo de mudar de aba
    time.sleep(2)
    # Captura a tela e extrai o texto com OCR (reconhecimento óptico de caracteres)
    imagem = pyautogui.screenshot()
    texto = pyautogui.image_to_string(imagem, lang='por')
    # Retorna o texto como JSON
    return jsonify(texto=texto)

if __name__ == '__main__':
    app.run()
