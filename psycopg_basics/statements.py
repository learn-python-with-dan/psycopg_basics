
__all__ = [
    'create_user_stmt',
    'get_user_stmt',
]


create_user_stmt = """
    INSERT INTO users (name) VALUES (%s)
    RETURNING id
"""

get_user_stmt = """
    SELECT * FROM users WHERE id = %s
"""
