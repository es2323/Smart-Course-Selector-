from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)  # The question text

    def __str__(self):
        return self.text

    # Helper method to create default answers (Yes/No)
    def add_default_answers(self):
        Answer.objects.get_or_create(question=self, text="Yes", score=1)
        Answer.objects.get_or_create(question=self, text="No", score=0)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    text = models.CharField(max_length=255)
    score = models.IntegerField()

    def __str__(self):
        return self.text



class QuizSession(models.Model):
    current_question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL, related_name="quiz_sessions")
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return f"Session ID: {self.id} (Current Question: {self.current_question})"


class Recommendation(models.Model):
    degree_name = models.CharField(max_length=255)
    criteria = models.TextField()

    def __str__(self):
        return self.degree_name
