from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import datetime
from django.utils.encoding import force_str as force_text
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager

from .field_utils import RichTextField

NULLABLE_FK = dict(blank=True, null=True, on_delete=models.SET_NULL)
NULLABLE = dict(blank=True, null=True)

class _BaseModel(models.Model):

    class Meta:
        abstract = True

    def has_field(self, field)->bool:
        try:
            self._meta.get_field(field)
            return True
        except FieldDoesNotExist:
            return False

class BaseMeta:
    ordering = ['id']


class AbstractMeta:
    abstract = True


class WithName(_BaseModel):
    name = models.CharField("名称", max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class WithUniqueName(WithName):
    name = models.CharField("名称", max_length=200, unique=True)

    class Meta:
        abstract = True


class WithDesc(_BaseModel):
    # description = models.TextField('描述', null=True, blank=True)
    description = RichTextField(default='', verbose_name='描述', null=True, blank=True)

    # description = RichTextField(default='', verbose_name='描述', null=True, blank=True,
    #                            width=800, height=150,
    #                            toolbars="mini"
    #                            )

    class Meta:
        abstract = True


class WithShortDesc(_BaseModel):
    description = models.CharField('描述', max_length=200, null=True, blank=True)

    class Meta:
        abstract = True


class WithKey(_BaseModel):
    key = models.CharField("Key", max_length=200, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.key


class WithValue(_BaseModel):
    value = models.CharField("Value", max_length=500)

    class Meta:
        abstract = True


class WithCreator(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_creator",
        verbose_name="创建人")

    class Meta:
        abstract = True


class WithLevel(_BaseModel):
    LEVEL_DEFAULT = 2
    LEVEL_CHOICES = ((0, 'P0'), (1, 'P1'), (2, 'P2'), (3, 'P3'), (4, 'P4'), (5, 'P5'))
    level = models.PositiveSmallIntegerField('优先级', choices=LEVEL_CHOICES, default=LEVEL_DEFAULT)

    class Meta:
        abstract = True


class WithType(_BaseModel):
    TYPE_DEFAULT = None
    TYPE_CHOICES = None
    type = models.CharField('项目类型', max_length=20, choices=TYPE_CHOICES, default=TYPE_DEFAULT)

    class Meta:
        abstract = True


class WithStatus(_BaseModel):
    STATUS_DEFAULT = 'ok'
    STATUS_CHOICES = (('ok', '正常'), ('error', '异常'), ('pass', '通过'), ('fail', '失败'))
    status = models.CharField('状态', max_length=20, choices=STATUS_CHOICES, default=STATUS_DEFAULT)

    class Meta:
        abstract = True


class WithOperator(_BaseModel):
    operator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_operator",
        verbose_name="修改人"
    )

    class Meta:
        abstract = True


class WithManager(_BaseModel):
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_manager",
        verbose_name="负责人", blank=True, null=True
    )

    class Meta:
        abstract = True


class WithAssignee(_BaseModel):
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_assignee",
        verbose_name="指派给", blank=True, null=True
    )

    class Meta:
        abstract = True


class WithUrl(_BaseModel):
    url = models.CharField('URL', max_length=500, null=True, blank=True)

    class Meta:
        abstract = True


class WithImage(_BaseModel):
    image = models.ImageField('缩略图', upload_to='uploads/', null=True, blank=True)

    class Meta:
        abstract = True


class WithWatchers(_BaseModel):
    watchers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name="关注人",
        related_name="%(app_label)s_%(class)s_watchers",
        blank=True)

    class Meta:
        abstract = True


class WithMembers(_BaseModel):
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name="成员",
        related_name="%(app_label)s_%(class)s_members",
        blank=True)

    class Meta:
        abstract = True


class WithCreated(_BaseModel):
    created = models.DateTimeField("创建日期", auto_now_add=True)

    class Meta:
        abstract = True


class WithModified(_BaseModel):
    modified = models.DateTimeField(
        auto_now=True, verbose_name="修改日期"
    )

    class Meta:
        abstract = True
        ordering = ['-modified']


class WithActive(_BaseModel):
    active = models.NullBooleanField("已启用", default=True)

    class Meta:
        abstract = True


class WithDeleted(_BaseModel):
    deleted = models.NullBooleanField("已删除", default=False)

    class Meta:
        abstract = True


class WithParent(_BaseModel):
    parent = models.ForeignKey(
        'self',
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_parent",
        verbose_name="父级对象"
    )

    class Meta:
        abstract = True

    @property
    def path(self):
        node, parents = self, [self]
        while node.parent:
            parents.append(node.parent)
            node = node.parent
        parents.reverse()
        return '/' + '/'.join([str(item) for item in parents])


class WithStartEndTime(_BaseModel):
    start_time = models.DateTimeField("开始时间",
                                      default=timezone.datetime.now, editable=True,
                                      )
    end_time = models.DateTimeField("结束时间",
                                    default=timezone.datetime.now, editable=True,
                                    null=True, blank=True,
                                    )

    class Meta:
        abstract = True


class WithStartEndDate(_BaseModel):
    start_date = models.DateField("开始日期",
                                  default=datetime.date.today, editable=True,
                                  null=True, blank=True,
                                  )
    end_date = models.DateField("结束日期",
                                default=datetime.date.today, editable=True,
                                null=True, blank=True,
                                )

    class Meta:
        abstract = True


class WitContentType(_BaseModel):
    content_type = models.ForeignKey(
        ContentType,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('content type'),
        related_name="%(app_label)s_%(class)s_content_type",
        limit_choices_to={'app_label': 'idcops'}
    )
    object_id = models.PositiveIntegerField(
        _('object id'), blank=True, null=True)
    object_repr = GenericForeignKey('content_type', 'object_id')
    content = models.TextField(verbose_name="详细内容", blank=True)

    def __str__(self):
        return force_text(self.object_repr)

    class Meta:
        abstract = True


class WithNameDesc(WithDesc, WithName):
    class Meta:
        abstract = True


class WithCreatedModified(WithCreated, WithModified):
    class Meta:
        abstract = True


class WithKeyValueShortDesc(WithValue, WithKey, WithShortDesc):
    class Meta:
        abstract = True


class WithUser(WithCreator, WithOperator, WithCreatedModified):
    class Meta:
        abstract = True


class WithActiveDeleted(WithActive, WithDeleted):
    class Meta:
        abstract = True


class WithStage(_BaseModel):
    STAGE_CHOICES = (('dev', '开发阶段'), ('test', '测试环境测试'), ('stage', '预发测试'), ('prod', '线上测试'))
    stage = models.CharField('适用阶段', max_length=20, choices=STAGE_CHOICES, default='prod')

    class Meta:
        abstract = True


class WithTags(_BaseModel):
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True


class WithOrder(_BaseModel):
    order = models.PositiveSmallIntegerField('顺序', default=1)

    class Meta:
        abstract = True


class BaseModel(WithNameDesc, WithUser):
    class Meta:
        abstract = True




class InlineModel(WithName):
    class Meta:
        abstract = True


class RecordModel(WithCreated):
    class Meta:
        abstract = True


