import json

from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from questions_and_ratings.models import Question, QuestionVote, QuestionAnswer, Rating, RatingVote


@require_http_methods(["POST"])
def question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        answers = request.POST.getlist("answers")
        if answers:
            answers = [get_object_or_404(QuestionAnswer, pk=int(answer)) for answer in answers]
            if QuestionVote.votes(question, request.user):
                raise PermissionDenied()
            vote = QuestionVote(user=request.user)
            vote.save()
            vote.answers.add(*answers)
            return HttpResponse(json.dumps(question.get_results()))
        else:
            vote = QuestionVote.votes(question, request.user)
            vote.delete()
            return HttpResponse(json.dumps(question.get_results()))


@require_http_methods(["POST"])
def rating_view(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    if request.method == "POST":
        answers = request.POST.getlist("answers")
        if answers:
            if RatingVote.votes(rating, request.user):
                raise PermissionDenied()
            vote = RatingVote(rating=rating, value=int(answers[0]), user=request.user)
            vote.save()
            return HttpResponse(json.dumps(rating.get_results()))
        else:
            vote = RatingVote.votes(rating, request.user)
            vote.delete()
            return HttpResponse(json.dumps(rating.get_results()))
