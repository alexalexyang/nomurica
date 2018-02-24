from movies_crud import models
from django.conf import settings

class MovieRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read movie model go to movies db.
        """

        if model._meta.app_label == 'movies_crud':
            return 'movies_nonhegemony'

        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'movies_crud':
            return 'movies_nonhegemony'

        return 'default'

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     """
    #     Make sure the auth app only appears in the 'auth_db'
    #     database.
    #     """
    #     if app_label == 'randomizer':
    #         return db == 'movie_data.sql'
    #     return None