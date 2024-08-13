from django import forms

from django import forms

class PurchaseForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(max_length=100, label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Ваш email'}))
    phone = forms.CharField(max_length=15, label='Телефон', widget=forms.TextInput(attrs={'placeholder': 'Ваш телефон'}))

