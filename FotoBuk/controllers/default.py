@auth.requires_login()
def index():
	li=db(db.image).select()
	return dict(li=li)

@auth.requires_login()
def insert():
    db.image.author.default=auth.user.first_name
    db.image.author_id=auth.user_id
    form=SQLFORM(db.image)
    if form.process().accepted:
        response.flash = 'your image is posted'
    return dict(form=form)

@auth.requires_login()
def show():
    flag=0
    image = db(db.image.id==request.args(0)).select().first()
    db.comment.image_id.default = image.id
    cur_user=auth.user_id
    form = SQLFORM(db.comment)
    likes = (db)(db.like.like_id==image.id).select()
    #query = (db.like.like_id==image.id and db.like.liker==cur_user)
    #if db(query).count>0:
    if (db(db.like.like_id==image.id)(db.like.liker==cur_user)).count()> 0:
	    flag=1;
    else:
	    flag=0;
    print likes
#    for lik in likes:
#	    if cur
#	    if int(cur_user) == int(lik.liker):
#		    flag=1
    print flag
    form2 = SQLFORM(db.like)
    if form2.process().accepted:
	print 'yes'
	response.flash = 'You have liked the image'
    	db.like.insert(likername=auth.user.first_name)
	db.like.insert(liker=auth.user_id)
	db.like.insert(like_id=image.id)
    else:
	response.flash = 'You already like this image'

    if form.process().accepted:
        response.flash = 'your comment is posted'

    comments = db(db.comment.image_id==image.id).select()
    return dict(cur_user=cur_user,flag=flag,image=image, comments=comments, likes=likes, form=form, form2=form2)

def delete():
    db(db.image.id==request.args(0)).delete()
    image = db(db.image.id==request.args(0)).select()

def user():
	return dict(form=auth())

def download():
	return response.download(request,db)
