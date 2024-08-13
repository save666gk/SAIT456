from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    phone = forms.CharField(label='Номер телефона', max_length=15)