from flask import render_template, request, url_for, redirect, flash, abort
from flask_login import login_required, current_user, login_user, logout_user
from form import RegisterForm, LoginForm, ExpenseForm
from app import app
from model import User, Expense, db
from sqlalchemy import func

"""
Routes it will have
/                  — homepage, redirect to /expenses if logged in
/register          — registration page
/login             — login page
/logout            — logout, redirect to /login

/expenses          — list all expenses + total + filter
/expenses/add      — add expense form
/expenses/<id>/delete  — delete expense (POST only)

"""


# Homepage
@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for("expenses"))
    return redirect(url_for("login"))
    # return render_template('base.html')
    # return 'This is a homepage'


# register route page
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("expenses"))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            # name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            # password=form.password.data,
            # confirm_password=form.confirm_password.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        print("Form Response:", form.data)
        flash('Account created successfully.', 'success')
        return redirect(url_for('expenses'))
    return render_template('auth/register.html', form=form)


# login route page
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("expenses"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            print("Form Response:", form.data)
            return redirect(url_for('expenses'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('auth/login.html', form=form)


# logout route page
@app.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for("login"))


# expense lists route page
@app.route("/expenses")
@login_required
def expenses():
    expenses = Expense.query.filter_by(author_id=current_user.id).all()
    total = db.session.query(func.sum(Expense.amount)).filter_by(author_id=current_user.id).scalar() or 0
    return render_template("expenses/list.html", expenses=expenses, total=total)


# add expense route page
@app.route("/expense/add", methods=['GET', 'POST'])
@login_required
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(
            description=form.description.data,
            amount=form.amount.data,
            author_id=current_user.id,
            date=form.date.data,
            category=form.category.data
        )
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully.', 'success')
        return redirect(url_for('expenses'))
    return render_template("expenses/add.html", form=form)


# update expense route page
@app.route("/expense/update/<int:id>", methods=['GET', 'POST'])
@login_required
def update_expense(id):
    expense = Expense.query.get_or_404(id)
    if expense.author_id != current_user.id:
        abort(403)
    form = ExpenseForm(obj=expense)
    if form.validate_on_submit():
        expense.description = form.description.data
        expense.amount = form.amount.data
        expense.date = form.date.data
        expense.category = form.category.data
        db.session.commit()
        flash('Expense updated successfully.', 'success')
        return redirect(url_for('expenses'))
    return render_template("expenses/update.html", form=form)


# delete expense route page
@app.route("/expense/delete/<int:id>", methods=['POST'])
@login_required
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    if expense.author_id != current_user.id:
        abort(403)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully.', 'success')
    return redirect(url_for('expenses'))
