from google.appengine.ext import ndb
from google.appengine.api import users

class Picture(ndb.Model):
	image = ndb.BlobProperty(required = True) 
	caption = ndb.StringProperty(required = False)
	owner = ndb.KeyProperty(kind = 'KinstaUser')

class KinstaUser(ndb.Model):
    user_id = ndb.StringProperty()
    username = ndb.StringProperty()
    name = ndb.StringProperty(required = True)
    profile_pic = ndb.KeyProperty(Picture)
    fingerpaints = ndb.KeyProperty(Picture, repeated= True)
    friends = ndb.StringProperty(repeated=True)

    @classmethod
    def get_by_user(cls, user):
        return cls.query().filter(cls.user_id == user.user_id()).get()