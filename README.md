## Endpoints

### Get All Courses

Retrieves a list of all courses.

- **URL:** `/courses/`
- **Method:** GET
- **Success Response:**
  - **Code:** 200
  - **Content:** List of course objects
    ```json
    [
    {
        "id": "9f535aeb-5859-4be4-90b5-d7c3a77c03f4",
        "name": "Intro to programming2",
        "code": "CSIS2222",
        "pre_requisites": [
            {
                "id": "caa14070-8839-4996-96bd-db6f1993701f",
                "name": "Intro to programming1",
                "code": "CSIS1222",
                "pre_requisites": []
            }
        ]
    },
    {
        "id": "608b6270-24cf-4e90-90b1-e858b2cf6f97",
        "name": "basic kk",
        "code": "CSIS0111",
        "pre_requisites": [
            {
                "id": "d34d9061-a9f4-4509-b374-1e875206c6d0",
                "name": "Html + CSS",
                "code": "CSIS1280",
                "pre_requisites": [
                    {
                        "id": "eafac90a-a914-47dd-892d-f32623a0d136",
                        "name": "basi000",
                        "code": "CSIS0000",
                        "pre_requisites": []
                    }
                ]
            }
        ]
    }
]
    ```

### Get a Specific Course

Retrieves information about a specific course.

- **URL:** `/courses/<course_id>/`
- **Method:** GET
- **URL Params:** 
  - Required: `course_id=[uuid]`
- **Success Response:**
  - **Code:** 200
  - **Content:** Course object
    ```json
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "Introduction to Computer Science",
      "code": "CS101",
      "pre_requisites": []
    }
    ```
- **Error Response:**
  - **Code:** 500
  - **Content:** `{ "error": "Course not found" }`

### Create a New Course

Creates a new course.

- **URL:** `/courses/`
- **Method:** POST
- **Data Params:**
  ```json
  {
    "name": "Advanced Programming",
    "code": "CS201",
    "pre_requisites": ["550e8400-e29b-41d4-a716-446655440000"]
  }
