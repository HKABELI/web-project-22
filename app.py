from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/nav')
def nav():
    return render_template('Header.html')

@app.route('/footer')
def footer():
    return render_template('Footer.html')


@app.route('/Home')
@app.route('/')
def Home():
    return render_template('Home.html')


@app.route('/About-me')
def aboutme():
    return render_template('aboutme.html')


@app.route('/Contact_Us')
def Contact_Us():
    return render_template('Contact_Us.html')


@app.route('/Contact_Us', methods=['GET', 'POST'])
def contact_uc_check_func():
    username = ''
    if request.method == 'POST':
        # check in DB of the website  user Exists
        # if yes
        username = request.form['username']

        return render_template('Contact_Us.html',
                               request_method=request.method,
                               username=username)


@app.route('/Asana')
def Asana():
    return render_template('Asana.html')


@app.route('/Exercises')
def Exercises():
    return render_template('Exercises.html')


@app.route('/Gallery')
def GalleryPage():
    return render_template('GalleryPage.html')


@app.route('/Login')
def Login_Page():
    return render_template('Login_Page.html')


@app.route('/Meditation')
def meditation():
    return render_template('meditation.html')


@app.route('/Pranayama')
def pranayama():
    return render_template('pranayama.html')


@app.route('/Registration')
def Registration():
    return render_template('Registration.html')


@app.route('/Yoga')
def Yoga():
    return render_template('Yoga.html')


if __name__ == '__main__':
    app.run(debug=True)
