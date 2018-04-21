from flask import render_template,request
from wtforms import Form, TextField, TextAreaField, validators, StringField, \
SubmitField, SelectField
from flask_wtf import FlaskForm
from app import app

app.config['SECRET_KEY'] = 'you-will-never-guess'

class ReusableForm(FlaskForm):
      environment = \
      SelectField('environment',choices=[('Production','Production'),('UAT','UAT'),('Test','Test'),('Demo','Demo')])
      instrument  = TextField('', validators=[validators.required()], default="USD")
      instance    = SelectField('instance',choices=[('1','1'),('2','2')])
      lookuptype  = SelectField('type',choices=[('Cache','Cache'),('Storage','Storage')])
      scale       = SelectField('scale',choices=[('1h','1h')])
      points      = SelectField('points',choices=[('8','8'),('16','16'),('24','24')])
      output      = TextAreaField('')

@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def index():
    user = {'username': 'Miguel'}
    form = ReusableForm(request.form)

    if request.method == 'POST':
        print request.form
        form.output.data = "Running %s %s" % (form.instance.data,form.instrument.data)
        return render_template('index.html', title='Home', user=user,
            form=form)

    print "GET REQUEST"
    return render_template('index.html', title='Home', user=user,
        form=form)
