from django import forms
from django.contrib.auth.forms import UsernameField

from .models import CustomUser


class SignupForm(forms.Form):
    """サインアップフォーム

    Attributes
    ----------
    username : UsernameField
        ユーザ名
    nickname : CharField
        ニックネーム
    password : CharField
        パスワード
    password2 : CharField
        確認用パスワード
    """
    username = UsernameField(
        label='ユーザ名',
        min_length=3,
        max_length=8,
        help_text='3文字以上8文字以内の半角英数字で入力してください。',
    )

    nickname = forms.CharField(
        label='ニックネーム',
        min_length=1,
        max_length=32,
    )

    password = forms.CharField(
        label='パスワード',
        strip=False,
        min_length=6,
        max_length=255,
        widget=forms.PasswordInput(render_value=True),
        help_text='半角英数字と記号のみ入力可能です。',
    )

    password2 = forms.CharField(
        label='パスワード（確認用）',
        strip=False,
        min_length=6,
        max_length=255,
        widget=forms.PasswordInput(render_value=True),
        help_text='確認のため、もう一度同じパスワードを入力してください。',
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.encode('utf-8').isalnum():
            self.add_error(None, 'ユーザ名は半角英数字のみで入力してください。')
        return username

    def clean(self):
        super(SignupForm, self).clean()

        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            self.add_error(None, 'このユーザ名は既に使用されています。')

        password = self.cleaned_data['password']
        password2 = self.data.get('password2')
        if password != password2:
            self.add_error(None, 'パスワードとパスワード（確認用）が一致しません。')