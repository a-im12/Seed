from django.contrib import admin
from .models import Prefecture, Gather, Mission, MissionDetail, Genre, Product, Favorite, Community, CommunityGenre

class PrefectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class GatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'title', 'create_at')
    list_display_links = ('id', 'user_id', 'title', 'create_at')

class MissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'rank', 'mission')
    list_display_links = ('id', 'rank', 'mission')

class MissionDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'draw_time')
    list_display_links = ('user', 'draw_time')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'company')
    list_display_links = ('id', 'name', 'price', 'company')

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user')
    list_display_links = ('id', 'product', 'user')

class CommunityGenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('user', 'genre', 'title', 'posted_at', 'best_answer')
    list_display_links = ('user', 'genre', 'title', 'posted_at', 'best_answer')

admin.site.register(Prefecture, PrefectureAdmin)
admin.site.register(Gather, GatherAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(MissionDetail, MissionDetailAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(CommunityGenre, CommunityGenreAdmin)
admin.site.register(Community, CommunityAdmin)
