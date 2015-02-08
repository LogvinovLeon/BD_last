from django.shortcuts import get_object_or_404, render
from questions_and_ratings.models import Question, Rating


def sview(request):
    q = Question.objects.all()
    r = Rating.objects.all()
    dictionary = {'qs': q, 'rs': r}
    return render(request, 'raports/templates/raports.html', dictionary)


def generate(request):
    qs = Question.objects.all()
    q_list = []
    for q in qs:
        is_on = request.GET.get(str(q.id), 'f')
        if is_on == "on":
            q_list.append(q.id)
    rs = Rating.objects.all()
    for r in rs:
        is_on = request.GET.get('r' + str(r.id), 'f')
        if is_on == "on":
            q_list.append(-r.id)
    wanted_results = []
    for pk in q_list:
        if pk > 0:
            q = get_object_or_404(Question, pk=pk)
        else:
            q = get_object_or_404(Rating, pk=-pk)
        infos = []
        results = q.get_results()
        for key, value in results.iteritems():
            infos.append((key, value))
        wanted_results.append((q, infos))
    print wanted_results
    dictionary = {'results': wanted_results}
    return render(request, 'raports/templates/results.html', dictionary)
