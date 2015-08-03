from django.conf.urls import include, url, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^accounts/logout/$',	'django.contrib.auth.views.logout',	{'next_page':	'/'}),
	url(r'', include('blog.urls'))
)
