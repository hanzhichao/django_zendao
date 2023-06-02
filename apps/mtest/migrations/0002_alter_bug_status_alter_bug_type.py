# Generated by Django 4.0.5 on 2023-06-02 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('new', '打开'), ('resolved', '已解决'), ('closed', '已关闭')], default='new', max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='type',
            field=models.CharField(choices=[('code', '代码错误'), ('ui', '界面优化'), ('design', '设计缺陷'), ('conf', '配置相关'), ('deploy', '安装部署'), ('secure', '安全相关'), ('performance', '性能问题'), ('standard', '标准规范'), ('test_script', '测试脚本'), ('else', '其他')], default='code', max_length=20, verbose_name='缺陷类型'),
        ),
    ]
