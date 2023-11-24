from django.contrib import admin
from .models import Candidates, Voters, Vote

# Register your models here.

admin.site.register(Candidates)
admin.site.register(Voters)
admin.site.register(Vote)
