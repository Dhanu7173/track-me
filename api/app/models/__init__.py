from datetime import datetime
import decimal
import json
from ..extensions import db

class AppModel(db.Model):
   __abstract__ = True

   def to_dict(self):
      fields = {}
      for field in [x for x in dir(self) if not x.startswith("_") and x != 'metadata']:
         data = self.__getattribute__(field)
         if type(data) is datetime.datetime:
            data = data.strftime('%Y-%m-%d %H:%M:%S')
         if type(data) is datetime.date:
            data = data.strftime('%Y-%m-%d')
         if not hasattr(data, '__call__'):
            try:
               json.dumps(data)
               if field[-4:] == "List" and type(data) is not list:
                  fields[field] = [x for x in data.split(",") if x.strip() != ""]
               else:
                  fields[field] = data
            except TypeError:
               if type(data) is decimal.Decimal:
                  fields[field] = float(data)
               else:
                  fields[field] = None
      return fields


from .user import Users
from .projects import Projects
from .tasks import Tasks
from .files import FileAttachments
from .comments import ProjectComments
from .taskcomments import TaskComments
from .team import ProjectMembers
