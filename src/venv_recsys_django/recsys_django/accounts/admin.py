from django.contrib import admin

from accounts.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """カスタムユーザ管理クラス
    """
    list_display =  ('id', 'username', 'user_id')
    list_display_links = ('id', 'username', 'user_id')


admin.site.register(CustomUser, CustomUserAdmin)
