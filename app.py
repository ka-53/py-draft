from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Настройки для подключения к базе данных
db_config = {
    'host': 'localhost',
    'user': 'root',  # По умолчанию для XAMPP
    'password': '',  # По умолчанию пароль пустой
    'database': 'my_data'
}

# Маршрут для отображения формы
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для обработки данных формы
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    
    # Подключение к базе данных и вставка данных
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()
    
    return "New record created successfully"

if __name__ == '__main__':
    app.run(debug=True)
