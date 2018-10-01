from test.models import database
from test.models.orders import Orders
from test.models.resources import Resources

database.drop_tables([Orders, Resources])
database.create_tables([Orders, Resources])
