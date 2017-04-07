from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from teambuilder.forms import  AddPokemon, AddTeam, SubmitComment, RegistrationForm
from teambuilder.models import User as Foo, Team, TeamMember, Pokemon, Comment, Move, Item
from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Login_required and LoginRequiredMixin check if user is logged before giving access to certain pages
# If not, redirect to login page

# Render landing page
def landing(request):	
	return render(request, 'teambuilder/general.html')
	
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/teambuilder/dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
	
# Render profile page
class ProfileView(ListView):
	# Define template for view
	template_name = 'teambuilder/profile.html'
	# Define name of object used in template
	context_object_name = 'foo'
		
	# Make database query
	def get_queryset(self):
		# Return queryset of users who's ID matches current user
		return User.objects.get(id=self.request.user.id)

# /teambuilder/addteam method
@login_required(login_url='/teambuilder/login/')	
def addteam(request):
	# Check if POST request
	if request.method == 'POST':
		
		# create a form instance for each team member to be added and populate it with data from the request
		# set prefix so JS scripts can target appropriate elements, otherwise each element ID for each form will be identical
		team = AddTeam(request.POST)
		p1 = AddPokemon(request.POST, prefix="P1")
		p2 = AddPokemon(request.POST, prefix="P2")
		p3 = AddPokemon(request.POST, prefix="P3")
		p4 = AddPokemon(request.POST, prefix="P4")
		p5 = AddPokemon(request.POST, prefix="P5")
		p6 = AddPokemon(request.POST, prefix="P6")
		
		# check whether all forms are valid
		if p1.is_valid() and p2.is_valid() and p3.is_valid() and p4.is_valid() and p5.is_valid() and p6.is_valid() and team.is_valid():
			# Save form data for team to newteam object
			newteam = team.save()
			# Get current users username
			newteam.owner = request.user.get_username()
			
			# Save form data for teammember to newp objects
			newp1 = p1.save(commit=False)
			# Get team ID
			newp1.teamid = newteam.id
			# Set position in team
			newp1.position = 1
			
			newp2 = p2.save(commit=False)
			newp2.teamid = newteam.id
			newp2.position = 2
			
			newp3 = p3.save(commit=False)
			newp3.teamid = newteam.id
			newp3.position = 3
			
			newp4 = p4.save(commit=False)
			newp4.teamid = newteam.id
			newp4.position = 4
			
			newp5 = p5.save(commit=False)
			newp5.teamid = newteam.id
			newp5.position = 5
			
			newp6 = p6.save(commit=False)
			newp6.teamid = newteam.id
			newp6.position = 6
			
			# Commit to database
			newteam.save()
			newp1.save()
			newp2.save()
			newp3.save()
			newp4.save()
			newp5.save()
			newp6.save()
			
			# Redirect to user dashboard
			return redirect('dashboard')
	# Else GET request
	else:
		# Create form objects for template
		team = AddTeam()
		p1 = AddPokemon(prefix="P1")
		p2 = AddPokemon(prefix="P2")
		p3 = AddPokemon(prefix="P3")
		p4 = AddPokemon(prefix="P4")
		p5 = AddPokemon(prefix="P5")
		p6 = AddPokemon(prefix="P6")
	
	# Render addteam page
	return render(request, 'teambuilder/addteam.html', {'team': team, 'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'p5': p5, 'p6': p6 })

# /teambuilder/editteam/?tid=tid method
@login_required(login_url='/teambuilder/login/')
def editteam(request):
	# Get team ID from URL
	tid = request.GET.get('tid', '')

	#Check if POST request
	if request.method == 'POST':
		# create a form instance for each team member to be added and populate it with data from the request
		team = AddTeam(request.POST, instance=Team.objects.get(id=tid))
		p1 = AddPokemon(request.POST, prefix="P1", instance=TeamMember.objects.get(teamid=tid, position=1))
		p2 = AddPokemon(request.POST, prefix="P2", instance=TeamMember.objects.get(teamid=tid, position=2))
		p3 = AddPokemon(request.POST, prefix="P3", instance=TeamMember.objects.get(teamid=tid, position=3))
		p4 = AddPokemon(request.POST, prefix="P4", instance=TeamMember.objects.get(teamid=tid, position=4))
		p5 = AddPokemon(request.POST, prefix="P5", instance=TeamMember.objects.get(teamid=tid, position=5))
		p6 = AddPokemon(request.POST, prefix="P6", instance=TeamMember.objects.get(teamid=tid, position=6))
		
		# Pulling data from database and creating valid forms, no form validation required
		# Save form changes for team to newteam object
		newteam = team.save()
		newteam.owner = request.user.get_username()
		
		# Save form changes for teammembers to newp objects
		newp1 = p1.save(commit=False)
		newp1.teamid = newteam.id
		newp1.position = 1
		
		newp2 = p2.save(commit=False)
		newp2.teamid = newteam.id
		newp2.position = 2
		
		newp3 = p3.save(commit=False)
		newp3.teamid = newteam.id
		newp3.position = 3
		
		newp4 = p4.save(commit=False)
		newp4.teamid = newteam.id
		newp4.position = 4
		
		newp5 = p5.save(commit=False)
		newp5.teamid = newteam.id
		newp5.position = 5
		
		newp6 = p6.save(commit=False)
		newp6.teamid = newteam.id
		newp6.position = 6
		
		# Commit changes to database
		newteam.save()
		newp1.save()
		newp2.save()
		newp3.save()
		newp4.save()
		newp5.save()
		newp6.save()
		
		# Redirect to user dashboard
		return redirect('/teambuilder/dashboard')
	else:
		# create a form instance for each team member to be added and populate it with data from the database
		team = AddTeam(instance=Team.objects.get(id=tid))
		p1 = AddPokemon(instance=TeamMember.objects.get(teamid=tid, position=1), prefix="P1")
		p2 = AddPokemon(instance=TeamMember.objects.get(teamid=tid, position=2), prefix="P2")
		p3 = AddPokemon(instance=TeamMember.objects.get(teamid=tid, position=3), prefix="P3")
		p4 = AddPokemon(instance=TeamMember.objects.get(teamid=tid, position=4), prefix="P4")
		p5 = AddPokemon(instance=TeamMember.objects.get(teamid=tid, position=5), prefix="P5")
		p6 = AddPokemon(instance=TeamMember.objects.get(teamid=tid, position=6), prefix="P6")
	
	# Get owner of team to be editted
	uid = Team.objects.values('owner').filter(id=tid)
	
	# Check if editor is owner
	if uid == request.user.username:
		# If owner, render website
		return render(request, 'teambuilder/editteam.html', {'team': team, 'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'p5': p5, 'p6': p6 })
	else:
		# Else, admonish him!
		return HttpResponse('That\'s not yours!')
		
# /teambuilder
class TeamListView(LoginRequiredMixin, ListView):
	# Define redirect for when user is not logged in
	login_url = '/teambuilder/login/'
	redirect_field_name = 'redirect_to'

	# Define template for view
	template_name = 'teambuilder/dashboard.html'
	# Define name of object to be used in template
	context_object_name = 'team_list'
	
	# Make database query
	def get_queryset(self):
		# Return query set of teams ordered by ID
		return Team.objects.order_by('id')
		
	# Get additional context data
	def get_context_data(self, **kwargs):
		# Create context object
		context = super(ListView, self).get_context_data(**kwargs)
		# Make database query for teammembers ordered by teamid and position
		# Add queryset to context object
		context['teammember_list'] = TeamMember.objects.order_by('teamid', 'position')
		return context

# /teambuilder/community
class CommunityListView(LoginRequiredMixin, ListView):
	# Define redirect for when user is not logged in
	login_url = '/teambuilder/login/'
	redirect_field_name = 'redirect_to'

	# Define template for view
	template_name = 'teambuilder/community.html'
	# Define name of object to be used in template
	context_object_name = 'team_list'
	
	# Make database query
	def get_queryset(self):
		# Return query set of teams ordered by ID
		return Team.objects.order_by('teamname')
		
	# Get additional context data
	def get_context_data(self, **kwargs):
		# Create context object
		context = super(ListView, self).get_context_data(**kwargs)
		# Make database query for teammembers ordered by teamid and position
		# Add queryset to context object
		context['teammember_list'] = TeamMember.objects.order_by('teamid', 'position')
		return context
	
# /teambuilder/community/tid	
class CommunityTeamListView(LoginRequiredMixin, ListView):
	# Define redirect for when user is not logged in
	login_url = '/teambuilder/login/'
	redirect_field_name = 'redirect_to'

	# Define template for view
	template_name = 'teambuilder/communityTeam.html'
	# Define name of object to be used in template
	context_object_name = 'team'
	
	# Make database query
	def get_queryset(self, **kwargs):
		# get team id from slug
		tid = self.kwargs['slug']
		# Return query set of team with matching team id
		return Team.objects.get(id=tid)
		
	# Get additional context data
	def get_context_data(self, **kwargs):
		# get team id from slug
		tid = self.kwargs['slug']
		# Create context object
		context = super(ListView, self).get_context_data(**kwargs)
		# Make database queries for...
		# All teammembers, ordered by position
		context['teammember_list'] = TeamMember.objects.all().order_by('position')
		# Comments with team ID tid
		context['comment_list'] = Comment.objects.filter(teamid=tid)
		# Average value of rating from all comments with team ID tid
		context['rating'] = Comment.objects.filter(teamid=tid).aggregate(Avg('rating')).values()
		# Count of pokemon with same name as each teammember
		context['analytics1'] = TeamMember.objects.filter(pname = TeamMember.objects.filter(teamid=tid, position=1).values('pname')).count()
		context['analytics2'] = TeamMember.objects.filter(pname = TeamMember.objects.filter(teamid=tid, position=2).values('pname')).count()
		context['analytics3'] = TeamMember.objects.filter(pname = TeamMember.objects.filter(teamid=tid, position=3).values('pname')).count()
		context['analytics4'] = TeamMember.objects.filter(pname = TeamMember.objects.filter(teamid=tid, position=4).values('pname')).count()
		context['analytics5'] = TeamMember.objects.filter(pname = TeamMember.objects.filter(teamid=tid, position=5).values('pname')).count()
		context['analytics6'] = TeamMember.objects.filter(pname = TeamMember.objects.filter(teamid=tid, position=6).values('pname')).count()
		# Count of all teammembers
		context['total'] = TeamMember.objects.all().count()
		return context
		
# /teambuilder/comment
@login_required(login_url='/teambuilder/login/')
def comment(request, slug):
	# Check if POST request
	if request.method == 'POST':
	# Create a form instance for comment to be added and populate it with data from the request
		c = SubmitComment(request.POST)
		
		# Check if form is valid
		if c.is_valid():
			# Save form data to newcomment object
			newcomment = c.save(commit=False)
			# Set comment teamid to slug value
			newcomment.teamid = slug
			# Set comment username to current user
			newcomment.username = request.user.username
			# Commit to database
			newcomment.save()
			
			# Redirect to community team page
			return redirect('/teambuilder/team/' + slug)
	
	else:
		# Create a form instance to be populated
		c = SubmitComment()
	
	# Render comment page with form c
	return render(request, 'teambuilder/comment.html', {'c': c})
	
# /teambuilder/typechart
@login_required(login_url='/teambuilder/login/')
def typechart(request):
	# Render type chart page
	return render(request, 'teambuilder/pokemontypechart.html')

# /teambuilder/pokemonlist
class PokemonListView(LoginRequiredMixin, ListView):
	# Define redirect for when user is not logged in
	login_url = '/teambuilder/login/'
	redirect_field_name = 'redirect_to'

	# Define template for view
	template_name = 'teambuilder/pokemonlist.html'
	# Define name of object to be used in view
	context_object_name = 'pokemon'
	
	# Make database query
	def get_queryset(self):
		# Return all pokemon
		return Pokemon.objects.all()
	
# /teambuilder/moveslist
class MovesListView(LoginRequiredMixin, ListView):
	# Define redirect for when user is not logged in
	login_url = '/teambuilder/login/'
	redirect_field_name = 'redirect_to'

	# Define template for view
	template_name = 'teambuilder/pokemonmovelist.html'
	# Define name of object to be used in view
	context_object_name = 'moves'
	
	# Make database query
	def get_queryset(self):
		# Return all moves
		return Move.objects.all()
	
# /teambuilder/itemlist
class ItemsListView(LoginRequiredMixin, ListView):
	# Define redirect for when user is not logged in
	login_url = '/teambuilder/login/'
	redirect_field_name = 'redirect_to'

	# Define template for view
	template_name = 'teambuilder/pokemonitemlist.html'
	# Define name of object to be used in view
	context_object_name = 'items'
	
	# Make database query
	def get_queryset(self):
		# Return all items
		return Item.objects.all()

# /teambuilder/delete/tid
@login_required(login_url='/teambuilder/login/')
def delete(request):
	# Get team id from URL
	tid = request.GET.get('tid', '')
	# Get owner of team
	uid = Team.objects.values('owner').filter(id=tid)
	
	# Check if deleting user is owner
	if uid == request.user.username:
		# Get team
		team = Team.objects.get(id=tid)
		# Get teammembers
		p1 = TeamMember.objects.get(teamid=tid, position=1)
		p2 = TeamMember.objects.get(teamid=tid, position=2)
		p3 = TeamMember.objects.get(teamid=tid, position=3)
		p4 = TeamMember.objects.get(teamid=tid, position=4)
		p5 = TeamMember.objects.get(teamid=tid, position=5)
		p6 = TeamMember.objects.get(teamid=tid, position=6)
		# Delete team and teammembers
		team.delete()
		p1.delete()
		p2.delete()
		p3.delete()
		p4.delete()
		p5.delete()
		p6.delete()
		# Return to dashboard
		return redirect('/teambuilder/dashboard')
	
	else:
		# Else, admonish them!
		return HttpResponse('That\'s not yours!')