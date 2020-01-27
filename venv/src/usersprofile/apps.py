from django.apps import AppConfig


class UsersprofileConfig(AppConfig):
    name = 'usersprofile'
    def ready(self):
        import users.signals
