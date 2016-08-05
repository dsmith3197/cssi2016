#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
from student import Student
import jinja2
import os
import json
import urllib
import urllib2
import random
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class RandomUserHandler(webapp2.RequestHandler):
    def get(self):
        response = urllib2.urlopen("https://randomuser.me/api/")
        content = response.read()
        content_obj = json.loads(content)
        name = content_obj['results'][0]['name']['first'] + " " + content_obj['results'][0]['name']['last']
        email = content_obj['results'][0]['email']
        self.response.write("my name is " + name + " and my email is "+  email + ".")

class GifHandler(webapp2.RequestHandler):
    def get(self):
        search = env.get_template("gifSearch.html")
        self.response.write(search.render())

    def post(self):
        results = env.get_template("showResults.html")
        query = self.request.get("query")

        if query == "":
            self.response.write('<h1>You didn\'t enter a search term! Here\'s a random gif</h1>')
            base_url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC"
            giphy_json_content = urllib2.urlopen(base_url).read()
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            data = {'urls' : [parsed_giphy_dictionary['data']['image_original_url']]}
            self.response.write(results.render(data))


        else:
            base_url = "http://api.giphy.com/v1/gifs/search?"
            url_params = {'q': query, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
            giphy_json_content = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            data = {'urls' : []}
            for i in parsed_giphy_dictionary['data']:
                data['urls'].append(i['images']['original']['url'])
            self.response.write(results.render(data))

class GoogleLoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))

        self.response.out.write('<html><body>%s</body></html>' % greeting)

class AddStudentHandler(webapp2.RequestHandler):
    def get(self):
        addStudent = env.get_template("addStudent.html")
        self.response.write(addStudent.render())

    def post(self):
        name = self.request.get('name')
        college = self.request.get('college')
        student = Student(name=name, university=college)
        key = student.put()
        self.response.write(name + " from " + college + " was added to the database <br> <a href='/displaystudents'>Display Students</a> <a href='/student'>Add a Student</a> <a href='/modifystudent'>Modify an Entry</a>")

class DisplayStudentsHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.get('college') != "":
            query = Student.query().filter(Student.university == self.request.get('college'))
            students = query.fetch()
        else:
            students = Student.query().fetch()
        data = {'students':students}
        displayStudents = env.get_template("displayStudents.html")
        self.response.write(displayStudents.render(data))  

class ModifyStudentHandler(webapp2.RequestHandler):
    def get(self):
        modifyStudent = env.get_template("modifyStudent.html")
        self.response.write(modifyStudent.render())

    def post(self):
        name = self.request.get('name')
        new_name = self.request.get('new_name')
        new_college = self.request.get('new_college')
        if name == "" or new_name == "" or new_college == "":
            error = env.get_template('modifyError.html')
            self.response.write(error.render())
        else:
            query = Student.query().filter(Student.name == name)
            students = query.fetch()
            for student in students:
                student.name = new_name
                student.university = new_college
                student.put()
                self.response.write(name + " was successfully changed <br> <a href='/displaystudents'>Display Students</a> <a href='/student'>Add a Student</a> <a href='/modifystudent'>Modify an Entry</a>")


app = webapp2.WSGIApplication([
    ('/randomuser', RandomUserHandler),
    ('/gif', GifHandler),
    ('/', GoogleLoginHandler),
    ('/student', AddStudentHandler),
    ('/displaystudents', DisplayStudentsHandler),
    ('/modifystudent', ModifyStudentHandler)
], debug=True)
