from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Choice, Question
from django.views import generic


class Index(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class Detail(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class Results(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question': question,
            'error_message': 'You didn;t select a choice.'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(pk,)))


def owner(request):
    return HttpResponse("Hello, world. 0eaf0f79 is the polls index.")
