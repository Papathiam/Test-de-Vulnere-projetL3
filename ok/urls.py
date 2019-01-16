from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    # url(r'^$', auth_views.login, {'template_name': 'pentestapp/login.html'}, name='login'),
    url(r"^$", views.index, name="home"),
    # url(r"^pentestSys/$", views.pentestSys, name="pentestSys"),
    # url(r"^pentestWeb/$", views.pentestWeb, name="pentestWeb"),
    # url(r"^pentestSys/collecte/$", views.collecte, name="collecte"),
    url(r"^scanPorts/$", views.scan, name="scan"),
#     url(r"^pentestSys/collecte/scanRéseau/$", views.scanReseau, name="scanReseau"),
#     url(r"^pentestSys/analyse/$", views.analyse, name="analyse"),
#     url(r"^pentestSys/exploit/$", views.exploit, name="exploit"),
#     url(r"^pentestWeb/Scanweb/$", views.collecteweb, name="collecteweb"),
#     #url(r"^pentestWeb/Scanweb1/$", views.scanWeb, name="scanweb"),
#     url(r"^pentestWeb/exploitweb/$", views.exploitweb, name="exploitweb"),

]

