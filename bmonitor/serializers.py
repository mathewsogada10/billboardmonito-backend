from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.db.models import Q
from bmonitor.models import MediaAgency, Client, Town, Brand, BillBoard, Image, Competitor, Users, BillBoardBrand, BrandAgency, BoardSupplier


class MediaAgencySerializer(serializers.ModelSerializer):
    clients = serializers.SerializerMethodField('getClients')

    class Meta:
        model = MediaAgency
        fields = [
            'id',
            'name',
            'dateCreated',
            'lastUpdate',
            'town',
            'location',
            'clients'
        ]
        read_only_fields = ['id', 'dateCreated']

    def getClients(self, obj):
        # brnds = BrandAgency.objects.all().select_related('agency').select_related('brand')..select_related('client')
        brndAgency = BrandAgency.objects.filter(agency=obj.id)
        brnd = Brand.objects.filter(
            id__in=brndAgency.values_list('brand', flat=True))
        clients = Client.objects.filter(
            id__in=brnd.values_list('client', flat=True))
        ser = ClientSerializer(clients, many=True, read_only=True)
        return ser.data


class ClientSerializer(serializers.ModelSerializer):
    boards = serializers.SerializerMethodField('getBillboards')

    class Meta:
        model = Client
        fields = [
            'id',
            'dateCreated',
            'lastUpdate',
            'name',
            'town',
            'location',
            'boards'
        ]

        read_only_fields = ['id', 'dateCreated']

    def getBillboards(self, obj):
        brand = Brand.objects.filter(client=obj.id)
        brndAgency = BrandAgency.objects.filter(
            brand__in=brand.values_list('id', flat=True))
        billBoardBrand = BillBoardBrand.objects.filter(
            brandAgency__in=brndAgency.values_list('id', flat=True))
        billBoards = BillBoard.objects.filter(
            id__in=billBoardBrand.values_list('billboard', flat=True))
        ser = BillBoardSerializer(billBoards, many=True, read_only=True)
        return ser.data


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = [
            'id',
            'name',
            'dateCreated'
        ]

        read_only_fields = ['id', 'dateCreated']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'description',
            'dateCreated',
            'lastUpdate',
            'client',
        ]
        read_only_fields = ['id', 'dateCreated']


class BillBoardSerializer(serializers.ModelSerializer):
    competitors = serializers.SerializerMethodField('getCompetitors')

    class Meta:
        model = BillBoard
        fields = [
            'id',
            'description',
            'boardType',
            'latittude',
            'longitude',
            'owner',
            'dateCreated',
            'lastUpdate',
            'state',
            'street',
            'competitors'
        ]

        read_only_fields = ['id', 'dateCreated']

    def getCompetitors(self, obj):
        boardBrand = BillBoardBrand.objects.filter(
            billboard=obj.id, brandAgency__contract="ACTIVE")
        competitors = Competitor.objects.filter(boardBrand__in=boardBrand.values_list("id",flat=True))
        ser = CompetitorSerializer(competitors, many=True, read_only=True)
        return ser.data


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'description',
            'fileContent',
            'dateCreated',
            'board'
        ]
        read_only_fields = ['id', 'dateCreated']


class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = [
            'id',
            'name',
            'description',
            'distance',
            'avInShops',
            'boardBrand',
            'dateCreated',
            'lastUpdate'
        ]
        read_only_fields = ['id', 'dateCreated']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ['id', 'dateCreated']


class BillBoardBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillBoardBrand
        fields = [
            'id',
            'brandAgency',
            'dateCreated',
            'lastUpdate',
            'billboard',
            'recommendation'
        ]
        read_only_fields = ['id', 'dateCreated']


class BrandAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandAgency
        fields = [
            'id',
            'brand',
            'agency',
            'dateCreated',
            'lastUpdate',
            'contract'
        ]
        read_only_fields = ['id', 'dateCreated']


class BoardSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardSupplier
        fields = '__all__'

        read_only_fields = ['id', 'dateCreated']
