from glob import escape
from rest_framework.exceptions import NotFound
from glossaries.models import Glossary, Category

def get_a_category(category_pk):
    try:
        category = Category.objects.get(pk=category_pk)
        return category
    except Category.DoesNotExist:
        raise NotFound(detail="Category is not fount", code=404)