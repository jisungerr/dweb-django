from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),

    path('login/', views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('cadastro/', views.AccountCreate.as_view(), name='cadastrar'),
    path('users/<int:pk>/editar', views.AccountEdit.as_view(), name='editar'),
    path('users/<int:pk>/delete/', views.AccountDelete.as_view(), name='deletar'),


    path('games/cadastrojogo/', views.CreateJogo.as_view(), name='cadastro-jogo'),
    path('games/<int:pk>/', views.ViewJogos.as_view(), name='detalhe-jogo'),
    path('games/<int:pk>/delete/', views.DeletarJogo.as_view(), name='deletar-jogo'),
    path('games/<int:pk>/edit/', views.EditarJogo.as_view(), name='editar-jogo'),
]
