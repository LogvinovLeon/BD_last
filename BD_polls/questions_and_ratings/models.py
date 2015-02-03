from cms.models import CMSPlugin
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class QuestionRatingMixin(models.Model):
    start = models.DateTimeField(default=timezone.now())
    end = models.DateTimeField()
    show_results_before_end = models.BooleanField(default=False)
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

    def is_active(self):
        return timezone.now() <= self.end

    class Meta:
        abstract = True


class VoteMixin(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True


class Question(QuestionRatingMixin):
    multiple_answers = models.BooleanField(default=False)

    def get_results(self):
        if self.show_results_before_end or not self.is_active():
            answers = QuestionAnswer.objects.filter(question=self)
            return dict((answer.text, answer.questionvote_set.count()) for answer in answers)
        else:
            return None


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=200)


class QuestionVote(VoteMixin):
    answers = models.ManyToManyField(QuestionAnswer)

    @staticmethod
    def votes(question, user):
        return QuestionVote.objects.filter(answers__question=question, user=user)


class Rating(QuestionRatingMixin):
    max = models.IntegerField()
    TYPES = (
        ("STARS", "stars rating"),
        ("SLIDER", "slider rating"),
        ("LIKES", "like rating"),
    )
    type = models.CharField(max_length=10, choices=TYPES)

    def get_results(self):
        if self.show_results_before_end or not self.is_active():
            return dict((i, self.ratingvote_set.filter(value=i).count()) for i in range(1, self.max + 1))
        else:
            return None


class RatingVote(VoteMixin):
    rating = models.ForeignKey(Rating)
    value = models.IntegerField()

    @staticmethod
    def votes(rating, user):
        return RatingVote.objects.filter(rating=rating, user=user)


class QuestionPlugin(CMSPlugin):
    question = models.ForeignKey(Question)


class RatingPlugin(CMSPlugin):
    rating = models.ForeignKey(Rating)