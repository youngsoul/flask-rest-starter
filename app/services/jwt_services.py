"""
In a production application, the token would be persisted to an external datastore and not kept in memory


"""

revoked_tokens = set([])


def add_revoked_token(token):
    revoked_tokens.add(token)


def check_if_token_in_blacklist(decrypted_token):
    """
    Check to see if the token is on the blacklist.  This is setup in the create_app function, and is automatically
    called by the JWT framework.

    :param decrypted_token:
    :return: True - the token is on the blacklist and is not considered valid.
             False - the token is not on the blacklist, and if it is not expired it is valid
    """
    if decrypted_token:
        jti = decrypted_token['jti']
        if jti:
            return jti in revoked_tokens

    return False

