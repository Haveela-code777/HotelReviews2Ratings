from django.http import HttpResponse
from .models import Review
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import ReviewCreateSerializer
from hotelapp.models import Hotel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# Create your views here.

def test(request):
    return HttpResponse("Neutral")

def sentiment_analysis(sentence):
    # sentence = "Nice loved it. Nice maintainence"
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    print("Sentence Overall Rated As", end = " ")
    formula_flag = 0
    if sentiment_dict['compound'] >= 0.05 :
        # 0.05 - 1
        min = 0.05
        max = 1
        rating_min = 2.5
        rating_max = 5
        formula_flag = 1
 
    elif sentiment_dict['compound'] <= - 0.05 :
        # -1 to -0.05
        min = -1
        max = -0.05
        rating_min = 1
        rating_max = 2.5
        formula_flag = 1
 
    else :
        rating_value = 2.5

    if formula_flag==1:
        sent_Range = (max - min)  
        rating_Range = (rating_max - rating_min)  
        rating_value = (((sentiment_dict['compound'] - min) * rating_Range) / sent_Range) + rating_min      

    return "%.1f" % rating_value
    # return HttpResponse("%.1f" % rating_value)

@api_view(['POST'])
def create_review(request):
    try:
        if request.method=="POST":
            data=request.data
            # JSON data
            # {
            #     "review" : "Nice hotel",
            #     "name" : "Kamal",
            #     "email" : "karrekamal10@gmail.com",
            #     "hotel" : 2
            # }
            # {
            #     "review" : "Nice hotel",
            #     "name" : "Kamal",
            #     "email" : "karrekamal10@gmail.com"
            # }
            hotel_id_ = data["hotel"]
            del data["hotel"]
            hotel_objs= Hotel.objects.filter(id=hotel_id_)
            if hotel_objs.count():
                hotel_obj = hotel_objs[0]
            else:
                return Response({"message":"No Hotel data found"},status=status.HTTP_404_NOT_FOUND)
            rating_ = sentiment_analysis(data["review"])
            serializer = ReviewCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save(hotel=hotel_obj,rating=rating_)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def retrieve_hotel_reviews(request):
    try:
        if request.method=="GET":
            if "hotel_id" in request.GET:
                # 1st method
                # hotel_objs=Hotel.objects.filter(id=2)
                # if hotel_objs.count():
                #     hotel_obj = hotel_objs[0]
                #     review_objs = Review.objects.filter(hotel=hotel_obj)
                # 2nd method
                review_objs = Review.objects.filter(hotel__id=request.GET["hotel_id"])
                serializer = ReviewCreateSerializer(review_objs,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({"message":"Parameter hotel_id is required"},status=status.HTTP_400_BAD_REQUEST)        
    except Exception as e:
        return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)