***********
Style Guide
***********

Syntax
======

License
*******

Python files start with a UTF8 encoding comment and the GPLv3 license.
A blank line should separate the license from the imports

Example::

    # -*- coding: utf-8 -*-

    # Copyright (C) 2013 Avencall
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>

    import argparse


Spacing
*******

* Lines should not go further than 80 to 100 characters.
* In python, indentation blocks use 4 spaces
* In PHP, indentation blocks use tabs
* Imports should be ordered alphabetically
* Separate module imports and `from` imports with a blank line

Example::

    import argparse
    import datetime
    import os
    import re
    import shutil
    import tempfile

    from StringIO import StringIO
    from urllib import urlencode


PEP8
****

When possible, use pep8 to validate your code. Generally, the following
errors are ignored :

 * E501 (max 80 chars per line)

Example::

    pep8 --ignore=E501 xivo_cti


When possible, avoid using backslashes to separate lines.

Bad Example::

    user = session.query(User).filter(User.firstname == firstname)\
                              .filter(User.lastname == lastname)\
                              .filter(User.number == number)\
                              .all()

Good Example::

    user = (session.query(User).filter(User.firstname == firstname)
                               .filter(User.lastname == lastname)
                               .filter(User.number == number)
                               .all())


Strings
*******

Avoid using the `+` operator for concatenating strings. Use string
interpolation instead.

Bad Example::

    phone_interface = "SIP" + "/" + username + "-" + password

Good Example::

    phone_interface = "SIP/%s-%s" % (username, password)


Comments
********

Redundant comments should be avoided. Instead, effort should be put on making
the code clearer.

Bad Example::

    #Add the meeting to the calendar only if it was created on a week day
    #(monday to friday)
    if meeting.day > 0 and meeting.day < 7:
        calendar.add(meeting)


Good Example::

    def created_on_week_day(meeting):
        return meeting.day > 0 and meeting.day < 7

    if created_on_week_day(meeting):
        calendar.add(meeting)


Naming
======


Conventions for functions prefixed by `find`:

 * Return None when nothing is found
 * Return an object when a single entity is found
 * Return the first element when multiple entities are found

Example::

    def find_by_username(username):
        users = [user1, user2, user3]
        user_search = [user for user in users if user.username == username]

        if len(user_search) == 0:
            return None

        return user_search[0]

Conventions for functions prefixed by `get`:

 * Raise an Exception when nothing is found
 * Return an object when a single entity is found
 * Return the first element when multiple entities are found


Example::

    def get_user(userid):
        users = [user1, user2, user3]
        user_search = [user for user in users if user.userid == userid]

        if len(user_search) == 0:
            raise UserNotFoundError(userid)

        return user_search[0]


Conventions for functions prefixed by `find_all`:

 * Return an empty list when nothing is found
 * Return a list of objects when multiple entites are found

Example::

    def find_all_users_by_username(username):
        users = [user1, user2, user3]
        user_search = [user for user in users if user.username == username]

        return user_search

Magic numbers
*************

Magic numbers should be avoided. Arbitrary values should be assigned to
variables with a clear name

Bad example::

    class TestRanking(unittest.TestCase):

        def test_ranking(self):
            rank = Rank(1, 2, 3)

            self.assertEquals(rank.position, 1)
            self.assertEquals(rank.grade, 2)
            self.assertEquals(rank.session, 3)


Good example::

    class TestRanking(unittest.TestCase):

        def test_ranking(self):
            position = 1
            grade = 2
            session = 3

            rank = Rank(position, grade, session)

            self.assertEquals(rank.position, position)
            self.assertEquals(rank.grade, grade)
            self.assertEquals(rank.session, session)


Tests
=====

Unit tests should be short, clear and concise in order to make the goal
of the test easy to understand. A unit test is separated into 3 sections :

 * Preconditions / Preparations
 * Thing to test
 * Assertions

Sections are separated by a blank line. Sections that become too big should be
split into smaller functions.

Example::

    class UserTestCase(unittest.TestCase):

        def test_fullname(self):
            user = User(firstname='Bob', lastname='Marley')
            expected = 'Bob Marley'

            fullname = user.fullname()

            self.assertEquals(expected, fullname)

        def _prepare_expected_user(self, firstname, lastname, number):
            user = User()
            user.firstname = firstname
            user.lastname = lastname
            user.number = number

            return user

        def _assert_users_are_equal(expected_user, actual_user):
            self.assertEquals(expected_user.firstname, actual_user.firstname)
            self.assertEquals(expected_user.lastname, actual_user.lastname)
            self.assertEquals(expected_user.number, actual_user.number)

        def test_create_user(self):
            expected = self._prepare_expected_user('Bob', 'Marley', '4185551234')

            user = create_user('Bob', 'Marley', '4185551234')

            self._assert_users_are_equal(expected, user)


