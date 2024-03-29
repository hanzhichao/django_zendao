from django.db import models
from django.conf import settings
from django.utils import timezone

from utils.field_utils import YamlField, RichTextField
from utils.model_utils import (BaseModel, BaseMeta, InlineModel, WithLevel, WithTags,  WithStatus,WithStage,
                               RecordModel,  WithOrder, WithAssignee, WithManager, WithStartEndDate,
                               WithParent, NULLABLE_FK
                               )

from mproduct.models import WithProductModule,  ProductRelease
from mproject.models import WithProject, Requirement, Task


class TestPlan(BaseModel, WithProject, WithManager, WithLevel, WithStartEndDate):
    TEST_PLAN_STATUS_CHOICES = (('new', '未开始'),
                              ('processing', '进行中'),
                              ('blocked', '被阻碍'),
                              ('done', '完成'))
    status = models.CharField('当前状态', max_length=20, choices=TEST_PLAN_STATUS_CHOICES, default='new')
    cc_to = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_%(class)s_cc_to", verbose_name="抄送给", blank=True)
    related_release = models.ForeignKey(ProductRelease, verbose_name='关联版本',
                                            related_name="%(app_label)s_%(class)s_related_version", **NULLABLE_FK)

    test_summary = RichTextField('测试总结', blank=True, null=True)
    test_cases = models.ManyToManyField('TestCase', verbose_name='用例', blank=True, through='TestPlanCase')

    class Meta(BaseMeta):
        verbose_name = '测试计划'
        verbose_name_plural = '测试计划'


class TestPlanCase(models.Model):
    TEST_RESULT_CHOICES = (('pass', '通过'), ('fail', '失败'), ('error', '异常'))
    TEST_STATUS_CHOICES = (('new', '未开始'), ('done', '已完成'))

    test_plan = models.ForeignKey('TestPlan', verbose_name='测试计划', related_name='%(app_label)s_%(class)s_test_case',on_delete=models.CASCADE)
    test_case = models.ForeignKey('TestCase', verbose_name='测试用例', related_name='%(app_label)s_%(class)s_test_case', on_delete=models.CASCADE)
    tester = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_operator",
        verbose_name="执行人", blank=True, null=True
    )
    test_start_time = models.DateTimeField("执行时间", default=timezone.datetime.now, editable=True)
    test_result = models.CharField('结果', max_length=20, choices=TEST_RESULT_CHOICES, blank=True, null=True)
    test_status = models.CharField('状态', max_length=20, choices=TEST_STATUS_CHOICES, blank=True, null=True)

    class Meta(BaseMeta):
        verbose_name = '测试用例'
        verbose_name_plural = '测试用例'

    def __str__(self):
        return ''


class TestCase(BaseModel, WithProductModule, WithTags, WithLevel):
    TESTCASE_TYPE_CHOICES = (('func_test', '功能'),
                             ('perf_test', '性能'),
                             ('conf_test', '配置相关'),
                             ('deploy_test', '安装部署'),
                             ('sec_test', '安全相关'),
                             ('api_test', '接口测试'),
                             ('else', '其他'))
    TESTCASE_STAGE_CHOICES = (('func_test', '功能测试阶段'),
                              ('integrate_test', '集成测试阶段'),
                              ('sys_test', '系统测试阶段'),
                              ('unit_test', '单元测试阶段'),
                              ('smoke_test', '冒烟测试阶段'),
                              ('version_verify', '版本验证阶段'))
    type = models.CharField('用例类型', max_length=20, choices=TESTCASE_TYPE_CHOICES, default='func_test')
    stage = models.CharField('适用阶段', max_length=20, choices=TESTCASE_STAGE_CHOICES, default='prod')
    related_requirement = models.ForeignKey(Requirement, verbose_name='关联需求',
                                            related_name="%(app_label)s_%(class)s_related_requirement", **NULLABLE_FK)
    pre_condition = RichTextField('预置条件', blank=True)

    class Meta(BaseMeta):
        verbose_name = '测试用例'
        verbose_name_plural = '测试用例'


class TestStep(WithOrder, InlineModel):
    test_case = models.ForeignKey(TestCase, verbose_name='测试用例', related_name='%(app_label)s_%(class)s_test_case', on_delete=models.CASCADE)
    excepted = models.CharField('预期', max_length=200, null=True, blank=True)

    class Meta(BaseMeta):
        verbose_name = '测试步骤'
        verbose_name_plural = '测试步骤'


class TestCaseRecord(RecordModel, WithStatus):
    test_case = models.ForeignKey(TestCase, verbose_name='测试用例', related_name='%(class)s_test_case', on_delete=models.CASCADE)
    data = YamlField('测试结果数据', null=True, blank=True)

    class Meta(BaseMeta):
        verbose_name = '测试用例记录'
        verbose_name_plural = '测试用例记录'


