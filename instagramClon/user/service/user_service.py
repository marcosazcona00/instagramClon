from user.models import User
from user.repository.user_repository import UserRepository
from django.contrib.auth import authenticate,login, logout

### Capa de Servicio
# https://www.iteramos.com/pregunta/13133/diferencia-entre-repositorio-y-capa-de-servicios

### Buscar el titulo Decoupling the Service Layer
# https://docs.microsoft.com/en-us/aspnet/mvc/overview/older-versions-1/models-data/validating-with-a-service-layer-cs

class UserService(object):
    def __init__(self, user_id = None):
        self._user_id = user_id
        self._user_repository = UserRepository()

    def register_user(self,user_data):
        '''
            Register an user in the webpage
            user_data: <Dict: {}>
            return: <User: Model>
        '''
        return self._user_repository.create(user_data)

    def find_by_id(self,user_id):
        '''
            Find an user by his id
        '''
        return self._user_repository.get(user_id) 

    def get_posts_user(self,user_id):
        '''
            Return all the posts of an user
            user_id: <int>
            Return: [<Post: Model>,<Post: Model>,<Post: Model>]

        '''
        return self._user_repository.get_posts_user(user_id)
    
    
    def find_all_related_users_by_username(self,username):
        '''
            Find all the users queried by username
            username: Str
            Return: List[ <User: Model> , <User: Model> ]  
        '''
        # Esto incluso podria ser un servicio o una clase Helper Search() 
        # que tenga metodos por diferentes criterios de busqueda
        pass

    # Seguir a un usuario deberia ir aca por ejemeplo
    def add_follow(from_user, to_user):
        '''
            Add a follow from a user to another
            from_user: <User: Model>
            to_user: <User: Model>
        '''
        pass
