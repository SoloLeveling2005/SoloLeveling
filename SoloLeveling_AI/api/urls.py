
from django.urls import path, re_path
from api import views
from django.conf import settings
from django.conf.urls.static import static

# from django_api.views import GetCSRFToken

urlpatterns = [
    # todo authorization and registration
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^auth/$', views.auth, name='auth'),

    # todo work url
    re_path(r'^request_ai/$', views.request_ai, name='request_ai'),
    re_path(r'^search/$',
            views.search,
            name='search')

    # path(r'api1/', views.index1, name="index1"),
    # path('csrf_token/', GetCSRFToken.as_view())
    # path('posts/', views.index, name="posts"),
    # path('posts/<id:int>', views.index, name="posts"),
    # path('posts/<id:int>/comment', views.index, name="posts"),

    # re_path(r'^create/<title:str>/$', views.create_todo, name="create_todo"),
    # re_path(r'^posts/(?P<id>\d+)/$', views.posts_one, name="posts_one"),

]
