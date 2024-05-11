from getting import getting_bp
from posting import posting_bp

from controllers import api_bp

api_bp.register_blueprint(getting_bp)
api_bp.register_blueprint(posting_bp)
