from doniApi.apiImports import Response, GenericAPIView, status


class BpBasicAPI(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response()

    def post(self, request, *args, **kwargs):
        return Response()

    def delete(self, request, *args, **kwargs):
        return Response()

    def put(self, request, *args, **kwargs):
        return Response()
