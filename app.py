from flask import Flask, render_template_string, request, session, redirect, url_for
import threading
from flask_session import Session

# Define the scoring system
scoring_system = {
    "pozisyona_bagli": 1,
    "pozisyona_bagli_deyil": 0,
    "beli": 1,
    "xeyr": 0,
    "olub": 0,
    "olmuyub": 1,
    "0san-3deq":1,
    "23saat-4-5gun":6,
    "10deq-23saat":17,
    "davamli":18,
    "heqiqi":1,
    "yalanci":7
}

# Define the Flask application
app = Flask(__name__)
app.secret_key = 'meowmeow'

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>String Scoring System</title>
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

                <h2>Question 1: Başgicəllənmə nə vaxt baş verir?</h2>
                <div id="input1_buttons">
                    <button type="button" class="button" id="btn_input1_pozisyona_bagli" onclick="selectInput('input1', 'pozisyona_bagli', 'btn_input1_pozisyona_bagli')">Pozisyona bağlı</button>
                    <button type="button" class="button" id="btn_input1_pozisyona_bagli_deyil" onclick="selectInput('input1', 'pozisyona_bagli_deyil', 'btn_input1_pozisyona_bagli_deyil')">Pozisyona bağlı deyil</button>
                </div>

                <h2>Question 2: Heç baş nahiyyəsindən travma almısınız mı?</h2>
                <div id="input2_buttons">
                    <button type="button" class="button" id="btn_input2_beli" onclick="selectInput('input2', 'beli', 'btn_input2_beli')">Bəli</button>
                    <button type="button" class="button" id="btn_input2_xeyr" onclick="selectInput('input2', 'xeyr', 'btn_input2_xeyr')">Xeyr</button>
                </div>

                <h2>Question 3: Başgicəllənmə zamanı eşitmə qabiliyyətiniz dəyişirmi?</h2>
                <div id="input3_buttons">
                    <button type="button" class="button" id="btn_input3_olmuyub" onclick="selectInput('input3', 'olmuyub', 'btn_input3_olmuyub')">Olmuyub</button>
                    <button type="button" class="button" id="btn_input3_olub" onclick="selectInput('input3', 'olub', 'btn_input3_olub')">Olub</button>
                </div>

                <h2>Question 4: Başgicəllənmə zamanı qulaqda dolğunluq və ya ağırlıq hissi varmı?</h2>
                <div id="input4_buttons">
                    <button type="button" class="button" id="btn_input4_olmuyub" onclick="selectInput('input4', 'olmuyub', 'btn_input4_olmuyub')">Olmuyub</button>
                    <button type="button" class="button" id="btn_input4_olub" onclick="selectInput('input4', 'olub', 'btn_input4_olub')">Olub</button>
                </div>

                <h2>Question 5: Başgicəllənmə zamanı və ya ondan dərhal əvvəl qulaqlarınızda vızıltı və ya cingilti hiss edirsiniz?</h2>
                <div id="input5_buttons">
                    <button type="button" class="button" id="btn_input5_olmuyub" onclick="selectInput('input5', 'olmuyub', 'btn_input5_olmuyub')">Olmuyub</button>
                    <button type="button" class="button" id="btn_input5_olub" onclick="selectInput('input5', 'olub', 'btn_input5_olub')">Olub</button>
                </div>

                <h2>Question 6: Son 1 ayda qrip və ya yuxarı tənəffüs yollarının infeksiyası olmusunuzmu?</h2>
                <div id="input6_buttons">
                    <button type="button" class="button" id="btn_input6_olmuyub" onclick="selectInput('input6', 'beli', 'btn_input6_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input6_olub" onclick="selectInput('input6', 'xeyr', 'btn_input6_olub')">Xeyr</button>
                </div>

                <h2>Question 7: İşıq başgicəllənmənizi artırırmı?</h2>
                <div id="input7_buttons">
                    <button type="button" class="button" id="btn_input7_olmuyub" onclick="selectInput('input7', 'beli', 'btn_input7_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input7_olub" onclick="selectInput('input7', 'xeyr', 'btn_input7_olub')">Xeyr</button>
                </div>

                <h2>Question 8: Uzun çəkən başgicəllənmə, ürəkbulanma, qusma və işığa həssalıqla davam edən hallar olubmu?</h2>
                <div id="input8_buttons">
                    <button type="button" class="button" id="btn_input8_olmuyub" onclick="selectInput('input8', 'beli', 'btn_input8_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input8_olub" onclick="selectInput('input8', 'xeyr', 'btn_input8_olub')">Xeyr</button>
                </div>

                <h2>Question 9: Uşaqlıq və ya yeniyetməlik dövründə hərəkət xəstəliyiniz (maşında gedərkən ürəkbulanma, qusma) olubmu?</h2>
                <div id="input9_buttons">
                    <button type="button" class="button" id="btn_input9_olmuyub" onclick="selectInput('input9', 'beli', 'btn_input9_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input9_olub" onclick="selectInput('input9', 'xeyr', 'btn_input9_olub')">Xeyr</button>
                </div>
                
                <input type="submit" class="button" value="Next">
            </form>
        </div>
        <script>
            function selectInput(inputId, value, buttonId) {
                document.getElementById(inputId).value = value;
                let buttons = document.querySelectorAll('#' + inputId + '_buttons .button');
                buttons.forEach(button => {
                    button.classList.remove('selected');
                });
                document.getElementById(buttonId).classList.add('selected');
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/page1', methods=['POST'])
def page1():
    session['input1'] = request.form.get('input1')
    session['input2'] = request.form.get('input2')
    session['input3'] = request.form.get('input3')
    session['input4'] = request.form.get('input4')
    session['input5'] = request.form.get('input5')
    session['input6'] = request.form.get('input6')
    session['input7'] = request.form.get('input7')
    session['input8'] = request.form.get('input8')
    session['input9'] = request.form.get('input9')
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Page 1</title>
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
            .button:focus {
                background-color: #218838;
            }
            .selected {
                background-color: #155724 !important;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Page 1</h1>
            <form action="/page2" method="post">
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

                <h2>Question 10: Başgicəllənmə vaxtı və ya öncəsində baş ağrısı olurmu?</h2>
                <div id="input10_buttons">
                    <button type="button" class="button" id="btn_input10_beli" onclick="selectInput('input10', 'beli', 'btn_input10_beli')">Bəli</button>
                    <button type="button" class="button" id="btn_input10_xeyr" onclick="selectInput('input10', 'xeyr', 'btn_input10_xeyr')">Xeyr</button>
                </div>

                <h2>Question 11: Sizdə tez-tez birtərəfli və pulsasiya edici baş ağrıları olurmu?</h2>
                <div id="input11_buttons">
                    <button type="button" class="button" id="btn_input11_olmuyub" onclick="selectInput('input11', 'beli', 'btn_input11_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input11_olub" onclick="selectInput('input11', 'xeyr', 'btn_input11_olub')">Xeyr</button>
                </div>

                <h2>Question 12: Başgicəllənmə öncəsində başağrısı və ya başgicəllənmə olacağını hiss edirsinizmi?</h2>
                <div id="input12_buttons">
                    <button type="button" class="button" id="btn_input12_olmuyub" onclick="selectInput('input12', 'beli', 'btn_input12_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input12_olub" onclick="selectInput('input12', 'xeyr', 'btn_input12_olub')">Xeyr</button>
                </div>

                <h2>Question 13: Elə başağrılarınız olub ki, buna görə dərman istifadə edib istirahət etmə ehtiyacınız olsun və istirahət sonrası başağrınız keçsin?</h2>
                <div id="input13_buttons">
                    <button type="button" class="button" id="btn_input13_olmuyub" onclick="selectInput('input13', 'beli', 'btn_input13_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input13_olub" onclick="selectInput('input13', 'xeyr', 'btn_input13_olub')">Xeyr</button>
                </div>

                <h2>Question 14: Görmənin ikiləşməsi və ya bulanıq görmə epizodu olubmu? Olubsa neçə dəfə?</h2>
                <div id="input14_buttons">
                    <button type="button" class="button" id="btn_input14_olmuyub" onclick="selectInput('input14', 'beli', 'btn_input14_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input14_olub" onclick="selectInput('input14', 'xeyr', 'btn_input14_olub')">Xeyr</button>
                </div>

                <h2>Question 15: Başgicəllənmə zamanı huşunuzu itirmədən heç yıxıldığınız olubmu?</h2>
                <div id="input15_buttons">
                    <button type="button" class="button" id="btn_input15_olmuyub" onclick="selectInput('input15', 'beli', 'btn_input15_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input15_olub" onclick="selectInput('input15', 'xeyr', 'btn_input15_olub')">Xeyr</button>
                </div>

                <h2>Question 16: Sizə bu günə kimi sinir sistemi ilə bağlı hər hansı diaqnoz qoyulubmu? (Dağınıq skleroz,insult,nevroz və.s)</h2>
                <div id="input16_buttons">
                    <button type="button" class="button" id="btn_input16_olmuyub" onclick="selectInput('input16', 'beli', 'btn_input16_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input16_olub" onclick="selectInput('input16', 'xeyr', 'btn_input16_olub')">Xeyr</button>
                </div>

                <h2>Question 17: Baş gicəllənməsi ilə yanaşı danışıqda çətinlik, udqunmada çətinlik, əl və ayaqlarda zəiflik, ikiqat görmə, üz iflici kimi şikayətləriniz olubmu?</h2>
                <div id="input17_buttons">
                    <button type="button" class="button" id="btn_input17_olmuyub" onclick="selectInput('input17', 'beli', 'btn_input17_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input17_olub" onclick="selectInput('input17', 'xeyr', 'btn_input17_olub')">Xeyr</button>
                </div>

                <h2>Question 18: Başgicəllənmə zamanı huşunuzu itirmisinizmi?</h2>
                <div id="input18_buttons">
                    <button type="button" class="button" id="btn_input18_olmuyub" onclick="selectInput('input18', 'beli', 'btn_input18_olmuyub')">Bəli</button>
                    <button type="button" class="button" id="btn_input18_olub" onclick="selectInput('input18', 'xeyr', 'btn_input18_olub')">Xeyr</button>
                </div>

                <h2>Question 19: Başgicəllənmənin ən şiddətli dövrü nə qədər baş verir?</h2>
                <div id="input19_buttons">
                    <button type="button" class="button" id="btn_input19_olmuyub" onclick="selectInput('input19', '0san-3deq', 'btn_input19_olmuyub')">0san-3deq</button>
                    <button type="button" class="button" id="btn_input19_olub" onclick="selectInput('input19', '23saat-4-5gun', 'btn_input19_olub')">23saat-4-5gun</button>
                    <button type="button" class="button" id="btn_input19_olubb" onclick="selectInput('input19', '10deq-23saat', 'btn_input19_olubb')">10deq-23saat</button>
                    <button type="button" class="button" id="btn_input19_olubbb" onclick="selectInput('input19', 'davamli', 'btn_input19_olubbb')">Davamli</button>
                </div>

                <h2>Question 20: Başgicəllənməniz nə şəkildə olur? (Başımın içinin fırlandığını hiss edirəm, ətraf dönmür və ya sadəcə ətraf dönürsə (Həqiqi)</h2>
                <div id="input20_buttons">
                    <button type="button" class="button" id="btn_input20_olmuyub" onclick="selectInput('input20', 'heqiqi', 'btn_input20_olmuyub')">Həqiqi baş ağrısı</button>
                    <button type="button" class="button" id="btn_input20_olub" onclick="selectInput('input20', 'yalanci', 'btn_input20_olub')">Yalançı baş ağrısı</button>
                </div>

                
                <input type="submit" class="button" value="Next">
            </form>
        </div>
        <script>
            function selectInput(inputId, value, buttonId) {
                document.getElementById(inputId).value = value;
                let buttons = document.querySelectorAll('#' + inputId + '_buttons .button');
                buttons.forEach(button => {
                    button.classList.remove('selected');
                });
                document.getElementById(buttonId).classList.add('selected');
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/page2', methods=['POST'])
def page2():
    session['input10'] = request.form.get('input10')
    session['input11'] = request.form.get('input11')
    session['input12'] = request.form.get('input12')
    session['input13'] = request.form.get('input13')
    session['input14'] = request.form.get('input14')
    session['input15'] = request.form.get('input15')
    session['input16'] = request.form.get('input16')
    session['input17'] = request.form.get('input17')
    session['input18'] = request.form.get('input18')
    session['input19'] = request.form.get('input19')
    session['input20'] = request.form.get('input20')

    # Collect all inputs
    inputs = [session.get(f'input{i}', '') for i in range(1, 21)]
    # Calculate scores
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

# Run the Flask application
def run_app():
    app.run(host='0.0.0.0', port=8003, debug=True, use_reloader=False)

if __name__ == "__main__":
    run_app()