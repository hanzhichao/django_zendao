# Generated by Django 2.0 on 2020-12-23 06:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('mproduct', '0002_auto_20201223_1153'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('mproject', '0008_task_project'),
        ('mtest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='附件')),
            ],
            options={
                'verbose_name': '附件',
                'verbose_name_plural': '附件',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('level', models.PositiveSmallIntegerField(choices=[(0, 'O'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=2, verbose_name='优先级')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('severity', models.PositiveSmallIntegerField(choices=[(0, 'O'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=2, verbose_name='严重等级')),
                ('type', models.CharField(choices=[('code', '代码错误'), ('ui', '界面优化'), ('design', '设计缺陷'), ('conf', '配置相关'), ('deploy', '安装部署'), ('secure', '安全相关'), ('performance', '性能问题'), ('standard', '标准规范'), ('test_script', '测试脚本'), ('else', '其他')], default='code', max_length=20, verbose_name='项目类型')),
                ('platform', models.CharField(choices=[('win10', 'Windows 10'), ('win7', 'Windows 7'), ('mac', 'MacOS'), ('centos', 'CentOS'), ('ubuntu', 'ubuntu')], default='win10', max_length=20, verbose_name='操作系统')),
                ('browser', models.CharField(choices=[('chrome', 'Chrome'), ('edge', 'Edge'), ('360', '360'), ('firefox', 'firefox'), ('ie', 'IE')], default='chrome', max_length=20, verbose_name='浏览器')),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mtest_bug_assignee', to=settings.AUTH_USER_MODEL, verbose_name='指派给')),
                ('cc_to', models.ManyToManyField(blank=True, related_name='mtest_bug_cc_to', to=settings.AUTH_USER_MODEL, verbose_name='抄送给')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mtest_bug_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mtest_bug_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mtest_bug_product', to='mproduct.Product', verbose_name='所属产品')),
                ('product_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_product_branch', to='mproduct.ProductBranch', verbose_name='所属分支')),
                ('product_module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_bug_module', to='mproduct.ProductModule', verbose_name='所属模块')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bug_project', to='mproject.Project', verbose_name='所属项目')),
                ('related_release', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_bug_related_release', to='mproduct.ProductRelease', verbose_name='影响版本')),
                ('related_requirement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_bug_related_requirement', to='mproduct.ProductRequirement', verbose_name='关联需求')),
                ('related_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_bug_related_requirement', to='mproject.Task', verbose_name='关联任务')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestPlanCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='执行时间')),
                ('test_result', models.CharField(blank=True, choices=[('pass', '通过'), ('fail', '失败'), ('error', '异常')], max_length=20, null=True, verbose_name='结果')),
                ('test_status', models.CharField(blank=True, choices=[('new', '未开始'), ('done', '已完成')], max_length=20, null=True, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='TestStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='顺序')),
                ('excepted', models.CharField(blank=True, max_length=200, null=True, verbose_name='预期')),
            ],
            options={
                'verbose_name': '步骤',
                'verbose_name_plural': '步骤',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='step',
            name='test_case',
        ),
        migrations.RemoveField(
            model_name='testplansolution',
            name='test_case',
        ),
        migrations.RemoveField(
            model_name='testplansolution',
            name='test_plan',
        ),
        migrations.RemoveField(
            model_name='testreport',
            name='test_plan',
        ),
        migrations.AlterModelOptions(
            name='testplan',
            options={'ordering': ['id'], 'verbose_name': '测试计划', 'verbose_name_plural': '3.测试计划'},
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='module',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='status',
        ),
        migrations.RemoveField(
            model_name='testcaserecord',
            name='test_report',
        ),
        migrations.RemoveField(
            model_name='testplan',
            name='module',
        ),
        migrations.RemoveField(
            model_name='testplan',
            name='options',
        ),
        migrations.RemoveField(
            model_name='testplan',
            name='product',
        ),
        migrations.AddField(
            model_name='testcase',
            name='product_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testcase_product_branch', to='mproduct.ProductBranch', verbose_name='所属分支'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='product_module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_testcase_module', to='mproduct.ProductModule', verbose_name='所属模块'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='related_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_testcase_related_requirement', to='mproduct.ProductRequirement', verbose_name='关联需求'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='type',
            field=models.CharField(choices=[('func_test', '功能'), ('perf_test', '性能'), ('conf_test', '配置相关'), ('deploy_test', '安装部署'), ('sec_test', '安全相关'), ('api_test', '接口测试'), ('else', '其他')], default='func_test', max_length=20, verbose_name='项目类型'),
        ),
        migrations.AddField(
            model_name='testplan',
            name='cc_to',
            field=models.ManyToManyField(blank=True, related_name='mtest_testplan_cc_to', to=settings.AUTH_USER_MODEL, verbose_name='抄送给'),
        ),
        migrations.AddField(
            model_name='testplan',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='结束日期'),
        ),
        migrations.AddField(
            model_name='testplan',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'O'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=2, verbose_name='优先级'),
        ),
        migrations.AddField(
            model_name='testplan',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mtest_testplan_manager', to=settings.AUTH_USER_MODEL, verbose_name='负责人'),
        ),
        migrations.AddField(
            model_name='testplan',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='testplan_project', to='mproject.Project', verbose_name='所属项目'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testplan',
            name='related_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_testplan_related_release', to='mproduct.ProductRelease', verbose_name='关联版本'),
        ),
        migrations.AddField(
            model_name='testplan',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='开始日期'),
        ),
        migrations.AddField(
            model_name='testplan',
            name='status',
            field=models.CharField(choices=[('new', '未开始'), ('processing', '进行中'), ('blocked', '被阻碍'), ('done', '完成')], default='prod', max_length=20, verbose_name='当前状态'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'O'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=2, verbose_name='优先级'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mtest_testcase_product', to='mproduct.Product', verbose_name='所属产品'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='stage',
            field=models.CharField(choices=[('func_test', '功能测试阶段'), ('integrate_test', '集成测试阶段'), ('sys_test', '系统测试阶段'), ('unit_test', '单元测试阶段'), ('smoke_test', '冒烟测试阶段'), ('version_verify', '版本验证阶段')], default='prod', max_length=20, verbose_name='适用阶段'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='test_cases',
            field=models.ManyToManyField(blank=True, through='mtest.TestPlanCase', to='mtest.TestCase', verbose_name='用例'),
        ),
        migrations.DeleteModel(
            name='Step',
        ),
        migrations.DeleteModel(
            name='TestPlanSolution',
        ),
        migrations.DeleteModel(
            name='TestReport',
        ),
        migrations.AddField(
            model_name='teststep',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mtest_teststep_test_case', to='mtest.TestCase', verbose_name='测试用例'),
        ),
        migrations.AddField(
            model_name='testplancase',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mtest_testplancase_test_case', to='mtest.TestCase', verbose_name='测试用例'),
        ),
        migrations.AddField(
            model_name='testplancase',
            name='test_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mtest_testplancase_test_case', to='mtest.TestPlan', verbose_name='测试计划'),
        ),
        migrations.AddField(
            model_name='testplancase',
            name='tester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mtest_testplancase_operator', to=settings.AUTH_USER_MODEL, verbose_name='执行人'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='bug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_attachment_test_case', to='mtest.Bug', verbose_name='Bug'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='test_case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_attachment_test_case', to='mtest.TestCase', verbose_name='测试用例'),
        ),
    ]