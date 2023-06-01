from django.db import models

from django.conf import settings

from utils.field_utils import RichTextField
from utils.model_utils import (BaseModel, BaseMeta, InlineModel, WithLevel, WithStartEndDate, WithAssignee, NULLABLE_FK,
                               WithStage, WithTags
                               )
from mproduct.models import Product, ProductModule, WithProduct, WithProductModule, ProductPlan


class Project(BaseModel, WithStartEndDate):
    VIEW_CONTROL_CHOICES = (('default', '默认'), ('private', '私有'), ('white_list', '白名单'))
    PROJECT_TYPE_CHOICES = (('short', '短期项目'), ('long', '长期项目'), ('ops', '运维项目'))
    PROJECT_STATUS_CHOICES = (('new', '未开始'), ('processing', '进行中'), ('hang_up', '已挂起'), ('done', '已完成'))

    key = models.CharField("项目代号", max_length=200, unique=True)
    type = models.CharField('项目类型', max_length=20, choices=PROJECT_TYPE_CHOICES, blank=True, null=True)
    work_days = models.PositiveIntegerField('可用工作日', blank=True, null=True)
    team_name = models.CharField('团队名称', max_length=200, blank=True, null=True)
    status = models.CharField('项目状态', max_length=20, choices=PROJECT_STATUS_CHOICES, default='new', blank=True,
                              null=True)
    related_products = models.ManyToManyField(Product, verbose_name='关联产品', blank=True,
                                              through='ProjectRelatedProduct')
    view_control = models.CharField('访问控制', choices=VIEW_CONTROL_CHOICES, max_length=20, default='default')
    project_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_manager",
        verbose_name="项目负责人", blank=True, null=True
    )

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
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name="项目成员",
        related_name="%(app_label)s_%(class)s_members",
        blank=True, through='ProjectMember')

    class Meta(BaseMeta):
        verbose_name = "项目"
        verbose_name_plural = "项目"


class WithProject(models.Model):
    project = models.ForeignKey(
        Project, verbose_name='所属项目', related_name="%(class)s_project", on_delete=models.PROTECT)

    class Meta:
        abstract = True


class ProjectRelatedProduct(WithProject, WithProduct):
    class Meta(BaseMeta):
        verbose_name = "关联产品"
        verbose_name_plural = "关联产品"

    def __str__(self):
        return ''


class ProjectMember(WithProject):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_user",
        verbose_name="用户"
    )
    role = models.CharField('角色', max_length=100, blank=True, null=True)
    work_days = models.FloatField('可用工日', default=66)
    work_hours_per_day = models.FloatField('可用工时/每天', default=7)

    class Meta(BaseMeta):
        verbose_name = "项目成员"
        verbose_name_plural = "项目成员"

    def __str__(self):
        return ''


class Requirement(BaseModel, WithProductModule, WithLevel, WithAssignee, WithStage, WithTags):
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
        verbose_name = "需求"
        verbose_name_plural = "需求"


class ProductRequirementAttachment(InlineModel):
    product_requirement = models.ForeignKey(Requirement, verbose_name='所属需求',
                                            related_name="%(app_label)s_%(class)s_product_requirement", **NULLABLE_FK)

    file = models.FileField('附件', upload_to='uploads/')

    class Meta(BaseMeta):
        verbose_name = "附件"
        verbose_name_plural = "附件"


class Task(BaseModel, WithProject, WithAssignee, WithLevel, WithStartEndDate):
    TASK_TYPE_CHOICES = (('dev', '开发任务'), ('test', '测试任务'))
    TASK_STATUS_CHOICES = (('new', '未开始'), ('processing', '进行中'), ('hang_up', '已挂起'), ('done', '已完成'))
    product_module = models.ForeignKey(
        ProductModule, verbose_name='所属模块', related_name="%(app_label)s_%(class)s_module", **NULLABLE_FK)
    type = models.CharField('任务类型', max_length=20, choices=TASK_TYPE_CHOICES, default='')
    status = models.CharField('项目状态', max_length=20, choices=TASK_STATUS_CHOICES, default='new', blank=True,
                              null=True)
    estimated_time = models.PositiveSmallIntegerField('预计耗时(h)', blank=True, null=True)
    cc_to = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_%(class)s_cc_to", verbose_name="抄送给", blank=True)

    class Meta(BaseMeta):
        verbose_name = "任务"
        verbose_name_plural = "任务"


class TaskAttachment(InlineModel):
    task = models.ForeignKey(Task, verbose_name='所属任务', related_name="%(app_label)s_%(class)s_task", **NULLABLE_FK)

    file = models.FileField('附件', upload_to='uploads/')

    class Meta(BaseMeta):
        verbose_name = "附件"
        verbose_name_plural = "附件"
