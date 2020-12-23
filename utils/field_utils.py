import json
from datetime import datetime, date, timedelta

import yaml
import django
from django.core.exceptions import ValidationError
from django import forms
from django.db import models
from django.core import exceptions
from django.utils.encoding import force_text
from django.core.exceptions import ObjectDoesNotExist


class YamlWidget(forms.Textarea):
    def __init__(self, attrs=None):
        default_attrs = {'cols': '40', 'rows': '5'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""
        if not isinstance(value, str):
            value = yaml.safe_dump(value, default_flow_style=False, allow_unicode=True)
        if django.VERSION < (2, 0):
            return super().render(name, value, attrs)
        return super().render(name, value, attrs, renderer)


class YamlFormField(forms.CharField):
    empty_values = [None, '']

    def __init__(self, *args, **kwargs):
        if 'widget' not in kwargs:
            kwargs['widget'] = YamlWidget
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, str) and value:
            try:
                return yaml.safe_load(value)
            except Exception as exc:
                raise forms.ValidationError('Yaml decode error: %s' % (exc.args[0],))
        else:
            return value

    def validate(self, value):
        if value in self.empty_values and self.required:
            raise forms.ValidationError(self.error_messages['required'], code='required')


class YamlField(models.Field):
    description = "Yaml object"

    def get_internal_type(self):
        return 'TextField'

    def formfield(self, **kwargs):
        defaults = {
            'form_class': YamlFormField,
            'widget': YamlWidget
        }
        defaults.update(**kwargs)
        return super().formfield(**defaults)

    def to_python(self, value: str):  # 将数据库内容转为python对象时调用
        if value is None:
            if not self.null and self.blank:
                return ""
            return None
        if isinstance(value, (list, dict)):
            return value
        value = yaml.safe_load(value)
        return value

    def validate(self, value, model_instance):  # 验证从接受到字典格式
        if not self.null and value is None:
            raise ValidationError(self.error_messages['null'])
        try:
            self.get_prep_value(value)
        except ValueError:
            raise ValidationError(self.error_messages['invalid'] % value)

    def get_prep_value(self, value: (list, dict)):  # 保存时插入数据, 转为字符串存储
        if value is None:
            return None
        value = yaml.safe_dump(value, allow_unicode=True)
        return value

    def from_db_value(self, value: str, expression, connection, *args, **kwargs):  # 从数据库读取字段是调用
        return self.to_python(value)

    def value_to_string(self, obj):  # Rest Framework调用时
        return self.value_from_object(obj)


class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        if isinstance(obj, timedelta):
            return obj.seconds

        return json.JSONEncoder.default(self, obj)


def json2dict(json_str: str) -> (None, dict):
    if json_str == "{}":
        return None
    try:
        return json.loads(json_str)
    except json.decoder.JSONDecodeError:
        print('json解码错误', json_str)
        return json_str


class OrderField(models.PositiveIntegerField):

    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super(OrderField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            # 如果没有值，查询自己所在表的全部内容，找到最后一条字段，设置临时变量value = 最后字段的序号+1
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    # 存在for_fields参数，通过该参数取对应的数据行
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)
                # 取最后一个数据对象的序号
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(OrderField, self).pre_save(model_instance, add)


class JSONField(models.TextField):
    """读取时: from_db_value
    写入时: from_db_value --> to python --> get_prep_value
    """
    def to_python(self, value):  # 将数据库内容转为python对象时调用
        print('to python', value, type(value))
        if not value:
            value = {}
        if isinstance(value, (list, dict)):
            return value
        return json2dict(value)

    def get_prep_value(self, value):  # create时插入数据, 转为字符串存储
        print('get_prep_value', value, type(value))
        return value if value is None else json.dumps(value)

    def from_db_value(self, value, expression, connection):  # 从数据库读取字段是调用
        print('from_db_value', value, type(value))
        return json2dict(value)


class MultipleSelectFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple


class MultipleSelectField(models.Field):
    __metaclass__ = models.CharField

    def get_internal_type(self):
        return "CharField"

    def get_choices_default(self):
        return self.get_choices(include_blank=False)

    def formfield(self, **kwargs):
        # don't call super, as that overrides default widget if it has choices
        defaults = {
            'required': not self.blank,
            'label': self.verbose_name.capitalize(),
            'help_text': self.help_text,
            'choices': self.choices
        }

        if self.has_default():
            defaults['initial'] = self.get_default()

        defaults.update(kwargs)

        return MultipleSelectFormField(**defaults)

    def get_db_prep_value(self, value, connection, prepared=False):
        if isinstance(value, list):
            return ",".join(map(str, value))
        if value is None or isinstance(value, str):
            return value
        else:
            return str(value)

    def to_python(self, value):
        if value is None or isinstance(value, list):
            return value
        else:
            return str(value).split(",")

    def validate(self, value, model_instance):
        if not self.editable:
            # Skip validation for non-editable fields.
            return

        if self.choices and value not in self.empty_values:
            if not isinstance(value, list):
                value = [value]
            if set(dict(self.choices).keys()) & set(value) == set(value):
                return
            raise exceptions.ValidationError(
                self.error_messages['invalid_choice'],
                code='invalid_choice',
                params={'value': value},
            )

        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_messages['null'], code='null')

        if not self.blank and value in self.empty_values:
            raise exceptions.ValidationError(self.error_messages['blank'], code='blank')

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(MultipleSelectField, self).contribute_to_class(cls, name)

        if self.choices:
            fieldname = self.name
            choicedict = dict(self.choices)

            def func(self):
                value = getattr(self, fieldname)
                if not isinstance(value, list):
                    value = [value]
                return ", ".join([force_text(choicedict.get(i, i)) for i in value])

            setattr(cls, 'get_%s_display' % fieldname, func)
