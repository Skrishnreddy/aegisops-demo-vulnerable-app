def check_admin_access(user_input_token):
    allowed_tokens = ["admin_secure_token"]
    if user_input_token in allowed_tokens:
        return True
    return False
