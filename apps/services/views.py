from django.http import Http404
from rest_framework import status, request
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from apps.services.models import Services, upload_to, Category
from apps.services.permissions import ServicePermission
from apps.services.serializers import ServiceCreateSerializer, CategorySerializer, ServiceSerializer
from apps.users.models import User
from apps.users.serializers import UserSerializer


class ServiceCreateAPIView(CreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [ServicePermission]

    def perform_create(self, serializer):
        # Set the owner of the service to the current authenticated user
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        # Extract the image data from the request
        image_data = request.data.get('image')

        # Create a dictionary containing the request data excluding the image
        request_data_without_image = dict(request.data)
        request_data_without_image.pop('image', None)

        # Create a serializer instance with the data excluding the image
        serializer = self.get_serializer(data=request_data_without_image)
        serializer.is_valid(raise_exception=True)

        # Save the service without the image
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


class CategoryGetAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
