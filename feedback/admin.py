from django.contrib import admin

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'subject', 'text', 'date']
    list_display = ('subject', 'date')

admin.site.register(Comment, CommentAdmin)
