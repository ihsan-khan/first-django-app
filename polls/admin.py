from django.contrib import admin
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    fields = ('pub_date', 'question_text')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

