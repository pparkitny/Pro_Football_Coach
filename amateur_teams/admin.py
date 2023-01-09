from django.contrib import admin

# Register your models here.
from .models import Coach, Team, Player, Stats, Pace, Shoting, Passing, Dribling, Defending, Physicality, Goalkeeping

admin.site.register(Coach)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Stats)
admin.site.register(Pace)
admin.site.register(Shoting)
admin.site.register(Passing)
admin.site.register(Dribling)
admin.site.register(Defending)
admin.site.register(Physicality)
admin.site.register(Goalkeeping)
