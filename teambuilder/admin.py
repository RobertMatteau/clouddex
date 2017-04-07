from django.contrib import admin

# Register your models here.
from .models import User
from .models import Team
from .models import TeamMember
from .models import Pokemon
from .models import Item
from .models import Move
from .models import Comment

admin.site.register(User)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Pokemon)
admin.site.register(Item)
admin.site.register(Move)
admin.site.register(Comment)
