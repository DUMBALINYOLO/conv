from rest_framework import serializers
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

from attendance.models import AttendanceRecord
from django.contrib.auth import authenticate


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class AdminStudentProfileCreateUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudentProfile
		fields = [
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'guardian',
			'gender',
			'guardian',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',

		]

class AdminParentProfileCreateUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = ParentProfile
		fields = [
			'title',
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',

		]


class AdminBursarProfileCreateUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = BursarProfile
		fields = [
			'title',
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',

		]


class AdminTeacherProfileCreateUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = TeacherProfile
		fields = [
			'title',
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',

		]


class AdminPrincipalCreateUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = PrincipalProfile
		fields = [
			'title',
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',

		]



class AdminStudentProfileListDetailSerializer(serializers.ModelSerializer):
	guardian = StringSerializer()
	gender = serializers.SerializerMethodField()

	class Meta:
		model = StudentProfile
		fields = [
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'guardian',
			'gender',
			'guardian',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',
		]

	def get_gender(self, obj):
		return obj.get_gender_display()

class AdminParentProfileListDetailSerializer(serializers.ModelSerializer):
	gender = serializers.SerializerMethodField()
	title  = serializers.SerializerMethodField()

	class Meta:
		model = ParentProfile
		fields = [
			'title',
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',

		]

	def get_gender(self, obj):
		return obj.get_gender_display()

	def get_title(self, obj):
		return obj.get_title_display()


class AdminBursarProfileListDetailSerializer(serializers.ModelSerializer):
	gender = serializers.SerializerMethodField()
	title  = serializers.SerializerMethodField()

	class Meta:
		model = BursarProfile
		fields = [
			'title',
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',

		]

	def get_gender(self, obj):
		return obj.get_gender_display()

	def get_title(self, obj):
		return obj.get_title_display()


class AdminTeacherProfileListDetailUpdateSerializer(serializers.ModelSerializer):
	gender = serializers.SerializerMethodField()
	title  = serializers.SerializerMethodField()

	class Meta:
		model = TeacherProfile
		fields = [
			'title',
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',

		]

	def get_gender(self, obj):
		return obj.get_gender_display()

	def get_title(self, obj):
		return obj.get_title_display()


class AdminPrincipalProfileListDetailSerializer(serializers.ModelSerializer):
	gender = serializers.SerializerMethodField()
	title  = serializers.SerializerMethodField()

	class Meta:
		model = PrincipalProfile
		fields = [
			'title',
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			# 'date_of_birth',
			'phone_number',
			'whatsapp_number',

		]

	def get_gender(self, obj):
		return obj.get_gender_display()

	def get_title(self, obj):
		return obj.get_title_display()


class AdminPrincipalCreateUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Principal
		fields = ['id', 'email', 'username', 'password']
		extra_kwargs = {'password':{"write_only": True}}


	def create(self, validated_data):
		principal = Principal.objects.create_principal(
				validated_data['email'],
				validated_data['username'],
				validated_data['password'],

			)
		return principal


class AdminTeacherSerializer(serializers.ModelSerializer):

	class Meta:
		model = Teacher
		fields = ['id', 'email', 'username', 'password']
		extra_kwargs = {'password':{"write_only": True}}


	def create(self, validated_data):
		teacher = Teacher.objects.create_teacher(
				validated_data['email'],
				validated_data['username'],
				validated_data['password'],

			)
		return teacher

class AdminBursarCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Bursar
		fields = ['id', 'email', 'username', 'password']
		extra_kwargs = {'password':{"write_only": True}}


	def create(self, validated_data):
		bursar = Bursar.objects.create_bursar(
				validated_data['email'],
				validated_data['username'],
				validated_data['password'],

			)
		return bursar




class AdminPrincipalListDetailSerializer(serializers.ModelSerializer):
	profile = AdminPrincipalProfileListDetailSerializer()

	class Meta:
		model = Principal
		fields = [
			'id',
			'username',
			'email',
			'profile',
		]


class AdminTeacherListDetailSerializer(serializers.ModelSerializer):
	profile = AdminTeacherProfileListDetailUpdateSerializer()

	class Meta:
		model = Teacher
		fields = [
			'id',
			'username',
			'email',
			'profile',
		]


class AdminBursarListDetailSerializer(serializers.ModelSerializer):
	profile = AdminBursarProfileListDetailSerializer()

	class Meta:
		model = Bursar
		fields = [
			'id',
			'username',
			'email',
			'profile',
		]



class AdminParentListDetailSerializer(serializers.ModelSerializer):
	profile = AdminParentProfileListDetailSerializer()

	class Meta:
		model = Principal
		fields = [
			'id',
			'username',
			'email',
			'profile',
		]


class AttendanceSerializer(serializers.ModelSerializer):
	attendance = StringSerializer()

	class Meta:
		model = AttendanceRecord
		fields = [
				'id',
				'attendance',
				'status',
			]


class AdminStudentListDetailSerializer(serializers.ModelSerializer):
	attendance = AttendanceSerializer(many=True)
	profile = AdminStudentProfileListDetailSerializer()


	class Meta:
		model = Student
		fields = [
				'id',
				'username',
				'email',
				'profile',
				'attendance',
			]