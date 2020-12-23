from django.db import models

from utils.model_utils import (BaseModel, BaseMeta, InlineModel, WithTags, WithParent, NULLABLE_FK)


class Attachment(InlineModel):
    # TYPE_DEFAULT = 'image'
    # TYPE_CHOICES = (('image', '图片'), ('csv', 'CSV'), ('doc', '文档'))
    file = models.FileField('附件', upload_to='uploads/')


class WithAttachments(models.Model):
    attachments = models.ManyToManyField(Attachment, verbose_name='附件',
                                         related_name="%(class)s_attachments", blank=True)

    class Meta:
        abstract = True


class DocLibrary(BaseModel):
    class Meta(BaseMeta):
        verbose_name = "文档库"
        verbose_name_plural = "1.文档库"


class DocCategory(InlineModel, WithParent):
    doc_library = models.ForeignKey(DocLibrary, verbose_name='文档库', related_name="%(class)s_category", on_delete=models.CASCADE)
    class Meta(BaseMeta):
        verbose_name = "分档分类"
        verbose_name_plural = "分档分类"


class Doc(BaseModel, WithTags, WithAttachments):  # description 为摘要
    doc_category = models.ForeignKey(DocCategory, verbose_name='所属分类', related_name="%(class)s_category", **NULLABLE_FK)
    html = models.TextField('HTML', null=True, blank=True)
    md = models.TextField('Markdown格式', null=True, blank=True)
    link = models.URLField('文档链接', null=True, blank=True)

    class Meta(BaseMeta):
        verbose_name = "文档"
        verbose_name_plural = "2.文档"