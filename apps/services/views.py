from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.services.models import Services
from apps.services.permissions import ServicePermission
from apps.services.serializers import ServiceCreateSerializer, ServiceImageSerializer, ServiceListSerializer


class ServiceCreateAPIView(CreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [ServicePermission]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ServiceList1APIView(ListAPIView):
    serializer_class = ServiceListSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        if category_id is None:
            raise Http404("Category ID is required")

        queryset = Services.objects.filter(category=category_id)
        if not queryset.exists():
            raise Http404("Services not found")

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ServiceListAPIView(ListAPIView):
    serializer_class = ServiceListSerializer

    def get_queryset(self):
        order_by_param = self.request.query_params.get('order_by', 'price')
        allowed_fields = ['price', 'name', 'category']
        if order_by_param not in allowed_fields:
            order_by_param = 'price'
        queryset = Services.objects.all().order_by(order_by_param)

        return queryset


class ServiceDeleteAPIView(DestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [ServicePermission]


class ServiceUpdateAPIView(UpdateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [ServicePermission]


class ServiceImageView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, service_id):
        choose_image = request.query_params.get('choose_image', None)

        if choose_image:
            image_instances = Services.objects.filter(id=choose_image)
            if not image_instances.exists():
                return Response({"detail": "Image not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ServiceImageSerializer(image_instances, many=True)
            return Response(serializer.data)
        else:
            service_instances = Services.objects.filter(id=service_id)

            if not service_instances.exists():
                return Response({"detail": "Service not found"}, status=status.HTTP_404_NOT_FOUND)
            image_file = request.data.get('image')
            if image_file:
                for service_instance in service_instances:
                    service_instance.image.save(image_file.name, image_file, save=True)
                    service_instance.save()

                serializer = ServiceImageSerializer(service_instances, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response({"detail": "Image file not provided"}, status=status.HTTP_400_BAD_REQUEST)

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNzc0Njg4LCJpYXQiOjE3MDE3Njc0ODgsImp0aSI6IjljZDRjZjBjYWU2OTQ2NmFhMGVjZWU4OWNlODZkMTI2IiwidXNlcl9pZCI6MX0.GfAyJ7-AxC4ZoE068OSy0t7vhOk-iCPtbVFprvNY2bo
