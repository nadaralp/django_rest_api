from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

# Now using third party imports rest API frameswork
# What you will return, inheriting from JsonResponse of django's framework
from rest_framework.response import Response
# This is one of their wrappers that allows you to build GET/POST request
from rest_framework.views import APIView

# Work with serializer 
from .serializers import PostSerializer
from .models import Post

# We want to understand how to work with POST request and GET request, we need to make sure that the format matches the data schema.
# All fields need to be included in the request ( the fields that are given on the serializers configuration)
# We check if the data is a valid request

# We need to create a class -> because the APIview is something we can inherit in our own classes


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        # this is what we use to handle when someone sends a get request for this endpoint
        # and we use the Response to send a response
        data = {
            "first_name": "Nadar",
            "last_name": "Alpenidze",
            "Age": 22
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        # Checking if valid
        if serializer.is_valid():
            # Before we save we need to check if the form received in the serializer is valid - just like we do in a form
            serializer.save()
            # We want to see what data what has been created for example, 201 success status
            return Response(serializer.data)

        # returns the errors
        return Response(serializer.errors)

class SerialzerView():
    pass


# def test_view(request):
#     # return render(request, "template.location.html")

#     # JSON response is accepting a dictionary,
#     # but if you want to pass something else you can set the list=False in the variables
#     data = {
#         "first_name": "Nadar",
#         "last_name": "Alpenidze",
#         "Age": 22
#     }
#     return JsonResponse(data)