from config import settings
from celery import shared_task
from django.core.mail.message import EmailMessage
from projects.models import Project, Project_Member


@shared_task
def send_email(pk):
    from_email = settings.EMAIL_HOST_USER
    project = Project.objects.get(pk=pk)
    to_email = Project_Member.objects.get(project_id=pk, role="author").member.email
    subject = f"[{project.title}] 검수 완료 알림 by dev"
    to = [to_email]
    message = f"[{project.title}]의 체크가 완료되었습니다. 2차 수정 후 최종납품 해 주세요."
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
    return True