from django.db.models import QuerySet
from rest_framework.exceptions import NotFound
from glossaries.models import Glossary, Category

def get_a_category(category_pk) -> Category:
    try:
        category = Category.objects.get(pk=category_pk)
        return category
    except Category.DoesNotExist:
        raise NotFound(detail="Category is not fount", code=404)
    
def get_glossary_by_category(project_pk, category_pk) -> QuerySet[Glossary]:
    return Glossary.objects.order_by("created_at").filter(project=project_pk, category=category_pk)
