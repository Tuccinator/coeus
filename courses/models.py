from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    banner = models.CharField(max_length=255, blank=True, default='')
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    requirements = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title

class CourseSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=255)
    order = models.IntegerField()

class Lecture(models.Model):
    section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    type = models.IntegerField()
    title = models.CharField(max_length=100)
    notes = models.TextField()

class Video(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    link = models.CharField(max_length=255)
    link_type = models.IntegerField()
    transcript = models.TextField()

class Quiz(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True)
    complexity_level = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question = models.TextField()
    answer_type = models.IntegerField()
    reasoning = models.TextField()