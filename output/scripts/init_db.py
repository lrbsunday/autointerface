from autointerface.models import database
from autointerface.models.projects import Projects
from autointerface.models.models import Models
from autointerface.models.fields import Fields
from autointerface.models.interfaces import Interfaces
from autointerface.models.params import Params

database.drop_tables([Projects, Models, Fields, Interfaces, Params])
database.create_tables([Projects, Models, Fields, Interfaces, Params])
