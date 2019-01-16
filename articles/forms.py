from django import forms
from .models import Comment ,Articles,UserProfile

class ScanForm(forms.Form):
    target = forms.CharField(max_length=255,label='', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Entrer une adresse...'
    }))


class ArticlesForm(forms.ModelForm):
	class Meta:
		model = Articles
		fields = ('titre' , 'body' , 'image')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)

class UserForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ( 'email', 'telephone' ,'user')


# titre = forms.CharField()
#     body = forms.CharField(widget=forms.Textarea)
#     image = forms.FileField()
