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
    image = models.ImageField(verbose_name="画像", upload_to='gather_img/', null=True)
    create_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)

class Mission(models.Model):
    rank = models.TextField(verbose_name="ランク", max_length=5)
    mission = models.TextField(verbose_name="ミッション", max_length=100)

class MissionDetail(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, verbose_name="ミッション", on_delete=models.CASCADE)
    draw_time = models.DateTimeField(verbose_name="抽選日時")

class Genre(models.Model):
    name = models.CharField(verbose_name="ジャンル名", max_length=10)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name="商品名", max_length=50)
    genre = models.ForeignKey(Genre, verbose_name="ジャンル", on_delete=models.CASCADE)
    default_price = models.IntegerField(verbose_name="定価")
    price = models.IntegerField(verbose_name="割引価格")
    deadline = models.DateTimeField(verbose_name="賞味・消費期限")
    image = models.ImageField(verbose_name="商品画像", upload_to='product_img/')
    detail = models.TextField(verbose_name="詳細", max_length=300)
    company = models.ForeignKey(CustomUser, verbose_name="掲載企業", on_delete=models.CASCADE)
    create_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    expiration = models.BooleanField(verbose_name="消費期限")

class Favorite(models.Model):
    product = models.ForeignKey(Product, verbose_name="商品", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.CASCADE)

class CommunityGenre(models.Model):
    name = models.CharField(verbose_name='Community ジャンル', max_length=10)
    
    def __str__(self):
        return self.name

class Community(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    genre = models.ForeignKey(CommunityGenre, verbose_name='Community ジャンル', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Community タイトル', max_length=70)
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    best_answer = models.BooleanField(verbose_name='ベストアンサー', default=False)

class CommunityMessage(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    community = models.ForeignKey(Community, verbose_name='Community', on_delete=models.CASCADE)
    message = models.CharField(verbose_name='メッセージ', max_length=300, null=False)
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    best_flg = models.BooleanField(verbose_name='ベストアンサー', default=False)

class Like(models.Model):
    community_message = models.ForeignKey(CommunityMessage, verbose_name='CommunityMessage', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)