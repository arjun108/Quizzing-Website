from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question,Choice,Category

@login_required
def index(request):
    category_list = Category.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def category(request, category_id):
	question_list = Question.objects.all().filter(category = category_id)
	template = loader.get_template('polls/category.html')
	context = {
		'question_list': question_list,
		'category_id': category_id,
	}
	return HttpResponse(template.render(context, request))

@login_required
def result(request, score):
    template = loader.get_template('polls/result.html')
    context = {
        'score': score,
	}
    return HttpResponse(template.render(context, request))

@login_required
def vote(request, category_id):
    score = 0
    template = loader.get_template('polls/result.html')
    question_list = Question.objects.all().filter(category = category_id)
    for question in question_list:
    	question_id = question.id
    	answer = question.choice_set.get(answer=True)
    	selected_choice = question.choice_set.get(pk=request.POST['choice'+ str(question_id)])
    	if answer == selected_choice:
    		score = score + 1
    context = {
    	'score': score,
    }
    return HttpResponseRedirect(reverse('polls:result', args=(score,)))