from django.db import models
from django.contrib.auth.models import User as UserDjango

# Create your models here.

class User(UserDjango):
    class Meta:
        db_table = 'user'

    def _same_user(self,user):
        '''
            Check if two users are the same user
            user: <User: Model>
            Return: Boolean
        '''
        return self.id == user.id

    def is_followed_by(self,user):
        '''
            Check if this user is already followed by the requested user
            user: <User: Model>
            Return: Boolean
        '''
        # Se fija si entre sus seguidores esta el usuario al que le quiere dar el follow
        return self.follower.filter(from_user = user).exists()
        
    def add_follower(self,follower_user):   
        '''
            Add a follower to this user
            user_to_follow: <User: Model>
            Return: Boolean
        '''
        if not self._same_user(follower_user) and not self.is_followed_by(follower_user):
            Follow.objects.create(from_user = follower_user, to_user = self)
            return True
        return False
        
    def followers(self):
        '''
            Return the followers of user
            Return: [ <User>, <User> ]
        '''
        return [ follow.from_user for follow in self.follower.all() ]

    def followings(self):
        '''
            Return the users that this instance follow to
            Return: [ <User>, <User> ]
        '''
        return [ follow.to_user for follow in self.following.all() ]

    #def _create_post(self):
    #    Este metodo no lo voy a usar, es para acordarme como crear un post
    #    user.posts.create(argumentos)

class Follow(models.Model):
    from_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='following')
    to_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='follower')

    class Meta:
        db_table = 'follow'
        constraints = [
            models.UniqueConstraint(fields=['from_user', 'to_user'], name='unique follow')
        ]
    