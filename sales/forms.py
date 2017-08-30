from django import forms

class ContactUsForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=25)
    email = forms.EmailField(help_text='A valid email address, please.')
    message = forms.CharField(max_length=100, help_text='100 characters max.')
