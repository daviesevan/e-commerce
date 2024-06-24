from flask import Blueprint

admin_auth_bp = Blueprint(
    'adminportal',
    __name__,
    url_prefix='/auth/admin'
)

@admin_auth_bp.post('/login')
def login():
    pass