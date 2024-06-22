from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserScore
from .serializers import UserScoreSerializer

@api_view(['POST'])
def add_user_score(request):
    if request.method == 'POST':
        serializer = UserScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user_score(request, username):
    try:
        user_score = UserScore.objects.get(username=username)
    except UserScore.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserScoreSerializer(user_score, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def top_10_users(request):
    users = UserScore.objects.all().order_by('-total_score')[:10]
    serializer = UserScoreSerializer(users, many=True)
    return Response(serializer.data)
