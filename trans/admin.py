from django.contrib import admin
from .models import Translation

# Register your models here.
@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    pass