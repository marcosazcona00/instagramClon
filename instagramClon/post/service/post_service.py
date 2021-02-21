from user.service.user_service import UserService
from post.repository.post_repository import PostRepository

class PostService(object):
    def __init__(self):
        self._post_repository = PostRepository()

    def create(self,user_id,post_data):
        '''
            Create a new post in instagram
            user_id: <int>
            post_data: <Dict: {}>
            Return: <Post: Model>
        '''
        user = UserService().find_by_id(user_id)
        return self._post_repository.create(user,post_data)