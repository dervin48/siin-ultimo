from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import *
from core.pos.models import Category, Product, Client


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

    def list(self, request, *args, **kwargs):
        return Response({'id': 4})


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return self.get_serializer().Meta.model.objects.all()

    def get(self, request, *args, **kwargs):
        # print(self.request.query_params['name'])
        # print(self.request.query_params.get('name', 'William Vargas'))
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(self.queryset)
        # items = [i.toJSON() for i in Category.objects.all()]
        # queryset = self.get_serializer().Meta.model.objects.all()
        serializer = self.serializer_class(self.queryset.all(), many=True)
        # return self.list(request, *args, **kwargs)
        return Response(serializer.data)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializers

    def post(self, request, *args, **kwargs):
        print(self.request.data)
        return self.create(request, *args, **kwargs)


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def put(self, request, *args, **kwargs):
        print(self.request.data)
        return self.update(request, *args, **kwargs)


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def delete(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=self.kwargs['pk'])
        instance.delete()
        return Response({'msg': f"Se ha eliminado correctamente el pk {self.kwargs['pk']}"})


class CategoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(self.request.query_params)
        return Response({'resp': False})

    def post(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        # serializer = CategorySerializers(queryset, many=True)
        serializer = [i.toJSON() for i in queryset]
        return Response(serializer)
