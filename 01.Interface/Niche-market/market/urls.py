from django.urls import path
from market.views import StoreDV, StoreLV, StoreCreateView, StoreUpdateView, StoreDeleteView, store_download, store_comment
from market.views import MarketDV, MarketCreateView, MarketUpdateView, MarketDeleteView, market_download,MarketDetail
from mysite.views import HomeView
from market.models import Market, Location

app_name = 'market'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('<int:pk>/', MarketDV.as_view(), name='market'),
    path('market_detail/<int:pk>/', MarketDetail.as_view(), name='market_detail'),
    path('market_add/', MarketCreateView.as_view(), name="market_add"),
    path('<int:pk>/market_update/', MarketUpdateView.as_view(), name="market_update"),
    path('<int:pk>/market_delete/', MarketDeleteView.as_view(), name="market_delete"),
    path('market_download/<int:id>', market_download, name="market_download"),

    path('store/<int:pk>/', StoreLV.as_view(), name='store'),
    path('store/<int:fk>/<int:pk>/', StoreDV.as_view(), name='store_detail'),
    path('<int:fk>/store_add/', StoreCreateView.as_view(), name="store_add"),
    path('<int:pk>/store_update/', StoreUpdateView.as_view(), name="store_update"),
    path('<int:pk>/store_delete/', StoreDeleteView.as_view(), name="store_delete"),
    path('store_download/<int:id>', store_download, name="store_download"),
    path('comment/<int:fk>/<int:pk>', store_comment, name='store_comment'),

]
