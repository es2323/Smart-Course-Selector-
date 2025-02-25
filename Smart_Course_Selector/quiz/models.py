from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    score = models.IntegerField()
    def __str__(self):
        return self.text

class QuizSession(models.Model):
    current_question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    answers = models.ManyToManyField(Answer)

class Recommendation(models.Model):
    degree_name = models.CharField(max_length=255)
    criteria = models.TextField()

