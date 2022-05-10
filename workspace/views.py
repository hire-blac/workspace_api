from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import viewsets
from workspace.models import BookedDay, Booking, Plan, Space
from .serializers import BookedDaySerializer, BookingSerializer, PlanSerializer, SpaceSerializer


# Create your views here.
class SpaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allows spaces to be viewed or edited
    """
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

class PlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allows plans to be viewed or edited
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allows bookings to be viewed or edited
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookedDayViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allows bookings to be viewed or edited
    """
    queryset = BookedDay.objects.all()
    serializer_class = BookedDaySerializer


class SpaceList(APIView):
    # List all Spaces or create a new Space
    def get(self, request, format=None):
        spaces = Space.objects.all()
        serializer = SpaceSerializer(spaces, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpaceDetail(APIView):
    # retrieve, update or delet a Space instance
    def get_object(self, slug):
        try:
            return Space.objects.get(slug=slug)
        except Space.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        space = self.get_object(slug=slug)
        serializer = SpaceSerializer(space)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        space = self.get_object(slug=slug)
        serializer = SpaceSerializer(space, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        space = self.get_object(slug=slug)
        space.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlanList(APIView):
    # List all plans or create a new plans
    def get(self, request, format=None):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanDetail(APIView):
    # retrieve, update or delet a Space instance
    def get_object(self, slug):
        try:
            return Plan.objects.get(slug=slug)
        except Plan.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        plan = self.get_object(slug=slug)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        plan = self.get_object(slug=slug)
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        plan = self.get_object(slug=slug)
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookingList(APIView):
    # List all bookings or create a new bookings
    def get(self, request, format=None):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetail(APIView):
    # retrieve, update or delet a booking instance
    def get_object(self, slug):
        try:
            return Booking.objects.get(slug=slug)
        except Booking.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        plan = self.get_object(slug=slug)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        plan = self.get_object(slug=slug)
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        plan = self.get_object(slug=slug)
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
