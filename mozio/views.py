from rest_framework.views import APIView
from mozio.helpers.json_response import JSONResponse
from rest_framework import status
from serializers import ProvidersSerializer, ServiceAreaSerializer
from rest_framework.parsers import JSONParser
from models import Providers as ProviderModel
from models import ServiceArea
from django.http import Http404
from rest_framework.response import Response

class ProviderList(APIView):

    model=ProviderModel
    serializer_class = ProvidersSerializer

    def get(self, request):
        """
        Get Providers details

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            name:
                required: true
                type: string
            email:
                required: true
                type: string
            phone_number:
                required: true
                type: string
            language:
                required: true
                type: string
            currency:
                required: true
                type: string

        response_serializer: ProvidersSerializer
        
        serializer: ProvidersSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 200
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """

        providers = ProviderModel.objects.all()
        serializer = ProvidersSerializer(providers, many=True)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Post Providers details

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            name:
                required: true
                type: string
            email:
                required: true
                type: string
            phone_number:
                required: true
                type: string
            language:
                required: true
                type: string
            currency:
                required: true
                type: string

        serializer: ProvidersSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 200
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """
        data = JSONParser().parse(request)
        serializer = ProvidersSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)




class ProviderDetail(APIView):

    model=ProviderModel
    serializer_class = ProvidersSerializer

    def get_object(self, pk):
        try:
            return ProviderModel.objects.get(pk=pk)
        except ProviderModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Get Providers details

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            name:
                required: true
                type: string
            email:
                required: true
                type: string
            phone_number:
                required: true
                type: string
            language:
                required: true
                type: string
            currency:
                required: true
                type: string

        serializer: ProvidersSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 200
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """

        provider = self.get_object(pk)
        serializer = ProvidersSerializer(provider)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        """
        Update Providers details

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            name:
                required: true
                type: string
            email:
                required: true
                type: string
            phone_number:
                required: true
                type: string
            language:
                required: true
                type: string
            currency:
                required: true
                type: string

        serializer: ProvidersSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 200
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """
        provider = self.get_object(pk)
        serializer = ProvidersSerializer(provider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete Provider

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            id:
                required: true
                type: string


        serializer: ProvidersSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 200
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """
        provider = self.get_object(pk)
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ServiceAreaList(APIView):

    model=ServiceArea
    serializer_class = ServiceAreaSerializer

    def get_object(self, pk):
        try:
            return ProviderModel.objects.get(pk=pk)
        except ProviderModel.DoesNotExist:
            raise Http404

    def get(self, request):
        """
        Get All ServiceAreaList details

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        serializer: ServiceAreaSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 200
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """
        service_areas = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(service_areas, many=True)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create ServiceArea details

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            name:
                required: true
                type: string
            price:
                required: true
                type: float
            loc:
                required: true
                type: string
            provider:
                required: true
                type: string

        serializer: ServiceAreaSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 400
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """
        data = JSONParser().parse(request)
        data["name"] = data.get("loc",{}).get("properties", "").get("name", "")
        data["price"] = data.get("loc",{}).get("properties", "").get("price", "")
        serializer = ServiceAreaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

class ServiceAreaDetail(APIView):

    model=ServiceArea
    serializer_class = ServiceAreaSerializer

    def get_object(self, pk):
        try:
            return ServiceArea.objects.get(pk=pk)
        except ProviderModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Get Providers details

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            id:
                required: true
                type: string

        serializer: ServiceAreaSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 200
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """
        service_area = self.get_object(pk)
        serializer = ServiceAreaSerializer(service_area)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update ServiceArea detail

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            name:
                required: true
                type: string
            price:
                required: true
                type: float
            loc:
                required: true
                type: string
            provider:
                required: true
                type: string

        serializer: ServiceAreaSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 400
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """
        service_area = self.get_object(pk)
        request.data["name"] = request.data.get("loc",{}).get("properties", "").get("name", "")
        request.data["price"] = request.data.get("loc",{}).get("properties", "").get("price", "")
        serializer = ServiceAreaSerializer(service_area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete ServiceArea details

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            id:
                required: true
                type: string

        serializer: ServiceAreaSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 400
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """
        service_area = self.get_object(pk)
        service_area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BatchGetServiceArea(APIView):

    model=ServiceArea
    serializer_class = ServiceAreaSerializer

    def post(self, request):
        """
        Get Multiple ServiceArea detail

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            ids:
                required: true
                type: list

        serializer: ServiceAreaSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessages:
            - code: 400
              message: Invalid Params
            - code: 200
              message: Successfully fetches the record
        """
        service_area_ids = request.data.get("ids","")
        if not service_area_ids or not isinstance(service_area_ids, list):
            return JSONResponse({"error": "Invaid Params"}, status=status.HTTP_400_BAD_REQUEST)
        service_areas = ServiceArea.objects.filter(id__in=service_area_ids)
        serializer = ServiceAreaSerializer(service_areas, many=True)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)

class FindServiceArea(APIView):


    def get(self, request):

        """
        Find ServiceArea based in Latitude and Longitude

        :param request:
        :return:
        ---
        # YAML (must be separated by `---`)

        type:
            lat:
                required: true
                type: float
            long:
                required: true
                type: float

        serializer: ServiceAreaSerializer
        omit_serializer: false

        parameters_strategy: merge
        omit_parameters:
            - path

        responseMessage:
            - code: 400
              message: Invalid Params
            - code: 201
              message: Successfully fetches the record
        """

        latitude = request.data.get('lat','')
        longitude = request.data.get('long','')
        result=[]
        service_area_objs = ServiceArea.objects.filter(loc__geo_intersects=[latitude, longitude])
        for service_area in service_area_objs:
            result.append({"polygon_name": service_area.name, "provider_name": service_area.provider.name,
                           "price": service_area.price})
        return JSONResponse(result, status=status.HTTP_200_OK)





