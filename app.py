from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, mode):
    if mode == "decode":
        shift = -abs(shift)
    else:
        shift = abs(shift)

    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += new_char
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        action = request.form['action']

        if action == 'encode':
            result = caesar_cipher(text, shift, "encode")
        elif action == 'decode':
            result = caesar_cipher(text, shift, "decode")

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
