# your_app/views/course_views.py

from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..services.course_service import CourseService
from ..models import Course
import json
import uuid


@method_decorator(csrf_exempt, name='dispatch')
class CourseController(View):

    def temp(self):
        return JsonResponse("hihi", safe=False)

    def get(self, request, course_id=None):
        print('exists' if course_id else 'not exists')
        if course_id:
            try:
                course_uuid = uuid.UUID(course_id)
                course = CourseService.get_course(course_uuid)
                return JsonResponse(course, safe=False)
            except (ValueError, Course.DoesNotExist):
                return JsonResponse({'error': 'Course not found'}, status=404)
        else:
            courses = CourseService.get_all_courses()
            #print(courses)
            return JsonResponse(courses, safe=False)

    def post(self, request):
        print('exists' if request else 'not exists')
        data = json.loads(request.body)
        name = data.get('name')
        code = data.get('code')
        pre_requisites = data.get('pre_requisites', [])

        if not name or not code:
            return JsonResponse({'error': 'Name and code are required'}, status=400)

        course = CourseService.create_course(name, code, pre_requisites)

        return JsonResponse({
            'id': str(course._id),
            'name': course.name,
            'code': course.code,
            'pre_requisites': course.pre_requisites
        }, status=201)

    def put(self, request, course_id):
        print(course_id)
        data = json.loads(request.body)
        name = data.get('name')
        code = data.get('code')
        pre_requisites = data.get('pre_requisites')

        try:
            course_uuid = uuid.UUID(course_id)
            course = CourseService.update_course(course_uuid, name, pre_requisites)
            if code:
                course.code = code
                course.save()
            return JsonResponse({
                'id': str(course._id),
                'name': course.name,
                'code': course.code,
                'pre_requisites': course.pre_requisites
            })
        except (ValueError, Course.DoesNotExist):
            return JsonResponse({'error': 'Course not found'}, status=404)

    def delete(self, request, course_id):
        try:
            course_uuid = uuid.UUID(course_id)
            CourseService.delete_course(course_uuid)
            return JsonResponse({'message': 'Course deleted successfully'})
        except (ValueError, Course.DoesNotExist):
            return JsonResponse({'error': 'Course not found'}, status=404)
