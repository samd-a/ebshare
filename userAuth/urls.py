from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.renderSignin, name='signin'),
    url(r'^register$', views.renderSignup, name='signup'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),
]