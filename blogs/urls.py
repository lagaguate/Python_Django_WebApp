

from django.urls import path
from servicios import views
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import CategoriaListado, CategoriaDetalle, CategoriaCrear, CategoriaActualizar, CategoriaEliminar
from blogs.views import PostListado, PostDetalle, PostCrear, PostActualizar, PostEliminar
from blogs.views import BlogListado
from blogs.views import PostCrudManager


post_crud = PostCrudManager()

#
# URLS de Categoria de Blogs
#

urlpatterns = [
    
    path('blog', BlogListado.as_view (template_name="blogs/blog.html"), name="blog"),
    
    ###
    # Categoria
    ###
    path('categoria', CategoriaListado.as_view(
        template_name="blogs/categoria/index.html"), name='categorialeer'),

    path('categoria/detalles/<int:pk>',
         CategoriaDetalle.as_view(template_name="blogs/categoria/detalles.html"), name='categoriadetalles'),

    path('categoria/crear',
         CategoriaCrear.as_view(template_name="blogs/categoria/crear.html"), name='categoriacrear'),

    path('categoria/editar/<int:pk>', CategoriaActualizar.as_view(
        template_name="blogs/categoria/actualizar.html"), name='categoriaeditar'),

    path('categoriaeliminar/<int:pk>',
         CategoriaEliminar.as_view(), name='categoriaeliminar'),
    # End Categoria

    ###
    # Post
    ###

    path('', PostListado.as_view(
        template_name="blogs/post/index.html"), name='postleer'),

    path('detalles/<int:pk>',
         PostDetalle.as_view(template_name="blogs/post/detalles.html"), name='postdetalles'),

    path('crear',
         PostCrear.as_view(template_name="blogs/post/crear.html"), name='postcrear'),

    path('editar/<int:pk>', PostActualizar.as_view(
        template_name="blogs/post/actualizar.html"), name='posteditar'),

    path('eliminar/<int:pk>',
         PostEliminar.as_view(), name='posteliminar'),
    # End Post
]

urlpatterns += post_crud.get_url_patterns()