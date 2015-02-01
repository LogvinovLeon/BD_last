from django.contrib import admin
from models import Question, QuestionAnswer, Rating
from questions_and_ratings.models import QuestionVote, RatingVote


class QuestionAnswerInline(admin.StackedInline):
    model = QuestionAnswer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionAnswerInline]


class RatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(QuestionVote)
admin.site.register(RatingVote)