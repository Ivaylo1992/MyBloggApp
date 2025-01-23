from libgravatar import Gravatar


def create_avatar(email):
    g = Gravatar(email)

    return g.get_image(default='http://cdn-icons-png.flaticon.com/512/12225/12225935.png')
