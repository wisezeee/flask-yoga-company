import os

from flask import Flask, render_template, redirect, url_for, flash
from flask_babel import gettext, Babel
from app.database import db
from flask_login import current_user, login_user, login_required, logout_user
from flask import request
from werkzeug.security import check_password_hash, generate_password_hash

from app.forms.login_form import LoginForm
from app.forms.register import RegisterForm
from app.models.user import User
from dotenv import load_dotenv
from flask_login import LoginManager


load_dotenv()

templates_path = os.path.abspath("app/templates")
app = Flask(__name__, template_folder=templates_path)

app.debug = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
login_manager = LoginManager(app)

babel = Babel(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('CONNECTION_PATH')
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/feedback')
def feedback_page():
    return render_template('feedback.html')

@login_manager.user_loader
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        form = LoginForm()

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            flash('перепроверь входные данные пж')
            return render_template('login.html', form=form)

        login_user(user, remember=remember)
        return redirect(url_for('profile'))

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        form = RegisterForm()
        user = User.query.filter_by(email=email).first()

        if user:
            flash(gettext('такой юзер уже есть'))
            return render_template('register.html', form=form)

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run()
