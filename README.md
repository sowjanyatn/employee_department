Employee and Department Management application written in Pyhon (Django).

Components:

admin panel to manage employees' and departments' data
API to list, add, edit and remove employees

Pre-requisites:
    python3
    python-pip3

Install dependencies
    pip3 install -r requirements.txt

Go to employee_dept_project directory
    Before running any of the following commands, you should cd into employee_dept_project directory:

    cd employee_dept_project

Run migrations
    python3 manage.py migrate

Create superuser with privileged access
    python3 manage.py createsuperuser

Start app
    python3 manage.py runserver localhost:8000

Initial data for the database
    ./emp_dep/manage.py loaddata ./emp_dep/employee_department/fixtures/myfixtures.json

API usage

    * API to list all the employees.
        GET : http://127.0.0.1:8000/api/employee/

    * API to return an employee.
        GET : http://127.0.0.1:8000/api/employee/<employee_id>
    
    * API to return employees based on department and salary range.
        GET : http://127.0.0.1:8000/api/employee/?dept_id=<dept_id>&start_sal=<start_sal>&end_sal=<end_sal>

        ex : http://127.0.0.1:8000/api/employee/?dept_id=2&start_sal=20000.0&end_sal=30000.0
    
    * API to create a employee.
        POST : http://127.0.0.1:8000/api/employee/

            Header => Content-Type : application/json
            param => {
                        "employee": {
                            "e_id": 9,
                            "name": "asdfghjkl",
                            "contact": 8970681862,
                            "salary": 50000,
                            "role": "product_engineer",
                            "department": 2
                        }
                    }
    * API to update a employee.
        PUT : http://127.0.0.1:8000/api/employee/<employee_id>

            Header => Content-Type : application/json
            {
                "employee": {
                    "e_id": 4,
                    "name": "qwertyuio",
                    "contact": 8970681862,
                    "salary": 20000,
                    "role": "product_engineer",
                    "department": 2
                }
            }

    * API to delete a employee.
        DELETE : http://127.0.0.1:8000/api/employee/<employee_id>
