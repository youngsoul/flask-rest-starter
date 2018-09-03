revoked_tokens = set([])


def add_revoked_token(token):
    revoked_tokens.add(token)

def check_if_token_in_blacklist(decrypted_token):
    if decrypted_token:
        jti = decrypted_token['jti']
        if jti:
            return jti in revoked_tokens

    return False

