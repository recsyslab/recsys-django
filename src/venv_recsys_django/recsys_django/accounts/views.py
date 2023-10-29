from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Max

from online.models import User
from .forms import SignupForm
from .models import CustomUser


class SignupView(View):
    """サインアップページビュー

    Attributes
    ----------
    context: dict
        コンテキスト
    """

    def __init__(self):
        self.context = {
            'form': SignupForm(),
        }

    def get(self, request, *args, **kwargs):
        """sigunup.htmlをレンダリングしたレスポンスを取得する。

        Parameters
        ----------
        request : WSGIRequest
            リクエスト

        Returns
        -------
        HttpResponse
            signup.htmlをレンダリングしたレスポンスを返す。
        """
        return render(request, 'signup.html', self.context)

    def post(self, request, *args, **kwargs):
        """新規にサインアップしたユーザを登録する。

        Parameters
        ----------
        request : WSGIRequest
            リクエスト

        Returns
        -------
        HttpResponse
            サインアップに成功した場合、accounts:signup_successにリダイレクトする。
            サインアップに失敗した場合、signup.htmlをレンダリングしたレスポンスを返す。
        """
        # フォームのバインディング
        signup_form = SignupForm(request.POST)

        # フォームのバリデーション
        if not signup_form.is_valid():
            # サインアップに失敗した場合
            self.context['form'] = signup_form
            return render(request, 'signup.html', self.context)

        # フォームデータの取得
        username = signup_form.cleaned_data['username']
        nickname = signup_form.cleaned_data['nickname']
        password = signup_form.cleaned_data['password']

        # ユーザの登録
        custom_user = CustomUser.objects.create_user(username=username, password=password)
        user_id = User.objects.all().aggregate(Max('user_id'))['user_id__max'] + 1
        # Userモデルにも登録し、CustomUserモデルのユーザとUserモデルのユーザを紐づけする。
        user = User(user_id=user_id, name=nickname)
        user.save()
        custom_user.user = user
        custom_user.save()

        # テンプレートのリダイレクト
        return redirect(reverse('accounts:signup_success'))


class SignupSuccessView(TemplateView):
    """サインアップ完了ページビュー
    """
    # レンダリングするテンプレート
    template_name = "signup_success.html"
