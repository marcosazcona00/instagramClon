from post.models import Post
from user.service.user_service import UserService

class PostRepository(object):
    def create(self,user,post_data):
        '''
            Create a new post in instagram
            user_id: <int>
            post_data: <Dict: {}>
            Return: <Post: Model>
        '''
        return Post.objects.create(**post_data, user = user)