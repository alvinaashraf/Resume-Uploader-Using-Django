from django.contrib import admin
from django.urls import path
from resume import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_pic, name='home'),
    path('<int:pk>',views.candidate.as_view(),name="candidate")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)