from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
course_resource = CourseResource()
category_resourse = CategoryResource()
api.register(course_resource)
api.register(category_resourse)

urlpatterns = [
    path('', include(api.urls))
]
