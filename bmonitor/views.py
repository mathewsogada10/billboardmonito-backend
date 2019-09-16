from django.shortcuts import render
from rest_framework import generics, mixins
from django.db.models import Q
from django.utils.timezone import get_current_timezone
from datetime import datetime, timedelta
from .serializers import MediaAgencySerializer, TownSerializer, ClientSerializer, BrandSerializer, BillBoardSerializer, ImageSerializer, CompetitorSerializer, UsersSerializer, BillBoardBrandSerializer, BrandAgencySerializer, BoardSupplierSerializer
from bmonitor.models import MediaAgency, Town, Client, Brand, BillBoard, Image, Competitor, Users, BillBoardBrand, BrandAgency, BoardSupplier
from django.utils import timezone
from django.http import JsonResponse
from rest_framework.decorators import APIView
from rest_framework.response import Response
# Create your views here.


class MediaAgencyPost(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = MediaAgencySerializer

    def get_queryset(self):
        return MediaAgency.objects.all()


class MediaAgencyViewOne(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = MediaAgencySerializer

    def get_queryset(self):
        return MediaAgency.objects.all()


class MediaAgencyViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = MediaAgencySerializer

    def get_queryset(self):
        query = MediaAgency.objects.all()
        param = self.request.GET.get("name")
        if param is not None:
            query = query.filter(Q(name__icontains=param))
        return query


class TownViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = TownSerializer

    def get_queryset(self):
        query = Town.objects.all()
        param = self.request.GET.get("name")
        if param is not None:
            query = query.filter(Q(name__icontains=param))
        return query


class ClientPost(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()


class ClientViewOne(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()


class ClientViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        query = Client.objects.all()
        paramName = self.request.GET.get('name')
        if paramName is not None:
            query = query.filter(Q(name__icontains=paramName))
        return query


class BrandPost(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = BrandSerializer

    def get_queryset(self):
        return Brand.objects.all()


class BrandViewOne(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = BrandSerializer

    def get_queryset(self):
        return Brand.objects.all()


class BrandViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        query = Brand.objects.all()
        paramClient = self.request.GET.get('client')
        paramAgency = self.request.GET.get('agency')
        if paramAgency is not None and paramClient is not None:
            brandAgency = BrandAgency.objects.filter(agency=paramAgency)
            query = query.filter(
                Q(client=paramClient, id__in=brandAgency.values_list('brand', flat=True))).distinct()
        elif paramClient is not None:
            query = query.filter(
                Q(client=paramClient)).distinct()
        return query


class BillBoardPost(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = BillBoardSerializer

    def get_queryset(self):
        return BillBoard.objects.all()


class BillBoardViewOne(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = BillBoardSerializer

    def get_queryset(self):
        return BillBoard.objects.all()


class BillBoardViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = BillBoardSerializer

    def get_queryset(self):
        query = BillBoard.objects.order_by('-id')
        paramBrand = self.request.GET.get('brand')
        if paramBrand is not None:
            brandAgency = BrandAgency.objects.get(
                brand=paramBrand, contract='ACTIVE')
            boardBrand = BillBoardBrand.objects.filter(
                brandAgency=brandAgency.id)
            query = query.filter(id__in=boardBrand.values_list(
                'billboard', flat=True)).distinct()
        return query


class ImagePost(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all()


class ImageViewOne(generics.RetrieveAPIView):
    lookup_field = 'description'
    serializer_class = ImageSerializer

    def get_queryset(self):
        return sel.Image.objects.all()


class ImageViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        query = Image.objects.all()
        tz = get_current_timezone()
        # dt = tz.localize(datetime.strptime(str_date, "%Y-%m-%d")) 2019-08-07 00:08:00'
        print(self.request.GET.get('endDate'))
        paramStartDate = tz.localize(datetime.strptime(
            self.request.GET.get('startDate'), "%Y-%m-%d"))
        paramEndDate = tz.localize(datetime.strptime(
            self.request.GET.get('endDate'), "%Y-%m-%d"))
        paramSupplier = self.request.GET.get('supplier')
        paramBrand = self.request.GET.get('brand')
        if paramBrand is not None and paramSupplier is not None:
            brandAgency = BrandAgency.objects.get(
                brand=paramBrand, contract="ACTIVE")
            boardBrand = BillBoardBrand.objects.filter(
                brandAgency=brandAgency.id)
            board = BillBoard.objects.filter(id__in=boardBrand.values_list(
                'billboard', flat=True), owner=paramSupplier)
            query = query.filter(
                dateCreated__gte=paramStartDate, dateCreated__lte=paramEndDate, board__in=board.values_list('id', flat=True))
            print(query)
        return query


class CompetitorPost(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = CompetitorSerializer

    def get_queryset(self):
        return Competitor.objects.all()

    def post(self, request, *args, **kwargs):
        compDict = self.request.data
        boardBrand = BillBoardBrand.objects.get(
            billboard=compDict["board"], brandAgency__contract="ACTIVE")
        compDict["boardBrand"] = boardBrand.id
        serializer = CompetitorSerializer(data=compDict)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class CompetitorViewOne(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = CompetitorSerializer

    def get_queryset(self):
        return Competitor.objects.all()


class CompetitorViewAll(mixins.CreateModelMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompetitorSerializer

    def get_queryset(self):
        query = Competitor.objects.all()
        paramBoard = self.request.GET.get('boardId')
        paramName = self.request.GET.get('name')
        if paramBoard is not None and paramName is not None:
            query = query.filter(
                Q(board=paramBoard, name__icontains=paramName))
        elif paramBoard is not None:
            query = query.filter(Q(board=paramBoard))
        elif paramName is not None:
            query = query.filter(Q(name__icontains=paramName))
        return query


class UserPost(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = UsersSerializer

    def get_queryset(self):
        return Users.objects.all()


class UserViewOne(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = UsersSerializer

    def get_queryset(self):
        return Users.objects.all()


class UserViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        query = Users.objects.all()
        authUserId = self.request.GET.get('id')
        if authUserId is not None:
            query = query.filter(Q(auth_user=authUserId))
        return query


class BillBoardBrandPost(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = BillBoardBrandSerializer

    def get_queryset(self):
        return BillBoardBrand.objects.all()

        bilbrdDict = self.request.data
        brdagency = BrandAgency.objects.get(
            brand=bilbrdDict['brandAgency'], contract='ACTIVE')
        bilbrdDict['brandAgency'] = brdagency.id
        serializer = BillBoardBrandSerializer(data=bilbrdDict)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class BillBoardBrandViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = BillBoardBrandSerializer

    def get_queryset(self):
        query = BillBoardBrand.objects.all()
        paramActive = self.request.GET.get('contract')
        paramBrand = self.request.GET.get('brandId')
        # paramboard = self.request.GET.get('boardId')
        if paramActive is not None and paramBrand is not None:
            query = query.filter(Q(brand=paramBrand, contract=paramActive))
        return query


class BrandAgencyPost(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = BrandAgencySerializer

    def get_queryset(self):
        return BrandAgency.objects.all()


class BrandAgencyViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = BrandAgencySerializer
   # serializer_class = serializers

    def get_queryset(self):
        query = BrandAgency.objects.all()
        # print(json.dumps(query))
        paramAgency = self.request.GET.get('agency')
        paramName = self.request.GET.get('name')
        if paramAgency is not None and paramName is not None:
            query = query.filter(Q(agency=paramAgency, brand__name=paramName))
        elif paramAgency is not None:
            query = query.filter(Q(agency=paramAgency))
        return query


class BoardSupplierViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = BoardSupplierSerializer

    def get_queryset(self):
        query = BoardSupplier.objects.all()
        return query
