# your_app/services/course_service.py

import json
from ..models import Course

class CourseService:

    @staticmethod
    def is_prerequisite(course_id):
        result = False
        all_course = Course.objects.all();
        for course in all_course:
            if str(course_id) in course.pre_requisites:
                result = True
        return result
    @staticmethod
    def get_prerequisites(course_id, processed_courses = None):
        if(processed_courses is None):
            processed_courses = set()
        try:
            course = Course.objects.get(_id = course_id)
            if( str(course_id) in processed_courses):
                return {
                    'id': str(course_id),
                    'name': course.name,
                    'code': course.code
                }
            processed_courses.add(str(course_id))

            course_dict = {
                'id': str(course._id),
                'name': course.name,
                'code': course.code,
                'pre_requisites': []
            }

            for pre_req_id in course.pre_requisites:
                pre_req = CourseService.get_prerequisites(pre_req_id, processed_courses)
                if pre_req:
                    course_dict['pre_requisites'].append(pre_req)

            return course_dict
        except Course.DoesNotExist:
            return None

    @staticmethod
    def create_course(name, pre_requisites):
        print(name, type(pre_requisites))
        # if pre_requisites == [] or pre_requisites is None:
        #     pre_requisites = '[]'
        # else:
        #     pre_requisites = json.dumps(pre_requisites)
        course = Course(name=name, pre_requisites=pre_requisites)
        print('221')
        course.save()
        print('222')
        return course

    @staticmethod
    def get_course(course_id):
        course = Course.objects.get(_id=course_id)
        return CourseService.get_prerequisites(course._id)

    @staticmethod
    def get_all_courses():
        courses = Course.objects.all()
        filter_course = [x for x in courses if not CourseService.is_prerequisite(x._id) ]
        return [CourseService.get_prerequisites(course._id) for course in filter_course]


    @staticmethod
    def update_course(course_id, name=None, pre_requisites=None):
        print("3453")
        course = Course.objects.get(_id=course_id)
        print(course)
        if name:
            course.name = name
        if pre_requisites is not None:
            course.pre_requisites = pre_requisites
        course.save()
        return course

    @staticmethod
    def delete_course(course_id):
        course = Course.objects.get(_id=course_id)
        course.delete()
