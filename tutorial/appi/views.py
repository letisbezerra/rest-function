from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from appi.models import Appi
from appi.serializers import AppiSerializer


@api_view(['GET', 'POST'])
def appi_list(request):
    if request.method == 'GET':
        appi = Appi.objects.all()
        serializer = AppiSerializer(appi, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AppiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response
        return Response(serializer.erros, status=)
    
class AppiDetail(APIView):
    def get_object(request, pk):
        try:
            return Appi.objects.get(pk=pk)
        except Appi.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        appi = self.get_object(pk)
        serializer = AppiSerializer(appi)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        appi = self.get_object(pk)
        serializer = AppiSerializer(appi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        appi = self.get_object(pk)
        appi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



