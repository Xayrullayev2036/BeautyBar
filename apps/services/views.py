from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.services.models import Services, upload_to, Category
from apps.services.permissions import ServicePermission
from apps.services.serializers import ServiceCreateSerializer, CategorySerializer, ServiceSerializer
from apps.services.serializers import ServiceImageSerializer, ServiceListSerializer
from apps.users.serializers import UserSerializer


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

        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):

        image_data = request.data.get('image')

        request_data_without_image = dict(request.data)
        request_data_without_image.pop('image', None)

        serializer = self.get_serializer(data=request_data_without_image)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        # Get the saved service instance
        service_instance = serializer.instance

        # Check if the image file is present before attempting to save it
        if image_data and isinstance(image_data, list):
            # Save the image separately
            service_instance.image.save(upload_to(service_instance, image_data[0].name), image_data[0])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ServiceGetAPIView(ListAPIView):
    serializer_class = ServiceCreateSerializer
    permission_classes = [ServicePermission]

    def get_queryset(self):
        user_id = self.request.user.id
        category_id = self.request.query_params.get('category_id')
        service_instances = Services.objects.filter(owner_id=user_id)

        if category_id:
            service_instances = service_instances.filter(category_id=category_id)
        if not service_instances.exists():
            raise Http404("Services not found")

        return service_instances

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


class ServiceOwnerGetAPIView(RetrieveAPIView):
    serializer_class = ServiceSerializer
    lookup_field = 'pk'

    def get_object(self):
        category_id = self.kwargs['pk']
        service = Services.objects.get(id=category_id)
        return service

    def retrieve(self, request, *args, **kwargs):
        service_instance = self.get_object()
        serializer = self.get_serializer(service_instance)

        owner = service_instance.owner
        owner_serializer = UserSerializer(owner)
        serialized_owner = owner_serializer.data

        combined_data = {
            'service': serializer.data,
            'owner': serialized_owner
        }

        return Response(combined_data)


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


class CategoryGetAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
