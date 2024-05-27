from django.contrib import admin
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('User.urls')),
    path('channel/', include('channel.urls')),
    path('chat/', include('chat.urls')),
    path('map/', include('map.urls')),
    path('emergencybtn/',include('EmergencyButton.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new
