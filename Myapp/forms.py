from django import forms
from .models import Supporter, Contact, Blogpost

class SupporterForm(forms.ModelForm):
    class Meta:
        model = Supporter
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'is_financial_supporter', 'is_mentor', 'is_child_sponsor'
        ]
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'message']

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['tittle', 'content', 'author', 'blogimage']