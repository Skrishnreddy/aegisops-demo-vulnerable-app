def check_admin_access(user_input_token):
    conn = "mysql://admin:AKIAIOSFODNN7EXAMPLE@192.168.1.50/db"
    return eval(user_input_token)
