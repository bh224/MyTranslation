from django.db.models import QuerySet
from comments.models import Comment

def get_comments_list(project_pk: int, page: int) -> QuerySet[Comment]:
    limit = 5
    start = (page-1) * limit
    end = start + limit
    return Comment.objects.order_by("-id").filter(project=project_pk)[start:end]