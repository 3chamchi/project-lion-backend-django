from itertools import permutations
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from rest_framework import generics

from core.permissions import IsOwnerOnly

from .models import Post, Comment
from .serializers import PostBaseModelSerializer, PostListModelSerializer, PostRetrieveModelSerializer, \
    CommentListModelSerializer


# 게시글 목록 + 생성
class PostListCreateView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user.is_authenticated:
            serializer.save(writer=request.user)
        else:
            serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# 게시글 상세, 수정, 삭제
class PostRetrieveUpdateView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveModelSerializer


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'create':
            return PostBaseModelSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        permission_classes = list()
        action = self.action

        if action == 'list':
            permission_classes = [AllowAny]
        elif action in ['create', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOnly]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['get'])
    def get_comment_all(self, request, pk=None):
        post = self.get_object()
        comment_all = post.comment_set.all()
        serializer = CommentListModelSerializer(comment_all, many=True)
        return Response(serializer.data)


@api_view()
def calculator(request):
    # 1. 데이터 확인
    num1 = request.GET.get('num1', 0)
    num2 = request.GET.get('num2', 0)
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    data = {
        'type': 'FBV',
        'result': result,
    }

    # 3. 응답
    return Response(data)


class CalculatorAPIView(APIView):
    def get(self, request):
        # 1. 데이터 확인
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        operators = request.GET.get('operators')

        # 2. 계산
        if operators == '+':
            result = int(num1) + int(num2)
        elif operators == '-':
            result = int(num1) - int(num2)
        elif operators == '*':
            result = int(num1) * int(num2)
        elif operators == '/':
            result = int(num1) / int(num2)
        else:
            result = 0

        data = {
            'type': 'CBV',
            'result': result,
        }

        # 3. 응답
        return Response(data)

    def post(self, request):

        data = {
            'type': 'CBV',
            'method': 'POST',
            'result': 0,
        }

        # 3. 응답
        return Response(data)
