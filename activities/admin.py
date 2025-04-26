from django.contrib import admin

from .models import ActiviteBienEtre, Feedback  # <-- importer les deux modèles


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'msg_type', 'created_at')
    search_fields = ('name', 'email', 'msg_type', 'message')
    list_filter = ('msg_type', 'created_at')

@admin.register(ActiviteBienEtre)
class ActiviteBienEtreAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'date', 'mood', 'activity', 'comment')
    search_fields = ('mood', 'activity', 'comment')
    list_filter = ('date',)
