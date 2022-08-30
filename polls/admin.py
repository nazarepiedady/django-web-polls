from django.contrib import admin

from .models import Choice, Question


# Customize your administration model here.
class ChoiceInline(admin.modelAdmin):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
