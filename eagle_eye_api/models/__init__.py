"""
Data Models Package
Import all models here to ensure SQLAlchemy can resolve string references in relationships.
"""
# Import all models to register them with SQLAlchemy
from . import user
from . import location
from . import route
from . import event
from . import emergency
from . import building

