

from django.urls import path
from blogs import views
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import CategoriaListado, CategoriaDetalle, CategoriaCrear, CategoriaActualizar, CategoriaEliminar
from blogs.views import PostListado, PostDetalle, AddPost, PostActualizar, PostEliminar 
from blogs.views import Blogsearch

#
# URLS de Categoria de Blogs
#

urlpatterns = [
    
    #path('', BlogListado.as_view (template_name="blogs/blog.html"), name="xxxblog"),
    path('', views.Blogsearch, name="sblog"), 
    
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

    path('post', PostListado.as_view(
        template_name="blogs/post/index.html"), name='postleer'),

    path('post/detalles/<int:pk>',
         PostDetalle.as_view(template_name="blogs/post/detalles.html"), name='postdetalles'),

    path('post/crear',
         AddPost.as_view(template_name="blogs/post/crear.html"), name='postcrear'),

    path('post/editar/<int:pk>', PostActualizar.as_view(
        template_name="blogs/post/actualizar.html"), name='posteditar'),

    path('post/eliminar/<int:pk>',
         PostEliminar.as_view(), name='posteliminar'),
    # End Post
]

