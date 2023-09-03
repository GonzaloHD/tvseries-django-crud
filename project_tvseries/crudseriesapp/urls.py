from django.urls import path

from crudseriesapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view-series', views.view_series, name="view_series"),
    path('view-characters', views.view_characters, name="view_series"),
    path('new-series', views.new_series, name="new_series"),
    path('insert-series', views.insert_series, name="insert_series"),
    path('modify-series', views.modify_series, name="modify_series"),
    path('change-series', views.change_series, name="change_series"),
    path('delete-series', views.delete_series, name="delete_series"),
    path('new-character', views.newCharacter, name="change_series"),
    path('insert-character', views.insertCharacter, name="change_series"),
    path('modify-character', views.modify_character, name="modify_character"),
    path('change-character', views.change_character, name="change_character"),
    path('delete-character', views.delete_character, name="delete_character"),
    path('suggested-series', views.suggest_series, name="suggested-series")
]
