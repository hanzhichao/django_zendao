from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views import static

urlpatterns = [
    # path('static/<path>', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # path('uploads/<path>',static.serve,{"document_root":settings.MEDIA_ROOT},name='media'),
    path('admin/', admin.site.urls),
    # path('ueditor/', include('DjangoUeditor.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

if settings.DEBUG:
    urlpatterns.append(
        path('uploads/<path>',static.serve, {"document_root": settings.MEDIA_ROOT}, name='media')
    )
