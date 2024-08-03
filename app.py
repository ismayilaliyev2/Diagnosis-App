from flask import Flask, request, render_template_string, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure MySQL connection
db_config = {
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'your_db_host',
    'database': 'your_db_name'
}

scoring_system = {
    # Define your scoring system here
}

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Input Form</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 600px;
                margin: auto;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            h2 {
                color: #555;
                margin-top: 20px;
            }
            .button {
                background-color: #28a745;
                color: #fff;
                border: none;
                padding: 10px 15px;
                margin: 5px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            .button:hover {
                background-color: #218838;
            }
            .selected {
                background-color: #155724 !important;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Select inputs to calculate their score:</h1>
            <form action="/page1" method="post">
                <input type="hidden" name="input1" id="input1">
                <input type="hidden" name="input2" id="input2">
                <input type="hidden" name="input3" id="input3">
                <input type="hidden" name="input4" id="input4">
                <input type="hidden" name="input5" id="input5">
                <input type="hidden" name="input6" id="input6">
                <input type="hidden" name="input7" id="input7">
                <input type="hidden" name="input8" id="input8">
                <input type="hidden" name="input9" id="input9">
                <input type="hidden" name="input10" id="input10">
                <input type="hidden" name="input11" id="input11">
                <input type="hidden" name="input12" id="input12">
                <input type="hidden" name="input13" id="input13">
                <input type="hidden" name="input14" id="input14">
                <input type="hidden" name="input15" id="input15">
                <input type="hidden" name="input16" id="input16">
                <input type="hidden" name="input17" id="input17">
                <input type="hidden" name="input18" id="input18">
                <input type="hidden" name="input19" id="input19">
                <input type="hidden" name="input20" id="input20">
                <button type="submit" class="button">Calculate</button>
                <button type="submit" formaction="/save" class="button">Save</button>
            </form>
        </div>
    </body>
    </html>
    ''')

@app.route('/page1', methods=['POST'])
def page1():
    for i in range(1, 21):
        session[f'input{i}'] = request.form.get(f'input{i}')
    
    inputs = [session.get(f'input{i}', '') for i in range(1, 21)]
    total_score = sum(scoring_system.get(input, 0) for input in inputs)
    
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculation Result</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 600px;
                margin: auto;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            p {
                color: #555;
                font-size: 18px;
            }
            a {
                color: #007bff;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Result:</h1>
            <p>The total score is: {{ total_score }}</p>
            <a href="/">Go back</a>
        </div>
    </body>
    </html>
    ''', total_score=total_score)

@app.route('/save', methods=['POST'])
def save():
    for i in range(1, 21):
        session[f'input{i}'] = request.form.get(f'input{i}')
    
    inputs = [session.get(f'input{i}', '') for i in range(1, 21)]
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO your_table_name (input1, input2, input3, input4, input5, input6, input7, input8, input9, input10,
                                     input11, input12, input13, input14, input15, input16, input17, input18, input19, input20)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', inputs)
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))

# Run the Flask application
def run_app():
    app.run(host='0.0.0.0', port=8003, debug=True, use_reloader=False)

if __name__ == "__main__":
    run_app()
