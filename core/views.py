from core.models import Language
from core.serializers import LanguageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ListLanguages(APIView):

    def get(self, request):
        languages = Language.scan()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)
