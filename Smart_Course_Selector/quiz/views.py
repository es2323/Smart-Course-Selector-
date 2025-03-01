from django.shortcuts import render, get_object_or_404, redirect
from .models import QuizSession, Question, Recommendation, Answer
from .forms import QuizForm

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html')


def start_quiz(request):
    # Get the first question (or None if no questions exist)
    first_question = Question.objects.first()

    # Create a new QuizSession and set the first question
    session = QuizSession.objects.create(current_question=first_question)

    # Redirect to the quiz view with the session ID
    return redirect('quiz_with_session', session_id=session.id)




def get_next_question(session):
    answered_questions = session.answers.values_list('question', flat=True)
    return Question.objects.exclude(id__in=answered_questions).first()




def quiz(request, session_id):
    session = get_object_or_404(QuizSession, id=session_id)

    if session.current_question is None:
        # Redirect or handle missing current_question
        return redirect('index')

    current_question = session.current_question

    if request.method == 'POST':
        form = QuizForm(current_question, request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            session.answers.add(answer)
            # Get the next question
            next_question = get_next_question(session)
            if next_question:
                session.current_question = next_question
                session.save()
                return redirect('quiz_with_session', session_id=session.id)
            else:
                return redirect('display_recommendation', session_id=session.id)
    else:
        form = QuizForm(current_question)

    return render(request, 'quiz/quiz.html', {
        'form': form,
        'question': current_question
    })

