import os

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from utils.model_utils import WithUser

def attachment_upload(instance, filename):
    """Stores the attachment in a "per module/appname/primary key" folder"""
    return "attachments/{app}_{model}/{pk}/{filename}".format(
        app=instance.content_object._meta.app_label,
        model=instance.content_object._meta.object_name.lower(),
        pk=instance.content_object.pk,
        filename=filename,
    )


class Attachment(WithUser):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(db_index=True, max_length=64)
    content_object = GenericForeignKey("content_type", "object_id")
    attachment_file = models.FileField('附件', upload_to=attachment_upload)

    class Meta:
        verbose_name = '附件'
        verbose_name_plural = '附件'
        permissions = (
            ("delete_foreign_attachments", "可删除外链附件"),
        )

    def __str__(self):
        return ("{username} 添加 {filename}").format(
            username=self.creator.get_username(),
            filename=self.attachment_file.name,
        )

    @property
    def filename(self):
        return os.path.split(self.attachment_file.name)[1]


