from django.db import models

from utils.model_utils import (BaseModel, BaseMeta, InlineModel, WithTags, WithParent, NULLABLE_FK)
from DjangoUeditor.models import UEditorField
from mproduct.models import Product
from mproject.models import Project


class DocLibrary(BaseModel):
    class Meta(BaseMeta):
        verbose_name = "文档库"
        verbose_name_plural = "文档库"


class DocCategory(InlineModel, WithParent):
    doc_library = models.ForeignKey(DocLibrary, verbose_name='文档库', related_name="%(app_label)s_%(class)s_doc_library",
                                    on_delete=models.CASCADE)

    class Meta(BaseMeta):
        verbose_name = "分档分类"
        verbose_name_plural = "分档分类"


class Doc(BaseModel, WithTags):
    DOC_TYPE_CHOICES = (('file', '文件'), ('link', '链接'), ('page', '网页'))

    project = models.ForeignKey(
        Project, verbose_name='所属项目', related_name="%(app_label)s_%(class)s_project", **NULLABLE_FK)
    product = models.ForeignKey(
        Product, verbose_name='所属产品', related_name="%(app_label)s_%(class)s_product", **NULLABLE_FK)
    type = models.CharField('项目类型', max_length=20, choices=DOC_TYPE_CHOICES, default='page')
    doc_library = models.ForeignKey(DocLibrary, verbose_name='所属文档库',
                                    related_name="%(app_label)s_%(class)s_doc_library", on_delete=models.PROTECT)
    doc_category = models.ForeignKey(DocCategory, verbose_name='所属分类',
                                     related_name="%(app_label)s_%(class)s_doc_category", **NULLABLE_FK)
    content = UEditorField('文档正文', null=True, blank=True)
    link = models.URLField('文档链接', null=True, blank=True)

    class Meta(BaseMeta):
        verbose_name = "文档"
        verbose_name_plural = "文档"


class DocAttachment(InlineModel):
    file = models.FileField('附件', upload_to='uploads/')
