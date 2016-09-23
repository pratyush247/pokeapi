from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
<<<<<<< HEAD

=======
>>>>>>> secondary
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poketext.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^incoming/message$', views.incoming_message),
=======
    url(r'^incoming/message$',views.incoming_message),
>>>>>>> secondary
)
