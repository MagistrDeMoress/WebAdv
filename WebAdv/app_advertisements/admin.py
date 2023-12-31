from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'blue_title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'img', 'user']
    list_filter = ['auction', 'created_at', 'updated_at']
    actions = ['make_action_as_false', 'make_action_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)