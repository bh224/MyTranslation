from django.contrib import admin
from .models import Category, Glossary

# Register your models here.
@admin.register(Glossary)
class GlossaryAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
# Register your models here.
