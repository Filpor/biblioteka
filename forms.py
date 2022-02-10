from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title=StringField('Tytuł', validators=[DataRequired()])
    autor=StringField("Autor", validators=[DataRequired()])
    pages=IntegerField('Ilość Stron', validators=[DataRequired()])
    description=TextAreaField('Opis', validators=[DataRequired()])
    type=SelectField('Gatunek',choices=[('fantasy','fantasy'),('kryminał,sensacja','kryminał,sensacja'), 
    ('historyczna','historyczna'), ('literatura_piekna','literatura piękna'), ("przygodowa",'przygodowa')], validators=[DataRequired()])
    read=BooleanField("Przeczytana?", false_values=None)
     
