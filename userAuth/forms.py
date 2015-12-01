from django import forms
from userAuth.models import User

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('name', 'email', 'password')

	
	def email(self):
		email = self.cleaned_data['email']
		return email
	def name(self):
		name=self.cleaned_data['name']
		return name