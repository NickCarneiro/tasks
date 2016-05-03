from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'todos.views.index')
]
