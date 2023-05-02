from django.contrib import admin
from .models import Prefecture, Gather, Mission, MissionDetail

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

admin.site.register(Prefecture, PrefectureAdmin)
admin.site.register(Gather, GatherAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(MissionDetail, MissionDetailAdmin)
