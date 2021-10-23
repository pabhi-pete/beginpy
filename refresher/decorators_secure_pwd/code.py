"""
checkout the decorators function and syntax "at @"
"""

example_user = {'username': "randomuser", "access_level": "admin"}

"""
Example 1 approching decorators secure password
"""
# def get_admin_password():
#     return 12345

# def secure_function(secure_func):
#     if example_user["access_level"] == 'admin':
#         return secure_func

# now set get_admin_password = get_admin_password(secure_function)
# get_admin_password = secure_function(get_admin_password)
# print(get_admin_password) # return Noun, now we are safe and good to go


# if not it will run simply to get get_admin_password(), basically just print out
# print(get_admin_password()) # return 12345

"""
Example 2 apprched securing password
"""

# def get_admin_password():
#     return 12345

# def make_secure(secure_func):
#     def secure_function():
#         if example_user["access_level"] == 'admin':
#             return secure_func()
#         else:
#             return f'No admin permission for {example_user["username"]!r}.'
#     return secure_function

# get_admin_password = make_secure(get_admin_password)
# print(get_admin_password())

"""
Example 3 refactored example 2
if we have make_secure() function first we can use @make_secure to get_admin_password()
and we are no longer needed "get_admin_password = make_secure(get_admin_password)"
"""
import functools
def make_secure(secure_func):
    #wrapper to call get_admin_password.__name__ == get_admin_password, and != secure_function
    @functools.wraps(secure_func)
    def secure_function(*args, **kwargs): # option for decorators with parameters taking an argument
        if example_user["access_level"] == 'admin':
            return secure_func(*args, **kwargs)
        else:
            return f'No admin permission for {example_user["username"]!r}.'
    return secure_function

#decorator
@make_secure
def get_admin_password(panel):
    # return 12345 # original
    #added
    if panel == "admin":
        return 12345
    #added
    elif panel == "testering":
        return "super_dooper_secure_password"

print(get_admin_password('testering'))