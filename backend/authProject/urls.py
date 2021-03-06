from django.contrib                         import admin
from django.urls                            import path
from authApp                                import views
from rest_framework_simplejwt.views         import (TokenObtainPairView, TokenRefreshView)
                                            #pareja token access- token refresh
                                            #crea token refresh a partir de un token access


#asociamos cada endpoint a la calse que debe llamar
urlpatterns = [
    path('admin/',          admin.site.urls),
    path('login/',          TokenObtainPairView.as_view()),     #al logearse devolvemos la pareja de tokens
    path('refresh/',        TokenRefreshView.as_view()),        #devolvemos un refresh token a partir del access token
    path('user/',           views.UserCreateView.as_view()),
    path('user/<int:pk>/',   views.UserDetailView.as_view()),
    path('transaction/',                                views.TransactionsCreateView.as_view()),
    path('transaction/<int:user>/<int:pk>/',            views.TransactionsDetailView.as_view()),
    path('transactions/<int:user>/<int:account>/',      views.TransactionsAccountView.as_view()),
    path('transaction/update/<int:user>/<int:pk>/',     views.TransactionsUpdateView.as_view()),
    path('transaction/remove/<int:user>/<int:pk>/',     views.TransactionsDeleteView.as_view()),
    path('deposit/create/',                             views.DepositCreateView.as_view()), # create a new deposit
    path('deposit/<int:user>/<int:pk>/',                views.DepositDetailView.as_view()), # view information for a deposit
    path('deposits/<int:user>/<int:account>/',          views.DepositsAccountView.as_view()) # view all depositss for an specific account
]
