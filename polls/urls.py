
from . import views
from django.urls import path

app_name = 'polls'
urlpatterns = [
    # The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
    path('', views.index, name='index'),  # /polls
    path('<int:question_id>/', views.detail, name='detail'),  # /polls/5
    path('<int:question_id>/results', views.results,
         name='results'),  # /polls/5/results
    path('<int:question_id>/vote/', views.vote, name='vote')  # /polls/5/vote

]
