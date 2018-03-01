from django.db import models
from django.utils import timezone

# Create your models here.
# This is a place in which we will define our blog post.

# class Post(models.Model): – this line defines our model
# (it is an object).

# class is a special keyword that indicates that we are defining
# an object.

# Post is the name of our model. We can give it a different name 
# (but we must avoid special characters and whitespace). 
# Always start a class name with an uppercase letter.

# models.Model means that the Post is a Django Model, so Django knows
# that it should be saved in the database.

# models.CharField – this is how you define text with a limited number 
# of characters.
# models.TextField – this is for long text without a limit. 
# models.DateTimeField – this is a date and time.
# models.ForeignKey – this is a link to another model.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text        
