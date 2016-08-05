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
import jinja2
import logging
import os
import webapp2

# Initialize jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_vars = {"name": "CSSIer"}
        template = jinja_environment.get_template('hello.html')
        self.response.out.write(template.render(my_vars))

class ProfileHomeHandler(webapp2.RequestHandler):
    def get(self):
        #render navBar
        header_vars = {"webpageTitle" : "Douglas Anthony's Profile", 
                   "cssStlyeSource" : "profile/homepage.css"}
        header = jinja_environment.get_template('header.html')
        self.response.out.write(header.render(header_vars))
        body = jinja_environment.get_template('profile.html')
        self.response.out.write(body.render())

class ResumeHandler(webapp2.RequestHandler):
    def get(self):
        #render navBar
        header_vars = {"webpageTitle" : "Resume", 
                   "cssStlyeSource" : "profile/homepage.css"}
        header = jinja_environment.get_template('header.html')
        self.response.out.write(header.render(header_vars))
    
class ProjectsHandler(webapp2.RequestHandler):
    def get(self):
        #render navBar
        header_vars = {"webpageTitle" : "Projects", 
                   "cssStlyeSource" : "profile/homepage.css"}
        header = jinja_environment.get_template('header.html')
        self.response.out.write(header.render(header_vars))
    
class MusicHandler(webapp2.RequestHandler):
    def get(self):
        #render navBar
        header_vars = {"webpageTitle" : "Music", 
                   "cssStlyeSource" : "profile/homepage.css"}
        header = jinja_environment.get_template('header.html')
        self.response.out.write(header.render(header_vars))

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        #render navBar
        header_vars = {"webpageTitle" : "Contact", 
                   "cssStlyeSource" : "profile/homepage.css"}
        header = jinja_environment.get_template('header.html')
        self.response.out.write(header.render(header_vars))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        #render navBar
        header_vars = {"webpageTitle" : "About", 
                   "cssStlyeSource" : "profile/homepage.css"}
        header = jinja_environment.get_template('header.html')
        self.response.out.write(header.render(header_vars))
    
    


app = webapp2.WSGIApplication([
    ('/', ProfileHomeHandler),
    ('/profile', ProfileHomeHandler),
    ('/resume', ResumeHandler),
    ('/projects', ProjectsHandler),
    ('/music', MusicHandler),
    ('/contact', ContactHandler),
    ('/about', AboutHandler)
], debug=True)
