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
    
    def calculate_total_score(self):
        # Calculate the total score based on the user's answers
        return sum(answer.score for answer in self.answers.all())
    
    def get_recommendations(self, top_n=3):
        recommendations = []
        for recommendation in Recommendation.objects.all():
            relevant_questions = recommendation.relevant_questions.all()
            answers = self.answers.filter(question__in=relevant_questions, text="Yes")
            if answers.count() == relevant_questions.count():
                recommendations.append(recommendation)

        # Limit to top_n recommendations
        return recommendations[:top_n]

class Recommendation(models.Model):
    degree_name = models.CharField(max_length=255)
    relevant_questions = models.ManyToManyField(Question) # Questions relevant to this recommendation
    criteria = models.TextField()

    def __str__(self):
        return self.degree_name
