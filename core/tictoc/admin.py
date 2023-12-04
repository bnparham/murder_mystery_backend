from django.contrib import admin
from .models import tictocModel

# Register your models here.
@admin.register(tictocModel)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'player', 'action', 'board', 'winner', 'terminal', 'time']
