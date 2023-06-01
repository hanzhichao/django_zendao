from django.db import models

from utils.model_utils import (BaseModel, BaseMeta, InlineModel, WithLevel, WithTags, WithKey,
                               WithManager, WithWatchers, WithStatus,WithStage, WithImage, WithUrl, WithStartEndDate,
                               WithParent, WithAssignee, WithType, NULLABLE_FK
                               )
from django.conf import settings
from utils.field_utils import RichTextField


class Product(BaseModel):
    PRODUCT_TYPE_CHOICES = (('normal', '正常'), ('multi_branches', '多分支'), ('multi_platforms', '多平台'))
    VIEW_CONTROL_CHOICES = (('default', '默认'), ('private', '私有'), ('white_list', '白名单'))
    key = models.CharField("产品代号", max_length=200, unique=True)
    type = models.CharField('产品类型', max_length=20, choices=PRODUCT_TYPE_CHOICES, blank=True, null=True)
    product_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_product_manager",
        verbose_name="产品负责人", **NULLABLE_FK
    )
    test_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_test_manager",
        verbose_name="测试负责人", **NULLABLE_FK
    )
    release_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_release_manager",
        verbose_name="发布负责人", **NULLABLE_FK
    )

    view_control = models.CharField('访问控制', choices=VIEW_CONTROL_CHOICES, max_length=20, default='default')

    class Meta(BaseMeta):
        verbose_name = "产品"
        verbose_name_plural = "产品"


class WithProduct(models.Model):
    product = models.ForeignKey(
        Product, verbose_name='所属产品', related_name="%(app_label)s_%(class)s_product", on_delete=models.PROTECT)

    class Meta:
        abstract = True


class ProductBranch(InlineModel, WithProduct):
    class Meta(BaseMeta):
        verbose_name = "产品分支"
        verbose_name_plural = "产品分支"


class WithProductBranch(WithProduct):
    product_branch = models.ForeignKey(
        ProductBranch, verbose_name='所属分支', related_name="%(class)s_product_branch", **NULLABLE_FK)

    class Meta:
        abstract = True


class ProductModule(InlineModel, WithProductBranch, WithParent):
    class Meta(BaseMeta):
        verbose_name = "产品模块"
        verbose_name_plural = "产品模块"


class WithProductModule(WithProductBranch):
    product_module = models.ForeignKey(
        ProductModule, verbose_name='所属模块', related_name="%(app_label)s_%(class)s_module", **NULLABLE_FK)

    class Meta:
        abstract = True



class ProductVersion(BaseModel, WithProductBranch):
    builder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_builder",
        verbose_name="构建者", on_delete=models.PROTECT
    )
    build_date = models.DateField('打包日期', blank=True, null=True)
    code_repo = models.CharField('源代码地址', max_length=200, blank=True, null=True)
    download_url = models.CharField('下载地址', max_length=200, blank=True, null=True)

    class Meta(BaseMeta):
        verbose_name = "版本"
        verbose_name_plural = "版本"


class ProductRelease(InlineModel):
    RELEASE_STATUS_CHOICES = (('ok', '正常'), ('停止维护', '停止维护'))

    product_version = models.ForeignKey(ProductVersion, verbose_name='所属版本',
                                        related_name="%(app_label)s_%(class)s_product_version", **NULLABLE_FK)
    release_date = models.DateField('打包日期', blank=True, null=True)

    status = models.CharField('当前状态', max_length=20, choices=RELEASE_STATUS_CHOICES, default='ok')

    class Meta(BaseMeta):
        verbose_name = "产品发布"
        verbose_name_plural = "产品发布"


class ReleasePackage(InlineModel):
    product_version = models.ForeignKey(ProductVersion, verbose_name='所属版本', related_name="%(app_label)s_%(class)s_product_version", **NULLABLE_FK)
    product_release = models.ForeignKey(ProductRelease, verbose_name='所属发布', related_name="%(app_label)s_%(class)s_product_release", **NULLABLE_FK)

    file = models.FileField('发行包', upload_to='uploads/')

    class Meta(BaseMeta):
        verbose_name = "发行包"
        verbose_name_plural = "发行包"



class ProductPlan(InlineModel, WithProductBranch, WithStartEndDate):
    class Meta(BaseMeta):
        verbose_name = "发布计划"
        verbose_name_plural = "发布计划"

