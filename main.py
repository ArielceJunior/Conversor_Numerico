from flask import Flask, render_template, request;

app = Flask(__name__)
app.secret_key = '123'

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def decimal_to_hexadecimal(decimal):
    if decimal == 0:
        return "0"
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
        decimal = decimal // 16
    return hexadecimal



@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/conversors', methods=['GET', 'POST'])
def conversors():
    result = None
    if request.method == 'POST':
        decimal_number = request.form.get('decimal_number', type=str)
        if decimal_number and decimal_number.isdigit():
            result = decimal_to_binary(int(decimal_number))
        else:
            result = "Por favor, insira um número decimal válido."
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
