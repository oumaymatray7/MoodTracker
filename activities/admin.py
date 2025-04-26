from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'msg_type', 'created_at')
    search_fields = ('name', 'email', 'msg_type', 'message')
    list_filter = ('msg_type', 'created_at')
