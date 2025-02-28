from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html')


def quiz(request, question_id=None):
    if request.method == 'POST':
        # Save the user's answer
        selected_answer = request.POST.get('answer')
        question_id = request.POST.get('question_id')
        question = get_object_or_404(Question, id=question_id)
        Answer.objects.create(
            question=question,
            selected_answer=selected_answer,
            score=(selected_answer == question.correct_option)
        )

    if question_id:
        question = get_object_or_404(Question, id=question_id)
    else:
        # Get the first question
        question = Question.objects.first()

    # Get the next question ID
    next_question = Question.objects.filter(id__gt=question.id).first()

    context = {
        'question': question,
        'next_question_id': next_question.id if next_question else None,
    }
    return render(request, 'quiz/quiz.html', context)