from django.db import models

#title, text, createDate
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    createDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' ' + str(self.createDate)
