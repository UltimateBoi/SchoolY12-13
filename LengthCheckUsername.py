def is_valid_username(username):
    if not username:
        return False
    return 3 <= len(username) <= 15