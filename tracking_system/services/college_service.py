from ..models import College

class CollegeService:

  @staticmethod
  def getAll():
    colleges = College.objects.all()
    return colleges

  @staticmethod
  def getOne(college_id):
    college = College.objects.get(_id=college_id)
    return college

  @staticmethod
  def update_college(college_id, name=None):
    college = CollegeService.getOne(college_id)
    if college:
      if name:
        college.name = name

    college.save()

    return college

  @staticmethod
  def delete_college(college_id):
    college = College.objects.get(_id=college_id)
    college.delete()
