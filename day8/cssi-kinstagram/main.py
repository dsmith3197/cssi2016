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
from google.appengine.ext import blobstore
from google.appengine.api import users
from kinsta_models import KinstaUser
from kinsta_models import Picture
import jinja2
import os
import json
import urllib
import urllib2
import webapp2

env = jinja2.Environment(loader= jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout = None
        if user:
            #check if user has an account set up
            account_created = False
            kinsta_users = KinstaUser.query().fetch()
            for kinsta_user in kinsta_users:
                if user.user_id() == kinsta_user.user_id:
                    #display timeline
                    greeting = env.get_template('timeline.html')
                    account_created = True
            if not account_created:
                #Prompt to create account
                greeting = env.get_template('createProfile.html')
            
            logout_url = users.create_logout_url('/')
            logout = env.get_template('logout.html')
            data = {'url': logout_url}
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        if logout:
            self.response.write(greeting.render())
            self.response.write(logout.render(data))
        else:
            self.response.write(
                '<html><body>{}</body></html>'.format(greeting))

    def post(self):
        #retrieve data from form
        name = self.request.get('name')
        username = self.request.get('username')

        #create new user
        user = users.get_current_user()
        new_user = KinstaUser(name= name, username = username, user_id = user.user_id())
        new_user.put()

        #redirect page
        self.redirect('/')

        
class UploadProfilePicHandler(webapp2.RequestHandler):
    def get(self):
    	upload_pic = env.get_template('uploadProfilePic.html')
    	upload_url = blobstore.create_upload_url('/upload_photo')
    	data = {'url':upload_url}
    	self.response.write(upload_pic.render(data))

    def post(self):
    	#retrieve data from form
        name = self.request.get('name')
        username = self.request.get('username')
#        profile_pic = self.request.get('profile_pic')
#        caption = self.request.get('caption')

        #create new picture and user
        new_user = User(name= name, username = username)
        new_user.put()

class FriendHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        friends = []
        non_friends = []
        if user:
            cur_user = KinstaUser.query().filter(KinstaUser.user_id == user.user_id()).fetch()[0]
            all_users = KinstaUser.query().filter(KinstaUser.user_id != user.user_id()).fetch()

            for user in all_users:
                if user.user_id in cur_user.friends:
                    friends.append(user)
                else:
                    non_friends.append(user)

            data = {'friends': friends, "non_friends": non_friends}
            friend_page = env.get_template("friends.html")
            self.response.write(friend_page.render(data))

            logout_url = users.create_logout_url('/')
            logout = env.get_template('logout.html')
            self.response.write(logout.render())
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
            self.response.write(greeting)

class AddFriendHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if user:
            friend_id = self.request.get('friend_id')
            cur_user = KinstaUser.query().filter(KinstaUser.user_id == user.user_id()).fetch()[0]
            cur_user.friends.append(friend_id)
            cur_user.put()
            self.response.write("successful <a href='/'>go back home</a>")


class RemoveFriendHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if user:
            friend_id = self.request.get('friend_id')
            cur_user = KinstaUser.query().filter(KinstaUser.user_id == user.user_id()).fetch()[0]
            cur_user.friends.remove(friend_id)
            cur_user.put()
            self.response.write("successful <a href='/'>go back home</a>")

class TestHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/friends', FriendHandler),
    ('/add_friend', AddFriendHandler),
    ('/remove_friend', RemoveFriendHandler),
    ('/test', TestHandler),
    ('/upload_profile_pic', UploadProfilePicHandler)
], debug=True)
