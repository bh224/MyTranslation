from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from projects.models import Project
from comments.models import Comment
from comments.serializers import CommentSerializer
from comments.services.comment_service import get_comments_list
from users.models import User


class Comments(APIView):
    """ 프로젝트 코멘트 조회/생성 """
    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        commnets = get_comments_list(pk, page)
        serializer = CommentSerializer(commnets, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        # todo 예외처리
        project = Project.objects.get(pk=pk)
        writer = request.user
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(writer=writer, project=project)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class CommentDetail(APIView):
    """ 코멘트 수정/삭제 """
    def put(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            edited_comment = serializer.save()
            serializer = CommentSerializer(edited_comment)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        delete_cnt, _ = comment.delete()
        if delete_cnt:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ParseError({"detail": "failed"})
        
