from rest_framework.routers import DefaultRouter
from people.apis import (
				CreateStudentAPI,
				CreateBursarAPI,
				CreatePrincipalAPI,
				CreateTeacherAPI,
				AdminStudentViewSet,
				AdminPrincipalViewSet,
				AdminParentViewSet,
				AdminTeacherViewSet,
				AdminBursarViewSet,
				BursarStudentViewSet,
				BursarParentViewSet,
			)
from django.urls import path

router = DefaultRouter()

router.register('admin-students', AdminStudentViewSet, basename='admin-students')
router.register('admin-principals', AdminPrincipalViewSet, basename='admin-principals')
router.register('admin-teachers', AdminTeacherViewSet, basename='admin-teachers')
router.register('admin-bursars', AdminBursarViewSet, basename='admin-bursars')
router.register('admin-parents', AdminParentViewSet, basename='admin-parents')
router.register('bursar-parents', BursarParentViewSet, basename='bursar-parents')
router.register('bursar-students', BursarStudentViewSet, basename='bursar-students')


urlpatterns = [
	path('create-student', CreateStudentAPI.as_view()),
	path('create-bursar', CreateBursarAPI.as_view()),
	path('create-principal', CreatePrincipalAPI.as_view()),
	path('create-teacher', CreateTeacherAPI.as_view()),
] + router.urls




