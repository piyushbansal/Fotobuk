db = DAL("sqlite://storage.sqlite")

from gluon.tools import Crud,Auth
auth=Auth(db)
crud = Crud(db)
auth.define_tables()
db.define_table('image',
   		Field('title', unique=True),
        	Field('author'),
		Field('author_id'),
   		Field('file', 'upload'),
   		format = '%(title)s')

db.define_table('comment',
		Field('image_id', db.image),
   		Field('author'),
   		Field('email'),
   		Field('body', 'text'))

db.define_table('like',
		Field('like_id',db.image),
		Field('liker'),
		Field('likername'))

#db.like.like_id.requires = IS_NOT_IN_DB(db, db.like.like_id)
#db.like.like_id.requires = IS_IN_DB(db, db.image.id, '%(title)s')
db.image.title.requires = IS_NOT_IN_DB(db, db.image.title)
db.comment.image_id.requires = IS_IN_DB(db, db.image.id, '%(title)s')
db.comment.author.requires = IS_NOT_EMPTY()
db.comment.email.requires = IS_EMAIL()
db.comment.body.requires = IS_NOT_EMPTY()

db.comment.image_id.writable = db.comment.image_id.readable = False
db.image.author.writable = db.image.author.readable = False
db.like.like_id.writable = db.like.like_id.readable = False
db.like.liker.writable = db.like.liker.readable = False
db.like.likername.writable = db.like.likername.readable = False

