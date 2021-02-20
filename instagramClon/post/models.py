from datetime import datetime
from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    description = models.CharField(max_length = 255)
    url_foto = models.TextField(null = False, blank=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def add_comment(self,*args,**kwargs):
        '''
            Add a comment to post
            **kwargs = Comment fields (title)
        '''
        self.comments.create(**kwargs)

    class Meta:
        db_table = 'post'


class Comment(models.Model):
    text = models.CharField(max_length = 255)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    response_to = models.ForeignKey('self',null = True, related_name = 'responses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'comment'

    def add_response(self,comment):
        '''
            Add a comment response to this comment
            comment: <Comment: Model>
        '''
        self.responses.add(comment)

    # responses.all() --> Devuelve una lista de respuestas de un comentario
