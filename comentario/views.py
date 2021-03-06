from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions, parsers, renderers, status

from models import *
from serializers import *

# Create your views here.
class ComentarioViewSet(viewsets.ModelViewSet):
	serializer_class = ComentairoSerializer

	def get_queryset(self):
		queryset = Comentario.objects.all().order_by('-pk')
		producto = self.request.query_params.get('producto', None)
		if producto is not None:
			queryset = Comentario.objects.filter(producto=producto).order_by('-pk')
		return queryset

	def create(self, request):
		print request.data
		if request.user.is_authenticated:
			request.data['usuario'] = request.user.pk
		serializer = ComentairoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComentarioImagenViewSet(viewsets.ModelViewSet):
	serializer_class = ComentarioImagenSerializer
	queryset = ComentarioImagen.objects.all()
	