from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    from .tasks import add
    add.delay(1,2)
    print(add.delay(1,2))
    return {'project': 'proj'}
