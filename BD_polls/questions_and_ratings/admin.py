from django.contrib import admin
from models import Question, QuestionAnswer, Rating


class QuestionAnswerInline(admin.StackedInline):
    model = QuestionAnswer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionAnswerInline]


class RatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Rating, RatingAdmin)