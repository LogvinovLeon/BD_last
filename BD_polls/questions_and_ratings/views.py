from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from questions_and_ratings.models import Question, QuestionVote, QuestionAnswer


@require_http_methods(["GET", "POST"])
def question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "GET":
        return render(request, "show_question.html", {"question": question})
    else:
        answers = request.POST.getlist("answers")
        if answers:
            answers = [get_object_or_404(QuestionAnswer, pk=int(answer)) for answer in answers]
            if QuestionVote.votes(question, request.user):
                raise PermissionDenied()
            vote = QuestionVote(user=request.user)
            vote.save()
            vote.answers.add(*answers)
        else:
            vote = QuestionVote.votes(question, request.user)
            vote.delete()
