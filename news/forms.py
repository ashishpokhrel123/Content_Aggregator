from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm




class CustomUserCreationForm(forms.Form):
    first_name = forms.CharField(label='Enter First name', max_length=150)
    last_name = forms.CharField(label='Enter Last name', max_length=150)
    username = forms.CharField(label='Enter Username', max_length=150)
    email = forms.EmailField(label='Enter Email')
    password1 = forms.CharField(label='Create Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    def save(self, commit=True):
        user = User.objects.create_user(
            #cleaned_data will check the duplicate value
            
           
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            #self.cleaned_data['first_name'],
            #self.cleaned_data['last_name'],
            
        )
        return user

class CustomUserForm(forms.Form):

    username = forms.CharField(label='Enter Username', max_length=150)
    password1 = forms.CharField(label='Create Password', widget=forms.PasswordInput)



    def save(self, commit=True):
        user1 = User.objects.create_user(
            #cleaned_data will check the duplicate value
            
           
            self.cleaned_data['username'],
            self.cleaned_data['password1'],
            #self.cleaned_data['first_name'],
            #self.cleaned_data['last_name'],
            
        )
        return user1




    




    

