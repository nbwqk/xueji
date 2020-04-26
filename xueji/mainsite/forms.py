from mainsite import models
from django import forms
from captcha.fields import CaptchaField

class StuForms(forms.ModelForm):
      captcha=CaptchaField()
      class Meta:
          model=models.Student
          fields=['banji','xuehao','name','xingbie','birthday','jiguan','zhuzhi','phone']

      def __init__(self,*args,**kwargs):
          super(StuForms,self).__init__(*args,**kwargs)
          self.fields['banji'].label='班级'
          self.fields['xuehao'].label='学号'
          self.fields['name'].label = '姓名'
          self.fields['xingbie'].label = '性别'
          self.fields['birthday'].label = '生日'
          self.fields['jiguan'].label = '籍贯'
          self.fields['zhuzhi'].label = '住址'
          self.fields['phone'].label = '联系电话'
          self.fields['captcha'].label='确定你不是机器人'

class LoginForm(forms.Form):
    username=forms.CharField(label='姓名',max_length=10)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())


