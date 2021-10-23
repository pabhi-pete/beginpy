import functools

example_user = {'username': "randomuser", "access_level": "guest"}
def make_secure(access_level):
    def decorator(secure_func):
        @functools.wraps(secure_func)
        def secure_function(*args, **kwargs):
            if example_user["access_level"] == access_level:
                return secure_func(*args, **kwargs)
            else:
                return f'No {access_level} for {example_user["username"]!r}.'
        return secure_function
    return decorator

#decorator 1st called
@make_secure("admin")
def get_admin_password():
   return "admin: 12345"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())