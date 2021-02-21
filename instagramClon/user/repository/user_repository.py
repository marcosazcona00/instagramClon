from user.models import User

# Digamos que en el repositorio iria lo que no es inherente a la logica de negocio.

class UserRepository(object):
    def get(self,id):
        '''
            Return an user by his id
            id: <int>
            Return: <User: Model>  
        ''' 
        try:
            return User.objects.get(id = id)
        except:
            return None


    def create(self,user_data):
        '''
            Create an user model 
            user_data: <Dict: {}>
            return: <User: Model>
        '''
        user = User.objects.create_user(**user_data)
        return user

    def update(self,user):
        pass
    
    def delete(self,user):
        pass
    
    def get_posts_user(self,user_id):
        '''
            Return all the posts of an user
            user_id: <int>
            Return: [<Post: Model>,<Post: Model>,<Post: Model>]

        '''
        user = self.get(user_id)
        if user is not None:
            return user.posts.all()    
        return []