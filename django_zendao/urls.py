import notifications.urls
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views import static

urlpatterns = [
    # path('static/<path>', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # path('uploads/<path>',static.serve,{"document_root":settings.MEDIA_ROOT},name='media'),
    # path('admin/', include('loginas.urls')),
    path('admin/', admin.site.urls),
    # path('ueditor/', include('DjangoUeditor.urls')),
    # path('ckeditor/', include('ckeditor_uploader.urls'))
    path('tinymce/', include('tinymce.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('comments/', include('django_comments.urls')),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    # path('attachments/',  include('attachments.urls', namespace='attachments')),
]

if settings.DEBUG:
    urlpatterns.append(
        path('uploads/<path>', static.serve, {"document_root": settings.MEDIA_ROOT}, name='media'),
    )

    urlpatterns.append(
        re_path(r'^media(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT})
    )
