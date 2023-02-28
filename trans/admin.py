from django.contrib import admin
from .models import Translation, CheckTranslation

# Register your models here.
@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    pass

@admin.register(CheckTranslation)
class CheckTranslationAdmin(admin.ModelAdmin):
    pass