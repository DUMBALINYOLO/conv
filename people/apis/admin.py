from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from people.models import (
					Student,
					StudentProfile,
					TeacherProfile,
					Teacher,
					Bursar,
					BursarProfile,
					Principal,
					PrincipalProfile,
					Parent,
					ParentProfile
				)
from people.serializers import (
						AdminPrincipalCreateUpdateSerializer,
						AdminTeacherSerializer,
						AdminBursarCreateSerializer,
						AdminPrincipalListDetailSerializer,
						AdminTeacherListDetailSerializer,
						AdminBursarListDetailSerializer,
						AdminParentListDetailSerializer,
						AdminStudentListDetailSerializer
					)


class CreateBursarAPI(generics.GenericAPIView):

	serializer_class = AdminBursarCreateSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response({
				"user": AdminBursarCreateSerializer(user, context=self.get_serializer_context()).data
			})



class CreatePrincipalAPI(generics.GenericAPIView):

	serializer_class = AdminPrincipalCreateUpdateSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response({
				"user": AdminBursarCreateSerializer(user, context=self.get_serializer_context()).data
			})




class CreateTeacherAPI(generics.GenericAPIView):

	serializer_class = AdminTeacherSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response({
				"user": AdminTeacherSerializer(user, context=self.get_serializer_context()).data
			})


class AdminStudentViewSet(viewsets.ModelViewSet):

	queryset = Student.objects.all()
	serializer_class = AdminStudentListDetailSerializer


class AdminPrincipalViewSet(viewsets.ModelViewSet):

	queryset = Principal.objects.all()
	serializer_class = AdminPrincipalListDetailSerializer


class AdminParentViewSet(viewsets.ModelViewSet):

	queryset = Parent.objects.all()
	serializer_class = AdminParentListDetailSerializer


class AdminTeacherViewSet(viewsets.ModelViewSet):

	queryset = Teacher.objects.all()
	serializer_class = AdminTeacherListDetailSerializer


class AdminBursarViewSet(viewsets.ModelViewSet):

	queryset = Bursar.objects.all()
	serializer_class = AdminBursarListDetailSerializer

