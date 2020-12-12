from django.contrib import admin
from .models import Team, SubTeam, Member, Sprint


admin.site.register(Team)
admin.site.register(SubTeam)
admin.site.register(Member)
admin.site.register(Sprint)

