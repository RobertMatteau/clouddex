'''
Django forms for teambuilder app
'''
from django import forms
from teambuilder.models import User as Foo, Team, TeamMember, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
	
# Form used to register new user
class RegistrationForm(UserCreationForm):
	email = forms.CharField(max_length=200)
	first_name = forms.CharField(max_length = 50, required=False)
	last_name = forms.CharField(max_length = 50, required=False)
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
	
# Form used on addteam page to enter team information
class AddTeam(forms.ModelForm):
	teamname = forms.CharField(label="Username", max_length=200)
	comment = forms.CharField(label="Comment", max_length=600, widget=forms.Textarea)
	
	class Meta:
		fields = ('teamname', 'comment',)
		model = Team
		
# Form used on addteam page to enter team member information
class AddPokemon(forms.ModelForm):
	pname = forms.CharField(label="Pokemon", max_length=50)
	pability = forms.CharField(label="Ability", max_length=50)
	pitem = forms.CharField(label="Item", max_length=50)
	movea = forms.CharField(label="Move A", max_length=50)
	moveb = forms.CharField(label="Move B", max_length=50)
	movec = forms.CharField(label="Move C", max_length=50)
	moved = forms.CharField(label="Move D", max_length=50)
	
	class Meta:
		fields = ('pname', 'pability', 'pitem', 'movea', 'moveb', 'movec', 'moved',)
		model = TeamMember

# Form used to submit comments on community team pages		
class SubmitComment(forms.ModelForm):
	message = forms.CharField(label="Comment", max_length=600)
	rating = forms.IntegerField(label="rating")
	
	class Meta:
		fields = ('message', 'rating',)
		model = Comment