from django.contrib import admin
from .models import Resume, JobDescription

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'match_score', 'uploaded_at')
    search_fields = ('name',)
    list_filter = ('job',)

@admin.register(JobDescription)
class JobDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

