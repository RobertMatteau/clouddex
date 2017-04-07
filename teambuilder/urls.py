'''
Django URL patterns for teambuilder app
'''
from django.conf.urls import url

# Import view functions
from . import views
from django.contrib.auth import views as auth_views
# Import ListView classes for Dashboard, Profle, Community, Community Team, Pokemon List, Move List, Item List
from teambuilder.views import TeamListView, ProfileView, CommunityListView, CommunityTeamListView, PokemonListView, MovesListView, ItemsListView

urlpatterns = [
	# Landing page /teambuilder
	url(r'^$', views.landing, name='landing'),
	# User Login
	url(r'^login/$', auth_views.login, { 'template_name': 'teambuilder/login.html' }, name='login'),
	# User Logout
	url(r'^logout/$', auth_views.logout, {'next_page': '/teambuilder'}, name='logout'),
	# User Registration
	url(r'^register/$', views.register, name='register'),
	# User Dashboard /teambuilder/dashboard
	url(r'^dashboard/$', TeamListView.as_view(), name='dashboard'),
	# Add Team /teambuilder/addteam
	url(r'^addteam/$', views.addteam, name='addteam'),
	# Edit Team /teambuilder/edit/?tid=tid
	url(r'^editteam/$', views.editteam, name='editteam'),
	# Profile /teambuilder/profile
	url(r'^profile/$', ProfileView.as_view(), name='profile'),
	# Community /teambuilder/community	
	url(r'^community/$', CommunityListView.as_view(), name='community'),
	# Community Team /teambuilder/team/slug
	url(r'^team/(?P<slug>[a-zA-Z0-9-]+)$', CommunityTeamListView.as_view(), name='team'),
	# Comment /teambuilder/team/comment/slug
	url(r'^team/comment/(?P<slug>[a-zA-Z0-9-]+)$', views.comment, name='comment'),
	# Type chart /teambuilder/typechart
	url(r'^typechart/$', views.typechart, name='typechart'),
	# Pokemon List /teambuilder/pokemon
	url(r'^pokemon/$', PokemonListView.as_view(), name='pokemon'),
	# Move List /teambuilder/moves
	url(r'^moves/$', MovesListView.as_view(), name='moves'),
	# Items List /teambuilder/items
	url(r'^items/$', ItemsListView.as_view(), name='items'),
	# Delete a team and it's members
	url(r'^delete/$', views.delete, name='delete-team'),
]