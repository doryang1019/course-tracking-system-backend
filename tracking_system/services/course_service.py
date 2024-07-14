# your_app/services/course_service.py

import json
from ..models import Course

class CourseService:

    @staticmethod
    def has_child(course_id):
        result = False
        course = Course.objects.get(_id = course_id)
        if len(list(course.pre_requisites)) != 0:
            result = True
        return result
    @staticmethod
    def is_prerequisite(course_id):
        result = False
        all_course = Course.objects.all();
        for course in all_course:
            if str(course_id) in course.pre_requisites:
                result = True
        return result

    @staticmethod
    def get_course_dict(course):
        return {
            'id': str(course._id),
            'code': course.code,
            'title': course.name,
            'childIds': [str(pre_req_id) for pre_req_id in course.pre_requisites]
        }

    @staticmethod
    def get_all_courses():
        courses = Course.objects.all()
        course_dict = {str(course._id): CourseService.get_course_dict(course) for course in courses}
        print(course_dict)
        def build_tree(course_id, visited=None):
            if visited is None:
                visited = set()

            if course_id in visited:
                return None

            visited.add(course_id)
            course = course_dict.get(course_id)

            if not course:
                return None

            tree = [course]

            for pre_req_id in course['childIds']:
                pre_req_tree = build_tree(pre_req_id, visited.copy())
                if pre_req_tree:
                    tree.extend(pre_req_tree)

            return tree

        # Find root courses (courses that are not prerequisites of any other course)
        # all_prerequisites = set(pre_req_id for course in course_dict.values() for pre_req_id in course['childIds'])
        # root_courses = [course_id for course_id in course_dict.keys() if course_id not in all_prerequisites]
        all_prerequisites = set()
        for course in course_dict.values():
            for pre_req_id in course['childIds']:
                all_prerequisites.add(pre_req_id)

        # Find root courses (courses that are not prerequisites of any other course)
        root_courses = []
        for course_id in course_dict.keys():
            if course_id not in all_prerequisites:
                root_courses.append(course_id)
        print("root courses")
        for i in root_courses:
            print(i)
        # Build trees for each root course
        trees = []
        visited = set()
        for root_id in root_courses:
            tree = build_tree(root_id, visited.copy())
            if tree:
                trees.append(tree)
        # print(trees)
        # Sort trees by the code of the root course
        trees.sort(key=lambda tree: tree[0]['code'])

        return trees

    @staticmethod
    def create_course(name, code, pre_requisites):
        print(name, type(pre_requisites))
        # if pre_requisites == [] or pre_requisites is None:
        #     pre_requisites = '[]'
        # else:
        #     pre_requisites = json.dumps(pre_requisites)
        course = Course(name=name, code=code, pre_requisites=pre_requisites)
        print('221')
        course.save()
        print('222')
        return course

    @staticmethod
    def get_course(course_id):
        course = Course.objects.get(_id=course_id)
        return CourseService.get_prerequisites(course._id)




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
