from django.contrib import admin
from .models import Question, Answer, QuizSession, Recommendation

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizSession)
admin.site.register(Recommendation)
