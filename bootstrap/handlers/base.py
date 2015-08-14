"""
Defines the base controller that all of the bootstrap controllers inherit from
"""

import oz
from .. import middleware

class BaseHandler(oz.RequestHandler, middleware.BoostrapMiddleware):
    pass
