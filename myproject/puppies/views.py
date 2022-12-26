from flask import Blueprint,render_template,redirect,url_for
from ..db import db
from myproject.puppies.forms import AddForm,DelForm
from myproject.models import Puppy

pupy_blp= Blueprint('puppies',
                              __name__,)
                              

@pupy_blp.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Puppy to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('/puppies/add.html',form=form)

@pupy_blp.route('/list')
def list():
    # Grab a list of puppies from database.
    puppies =Puppy.query.all()
    return render_template('/puppies/list.html', puppies=puppies)

@pupy_blp.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    return render_template('puppies/delete.html',form=form)