from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Client, Budget, Invoice
from .forms import ClientForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/clients')
def clients():
    clients = Client.query.all()
    return render_template('clients.html', clients=clients)

@main.route('/clients/new', methods=['GET', 'POST'])
def new_client():
    form = ClientForm()
    if form.validate_on_submit():
        # Form validation passed
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        new_client = Client(name=name, email=email, phone=phone)
        db.session.add(new_client)
        db.session.commit()
        flash('New client added successfully!', 'success')
        return redirect(url_for('main.clients'))
    elif request.method == 'POST':
        # If POST but validation failed, flash an error message
        flash('Please fix the errors in the form.', 'danger')
    return render_template('new_client.html', form=form)
