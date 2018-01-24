from django.conf.urls import url, include
from home import views
from home.views import PlacesListView, PlaceDetailView

urlpatterns = [
    url(r'^index/', views.home, name='home'),
    url(r'^nosotros/', views.nosotros, name='nosotros'),
    url(r'^datos/$', PlacesListView.as_view(), name='datos'),
    url(r'^gracias/', views.gracias, name='gracias'),
    url(r'^contactenos/', views.contactenos, name='contactenos'),
    url(r'^datos/(?P<pk>\d+)$', PlaceDetailView.as_view(), name='detalle'),

    #url(r'^crear/$', PlaceCreate.as_view(), name='place-crear'),
    #url(r'^datos/(?P<pk>\d+)/actualizar/$', PlaceUpdate.as_view(), name='place-actualizar'),
    #url(r'^datos/(?P<pk>\d+)/actualizar/$', PlaceDelete.as_view(), name='author-delete'),

]
