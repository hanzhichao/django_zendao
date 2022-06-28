from django.db import models

from utils.model_utils import (BaseModel, BaseMeta, InlineModel, WithLevel, WithTags, WithKey,
                               WithManager, WithWatchers, WithStatus,WithStage, WithImage, WithUrl, WithStartEndDate,
                               WithParent, WithAssignee, WithType, NULLABLE_FK
                               )
from django.conf import settings
from ckeditor.fields import RichTextField


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


class ProductPlan(InlineModel, WithProductBranch, WithStartEndDate):
    class Meta(BaseMeta):
        verbose_name = "产品计划"
        verbose_name_plural = "产品计划"


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
        verbose_name = "产品版本"
        verbose_name_plural = "产品版本"


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


class ProductRequirement(BaseModel, WithProductModule, WithLevel, WithAssignee, WithStage, WithTags):
    SOURCE_CHOICES = (('customer', '客户'),
                      ('user', '用户'),
                      ('pm', '产品经理'),
                      ('market', '市场'),
                      ('customer_service', '客服'),
                      ('developer', '开发人员'),
                      ('tester', '测试人员'),
                      ('else', '其他'),
                      )

    STATUS_CHOICES = (('active', '激活'), ('closed', '关闭'))
    STAGE_CHOICES = (('new', '未开始'),
                     ('in_plan', '已计划'),
                     ('in_project', '已立项'),
                     ('developing', '研发中'),
                     ('develop_complete', '研发完毕'),
                     ('testing', '测试中'),
                     ('test_complete', '测试完毕'),
                     ('accepted', '已验收'),
                     ('online', '已发布'),
                     )

    product_plan = models.ForeignKey(
        ProductPlan, verbose_name='所属计划', related_name="%(app_label)s_%(class)s_plan", **NULLABLE_FK)
    source = models.CharField('需求来源', max_length=20, choices=SOURCE_CHOICES, blank=True, null=True)
    status = models.CharField('状态', max_length=20, choices=STATUS_CHOICES, default='active')
    stage = models.CharField('所处阶段', max_length=20, choices=STAGE_CHOICES, default='new')
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_reviewer",
        verbose_name="由谁评审", **NULLABLE_FK
    )
    no_need_review = models.BooleanField('不需要评审', default=True)
    estimated_time = models.PositiveSmallIntegerField('预计耗时(h)', blank=True, null=True)
    acceptance_criteria = RichTextField('验收标准', blank=True, null=True)
    cc_to = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_%(class)s_cc_to", verbose_name="抄送给", blank=True)

    class Meta(BaseMeta):
        verbose_name = "产品需求"
        verbose_name_plural = "产品需求"


class ProductRequirementAttachment(InlineModel):
    product_requirement = models.ForeignKey(ProductRequirement, verbose_name='所属需求', related_name="%(app_label)s_%(class)s_product_requirement", **NULLABLE_FK)

    file = models.FileField('附件', upload_to='uploads/')

    class Meta(BaseMeta):
        verbose_name = "附件"
        verbose_name_plural = "附件"
