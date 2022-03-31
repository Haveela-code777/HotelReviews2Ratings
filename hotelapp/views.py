from django.http import HttpResponse
from .models import Hotel
from .serializer import HotelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def test(request):
    return HttpResponse("hello")
   
# CRUD APIs
@api_view(['POST'])
def create_hotel(request):
    if request.method == "POST":
        # json = {
        #     "name" : "hotel name",
        #     "location" : "hotel location",
        #     "image" : "Upload media image"
        # }

        # request.POST --> for text
        # request.FILES --> for file
        
        data = request.data
        # Without Serializer 
        # Hotel.objects.create(name=data["name"],location=data["location"],image=request.FILES['image'])
        # With Serializer
        serializer = HotelSerializer(data=data)
        if serializer.is_valid():
            # serializer.save(image=request.FILES['image'])
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def retrieve_hotel(request):
    try:
        if request.method=="GET":
            if "id" in request.GET:
                hotel_objs = Hotel.objects.filter(id=request.GET["id"])
                if hotel_objs.count():
                    serializer = HotelSerializer(hotel_objs.first())
                else:
                    return Response({"message":"No Hotel data found"},status=status.HTTP_404_NOT_FOUND)
            else:
                hotel_objs = Hotel.objects.all()
                serializer = HotelSerializer(hotel_objs,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_hotel(request,*args,**kwargs):
    try:
        if request.method=='PUT':
            hotel_objs = Hotel.objects.filter(id=kwargs["hotel_id"])
            if hotel_objs.count():
                data = request.data
                hotel_obj = hotel_objs[0]
                serializer = HotelSerializer(hotel_obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"message":"No Hotel data found"},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_hotel(request,*args,**kwargs):
    try:
        if request.method=='DELETE':
            hotel_objs=Hotel.objects.filter(id=kwargs["id"])
            if hotel_objs.count():
                # hotel_obj=hotel_objs[0]
                hotel_objs.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)        

# class HotelCRUDAPI(APIView):
#     def get(self,request):
#         pass
#     def post(self,request):
#         pass
#     def update(self,request):
#         pass
#     def delete(self,request):
#         pass