import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request,selection):
     page = request.args.get('page', 1, type=int)
     start = (page - 1) * QUESTIONS_PER_PAGE
     end = start + QUESTIONS_PER_PAGE

     questions = [question.format() for question in selection]
     current_questions = questions[start:end]
     return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  CORS(app, resources={r"/api/*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorization')
      response.headers.add('Access-Control-Allow-Headers','GET, POST, PATCH, DELETE, OPTIONS')
      return response

  @app.route('/api/categories', methods=['GET'])
  def get_categories():
      categories = Category.query.all()
      formatted_categories = {category.id: category.type for category in categories}

      if len(categories) == 0:
         abort(404)

      return jsonify({
             'success': True,
             'categories': formatted_categories
          })
 
  @app.route('/api/questions')
  def get_questions():

     selection = Question.query.all()
     current_questions = paginate_questions(request, selection)
     categories = Category.query.order_by(Category.id).all()
     formatted_categories = [category.format() for category in categories]

     if len(current_questions) == 0:
        abort(404)

     return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(selection),
            'current_category': None,
            'categories': formatted_categories
         })

  @app.route('/api/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
     try:
       question = Question.query.filter(Question.id == question_id).one_or_none()
       
       if question is None:
           abort(404)

       question.delete()

       return jsonify({
           'success': True,
           'deleted': question_id,
         })
     
     except:
       abort(422)

  @app.route('/api/questions', methods=['POST'])
  def create_question():
      body = request.get_json()

      new_question = body.get('question', None)
      new_difficulty = body.get('difficulty', None)
      new_category = body.get('category', None)
      new_answer = body.get('answer', None)
      searchTerm = body.get('searchTerm', None)

      try:
         if searchTerm:
           selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(searchTerm)))
           current_questions = paginate_questions(request, selection)


           return jsonify({
              'success': True,
              'questions': current_questions,
              'total_questions': len(selection.all()),
              'current_category': None
            })
         else:
           category = Category.query.filter_by(id=new_category).one_or_none()
           question = Question(question=new_question, answer=new_answer,difficulty=new_difficulty, category=category.type)
           question.insert()

           return jsonify({
             "success": True,
             "question": question.format()
            })

      except():
          abort(422)

  @app.route('/api/categories/<int:id>/questions', methods=['GET'])
  def get_questions_by_category(id):
        category = Category.query.filter_by(id=id).one_or_none()

        if (category is None):
            abort(404)

        selection = Question.query.filter_by(category=category.type).all()
        current_questions = paginate_questions(request, selection)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(selection),
            'current_category': id
        })

  @app.route('/api/quizzes', methods=['POST'])
  def get_next_question(): 
       try:
         body = request.get_json()
         previous_questions = body.get('previous_questions', [])
         category = body.get('quiz_category', [])

         if category['id'] == 0:
             questions = Question.query.filter(Question.id.notin_(previous_questions)).all()
         else:
             questions = Question.query.filter_by(category=category['type']).filter(Question.id.notin_(previous_questions)).all()
         
         available_questions = [question.format() for question in questions]
         random_question = random.choice(available_questions)

         return jsonify({
                'success': True,
                'question': random_question
            })
       except:
           abort(422)

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
         "success": False,
          "error": 404,
          "message": "resource not found"
          }), 404

  @app.errorhandler(422)
  def unprocessable(error):
     return jsonify({
         "success": False,
         "error": 422,
         "message": "unprocessable"
       }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400

  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "method not allowed"
      }), 405

  return app
 


    