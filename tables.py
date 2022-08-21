from flask_table import Table, Col, LinkCol
 
class Results(Table):
    user_id = Col('Id', show=False)
    user_name = Col('Name')
    user_email = Col('Email')
    user_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))
class Results_post(Table):
    id = Col('Id', show=False)
    post_title = Col('title')
    post_contents = Col('nội dung')
    edit = LinkCol('Edit', 'edit_post_view', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete_post', url_kwargs=dict(id='id'))
