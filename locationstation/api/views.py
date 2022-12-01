from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from .serializers import OutCodeSerializer, NexusSerializer
from django.db.models import Avg, Count
from .models import Listing
import requests
from geopy.distance import great_circle

custom_xml_renderer = XMLRenderer
custom_xml_renderer.item_tag_name = 'outcode'
custom_xml_renderer.root_tag_name = 'outcodes'

class OutcodeView(APIView):
    parser_classes = (XMLParser,)
    renderer_classes = (custom_xml_renderer,)

    def get(self, request, outcode):
        """
        returns nunber of listings in a given outcode 
        and average price
        """
        response = requests.get(f"https://api.postcodes.io/outcodes/{outcode}")
        if response.status_code == 404:
            return Response([],status=status.HTTP_404_NOT_FOUND)
        data = response.json()
        admin_districts = data.get('result').get('admin_district')
        admin_wards = data.get('result').get('admin_ward')
        query = Listing.objects.filter(
            neighbourhood_group__in=admin_districts,
            neighbourhood__in=admin_wards,

        ).aggregate(Avg('price'),Count('price'))
        # if not data avilable in listings for admin_districts return 404
        if not query.get('price__count'):
            return Response([],status=status.HTTP_404_NOT_FOUND)
        serializer = OutCodeSerializer(query)
        return Response(serializer.data)


class NexusView(APIView):
    parser_classes = (XMLParser,)
    renderer_classes = (custom_xml_renderer,)

    def get(self, request, outcode):
        """
        returns nearest outcodes for a given nexus code
        """
        response = requests.get(f"https://api.postcodes.io/outcodes/{outcode}/nearest/")
        if response.status_code == 404:
            return Response([],status=status.HTTP_404_NOT_FOUND)
        data = response.json().get('result')
        admin_districts = data[0].get('admin_district')
        admin_wards = data[0].get('admin_ward')
        start_coords =  (data[0].get('latitude'),data[0].get('longitude'))
        outcodes = []
        query = Listing.objects.filter(
            neighbourhood_group__in=admin_districts,
            neighbourhood__in=admin_wards,

        )
        root_query_agg = query.aggregate(Avg('price'),Count('price'))
        # if not data avilable in listings for admin_districts return 404
        if not root_query_agg.get('price__count'):
            return Response([],status=status.HTTP_404_NOT_FOUND)
        for outcode_data in data[1:]:
            admin_districts = outcode_data.get('admin_district')
            admin_wards = outcode_data.get('admin_ward')
            end_coords = (outcode_data.get('latitude'),outcode_data.get('longitude'))
            distance = great_circle(start_coords, end_coords).miles
            query = Listing.objects.filter(
                neighbourhood_group__in=admin_districts,
                neighbourhood__in=admin_wards,
            )
            query_agg = query.aggregate(Avg('price'),Count('price'))
            if query_agg.get('price__count'):
                query_agg.update(
                    {'distance':distance,'code':outcode_data.get('outcode')}
                )
                outcodes.append(query_agg)

        root_query_agg.update({'outcodes':outcodes,'nexus_outcode':outcode})
        serializer = NexusSerializer(root_query_agg)
        return Response(serializer.data)

