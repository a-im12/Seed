from django.db import models
from acount.models import CustomUser

class Prefecture(models.Model):
    name = models.CharField(verbose_name="都道府県名", max_length=10)

    def __str__(self):
        return self.name

class Gather(models.Model):
    user_id = models.ForeignKey(CustomUser, verbose_name="募集主", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="タイトル", max_length=100)
    prefecture = models.ForeignKey(Prefecture, verbose_name="都道府県", on_delete=models.CASCADE)
    access = models.CharField(verbose_name="アクセス", max_length=200)
    contact = models.CharField(verbose_name="連絡先", max_length=254)
    detail = models.TextField(verbose_name="詳細", max_length=300)
    create_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)

class Mission(models.Model):
    rank = models.TextField(verbose_name="ランク", max_length=5)
    mission = models.TextField(verbose_name="ミッション", max_length=100)

class MissionDetail(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, verbose_name="ミッション", on_delete=models.CASCADE)
    draw_time = models.DateTimeField(verbose_name="抽選日時")

