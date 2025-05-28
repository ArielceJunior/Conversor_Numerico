from flask import Flask, render_template, request;

app = Flask(__name__)
app.secret_key = '123'

# Conversão de decimal para binário
def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary
# Conversão de decimal para hexadecimal
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
# Conversão de decimal para octal
def decimal_to_octal(decimal):
    if decimal == 0:
        return "0"
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal
# Conversão de binario para decimal
def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal
# Conversão de binario para hexadecimal
def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_hexadecimal(decimal)
# Conversão de binario para octal   
def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_octal(decimal)
# Conversão de hexadecimal para decimal
def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    for digit in hexadecimal:
        decimal = decimal * 16 + int(digit, 16)
    return decimal
# Conversão de hexadecimal para binário
def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_binary(decimal)
# Conversão de hexadecimal para octal
def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_octal(decimal)
# Conversão de octal para decimal
def octal_to_decimal(octal):
    decimal = 0
    for digit in octal:
        decimal = decimal * 8 + int(digit)
    return decimal
# Conversão de octal para binário
def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_binary(decimal)
# Conversão de octal para hexadecimal
def octal_to_hexadecimal(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_hexadecimal(decimal)


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/integrantes.html')
def about():
    return render_template('integrantes.html')

@app.route('/descricao.html')
def description():
    return render_template('descricao.html')

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
