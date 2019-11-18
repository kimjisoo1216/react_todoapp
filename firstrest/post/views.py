from rest_framework import viewsets
from post.models import Post
from post.serializer import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Create your views here.
