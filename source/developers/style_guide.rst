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


Conditions
**********

Avoid using parenthesis around if statements, unless the statement expands
on multiple lines or you need to nest your conditions.

Bad Examples::

    if(x == 3):
        print "condition is true"

    if(x == 3 and y == 4):
        print "condition is true"


Good Examples::

    if x == 3:
        print "condition is true"

    if x == 3 and y == 4:
        print "condition is true"

    if (extremely_long_variable == 3
        and another_long_variable == 4
        and yet_another_variable == 5):

        print "condition is true"

    if (2 + 3 + 4) - (1 + 1 + 1) == 6:
        print "condition is true"


Consider refactoring your statement into a function if it becomes too long,
or the meaning isn't clear.

Bad Example::

    if price * tax - bonus / reduction + fee < money
        product.pay(money):

Good Example::

    def calculate_price(price, tax, bonus, reduction, fee):
        return price * tax - bonus / reduction + fee

    final_price = calculate_price(price, tax, bonus, reduction, fee)

    if final_price < money:
        product.pay(money)


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

Unit tests should be short, clear and concise in order to make the test easy to
understand. A unit test is separated into 3 sections :

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


Exceptions
==========

Exceptions should not be used for flow control. Raise exceptions only for edge cases,
or when something that isn't usually expected happens.

Bad Example::

    def is_user_available(user):
        if user.available():
            return True
        else:
            raise Exception("User isn't available")

    try:
        is_user_available(user)
    except Exception:
        disable_user(user)


Good Example::

    def is_user_available(user):
        if user.available():
            return True
        else:
            return False


    if not is_user_available(user):
        disable_user(user)


Avoid throwing `Exception`. Use one of Python's built-in Exceptions, or create
your own custom Exception. A list of exceptions is available at
http://docs.python.org/2/library/exceptions.html#exception-hierarchy


Bad Example::

    def get_user(userid):
        user = session.query(User).get(userid)

        if not user:
            raise Exception("User not found")

Good Example::

    class UserNotFoundError(LookupError):

        def __init__(self, userid):
            message = "user with id %s not found" % userid
            LookupError.__init__(self, message)

    def get_user(userid):
        user = session.query(User).get(userid)

        if not user:
            raise UserNotFoundError(userid)
