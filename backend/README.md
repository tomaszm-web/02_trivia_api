# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 
Error Handling
Errors are returned as JSON objects in the following format:

{
    "success": False, 
    "error": 400,
    "message": "bad request"
}

The API will return four error types when requests fail:

    400: Bad Request
    404: Resource Not Found
    422: Not Processable
	405: Method not allowed

ENDPOINTS:
GET '/api/categories'
GET '/api/questions'
POST '/api/questions'
GET '/api/categories/<int:id>/questions'
POST '/api/quizzes'
DELETE '/api/questions/<int:question_id>'

GET '/api/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/api/questions?page=<page:int>'
 - Returns a list of question objects and a list of category objects, success value, and total number of questions
 - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

Example response:
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "current_category": null, 
  "questions": [
    {
      "answer": "Crust, mantle, and core", 
      "category": "Science", 
      "difficulty": 5, 
      "id": 24, 
      "question": "The earth has three layers of varying temperatures. What are its three layers?"
    }, 
    {
      "answer": "Jupiter", 
      "category": "Science", 
      "difficulty": 5, 
      "id": 25, 
      "question": "What is the largest planet in the solar system?"
    }, 
    {
      "answer": "Ear", 
      "category": "Science", 
      "difficulty": 4, 
      "id": 26, 
      "question": "On what part of your body would you find the pinna?"
    }
  ], 
  "success": true, 
  "total_questions": 13
}

POST '/api/questions'
Request body: {question:string, answer:string, difficulty:int, category:int}
- Creates a new question using the submitted question, difficulty, category and answer. 
- Returns the question as an object together with the success value. 
Example response:
{
  "question": {
    "answer": "Cerebrum", 
    "category": "Science", 
    "difficulty": 1, 
    "id": 33, 
    "question": "Name the largest part of human brain?"
  }, 
  "success": true
}

POST '/api/questions'
Request body: {searchTerm:string}
- Fetches a list of questions containing the submitted search term (not case-sensitive), the total number of questions and success value. Current category is always returned with null value.

Example response:
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Cerebrum", 
      "category": "Science", 
      "difficulty": 1, 
      "id": 1, 
      "question": "Name the largest part of human brain?"
    }, 
    {
      "answer": "Iris", 
      "category": "Science", 
      "difficulty": 1, 
      "id": 2, 
      "question": "What is the name of coloured part of human eyes which is controlling the light passing through the pupil?"
    }, 
    {
      "answer": "Melanin", 
      "category": "Science", 
      "difficulty": 2, 
      "id": 3, 
      "question": "What is the name of substance which is giving skin and hair its pigments?"
    }, 
    {
      "answer": "Andy Warhol", 
      "category": "Art", 
      "difficulty": 1, 
      "id": 10, 
      "question": "Which artist made his name with paintings of soup cans and Coca-Cola bottles?"
    }
  ], 
  "success": true, 
  "total_questions": 4
}

GET '/api/categories/<int:id>/questions'
- Fetches a List of questions for the specified category and paginates them in a default quantity of 10 per page. 
- It also returns success value, current category and total number of questions for that category.
- Request Arguments: category id <int:id>

Example response:
{
  "current_category": 2, 
  "questions": [
    {
      "answer": "Andy Warhol", 
      "category": "Art", 
      "difficulty": 1, 
      "id": 10, 
      "question": "Which artist made his name with paintings of soup cans and Coca-Cola bottles?"
    }, 
    {
      "answer": "Christopher Wren", 
      "category": "Art", 
      "difficulty": 1, 
      "id": 11, 
      "question": "Who designed the largest Protestant church in England, St Paul's Cathedral?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}

POST '/api/quizzes'
- Request body: {previous_questions: arr, quiz_category: {id:int, type:string}}
- Fetches a random question for a chosen category which is not among previously used questions.

Example response:
{
  "question": {
    "answer": "Ear", 
    "category": "Science", 
    "difficulty": 4, 
    "id": 26, 
    "question": "On what part of your body would you find the pinna?"
  }, 
  "success": true
}

DELETE '/api/questions/<int:question_id>'
- Deletes the question of the given ID if it exists. Returns the id of the deleted question and success value.
- Request Arguments: question id <int:id>

{
  "deleted": 35, 
  "success": true
}


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```