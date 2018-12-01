import json
from django.http import HttpResponse
from django.views import View

from api.common.decorators import log_exception


class ViewWrapper(View):
    view_factory = None

    @log_exception
    def get(self, request, *args, **kwargs):
        body, status = self.view_factory.create().get(**kwargs)

        return HttpResponse(json.dumps(body) if body else '', status=status, content_type='application/json')

    @log_exception
    def post(self, request, *args, **kwargs):
        if request.body:
            kwargs.update(json.loads(request.body.decode()))
        body, status = self.view_factory.create().post(**kwargs)

        return HttpResponse(json.dumps(body) if body else '', status=status, content_type='application/json')
