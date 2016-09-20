from django.conf.urls import url

from . import views

urlpatterns = [
    #/stories/
    url(r'^$', views.index, name='index'),

    #/stories/71/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail_book, name='detail_book'),

    url(r'^(?P<book_id>[0-9]+)/les/$', views.read_book, name='read_book'),

    #/stories/author/34/
    url(r'^author/(?P<author_id>[0-9]+)/$', views.detail_author, name='detail_author'),

    url(r'^author/mypage/$', views.my_page, name='my_page'),

    #/stories/author/34/favorite
    url(r'^author/(?P<author_id>[0-9]+)/favorite$', views.favorite_book_by_author, name='favorite_book_by_author'),

    url(r'^create_book/$', views.create_book, name='create_book'),

    url(r'^(?P<id>[0-9]+)/edit$', views.edit_book, name='edit_book'),

    url(r'^(?P<id>[0-9]+)/delete$', views.delete_book, name='delete_book'),
]