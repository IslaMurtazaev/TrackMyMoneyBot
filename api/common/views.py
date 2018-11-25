import json
from django.http import HttpResponse
from django.views import View

    
class ViewWrapper(View):
    view_factory = None

    def get(self, request, *args, **kwargs):
        body, status = self.view_factory.create().get(**kwargs)

        return HttpResponse(json.dumps(body) if body else '', status=status, content_type='application/json')

    def post(self, request, *args, **kwargs):
        raise NotImplemented
