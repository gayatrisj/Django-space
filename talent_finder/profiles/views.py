# profiles/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
import requests

@api_view(['GET'])
def get_user_profile(request, name):
    try:
        linkedin_profile = requests.get(f'https://api.linkedin.com/v2/people/(name:{name})').json()
        leetcode_profile = requests.get(f'https://leetcode.com/api/profile/{name}').json()
        hackerrank_profile = requests.get(f'https://www.hackerrank.com/rest/contests/master/hackers/{name}/profile').json()
        gfg_profile = requests.get(f'https://auth.geeksforgeeks.org/user/{name}/').json()

        user_profile = UserProfile.objects.create(
            name=name,
            linkedin=linkedin_profile,
            leetcode=leetcode_profile,
            hackerrank=hackerrank_profile,
            gfg=gfg_profile
        )
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
