from blogs.models import Categoria, Post
import django_filters

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['categorias', ]