#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__ = "$Revision$ $Date$"
__author__  = "Guillaume Bour <gbour@proformatique.com>"
__license__ = """
    Copyright (C) 2010  Proformatique

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA..
"""

import sys, httplib, urllib, base64, csv
import cjson as json
from optparse import OptionParser

URI    = '/service/ipbx/json.php/restricted/pbx_services/phonebook/?act=list'

FIELDS = [
	{'name': 'title'          , 'ref': ['phonebook', 'title']},
	{'name': 'firstname'      , 'ref': ['phonebook', 'firstname']},
	{'name': 'lastname'       , 'ref': ['phonebook', 'lastname']},
	{'name': 'displayname'    , 'ref': ['phonebook', 'displayname']},
	{'name': 'society'        , 'ref': ['phonebook', 'society']},
	{'name': 'mobilenumber'   , 'ref': ['phonebooknumber', 'mobile', 'number']},
	{'name': 'email'          , 'ref': ['phonebook', 'email']},
	{'name': 'url'            , 'ref': ['phonebook', 'url']},
	{'name': 'description'    , 'ref': ['phonebook', 'description']},

	{'name': 'officenumber'   , 'ref': ['phonebooknumber' , 'office', 'number']},
	{'name': 'faxnumber'      , 'ref': ['phonebooknumber' , 'fax'   , 'number']},
	{'name': 'officeaddress1' , 'ref': ['phonebookaddress', 'office', 'address1']},
	{'name': 'officeaddress2' , 'ref': ['phonebookaddress', 'office', 'address2']},
	{'name': 'officecity'     , 'ref': ['phonebookaddress', 'office', 'city']},
	{'name': 'officestate'    , 'ref': ['phonebookaddress', 'office', 'state']},
	{'name': 'officezipcode'  , 'ref': ['phonebookaddress', 'office', 'zipcode']},
	{'name': 'officecountry'  , 'ref': ['phonebookaddress', 'office', 'country']},

	{'name': 'homenumber'     , 'ref': ['phonebooknumber' , 'home', 'number']},
	{'name': 'homeaddress1'   , 'ref': ['phonebookaddress', 'home', 'address1']},
	{'name': 'homeaddress2'   , 'ref': ['phonebookaddress', 'home', 'address2']},
	{'name': 'homecity'       , 'ref': ['phonebookaddress', 'home', 'city']},
	{'name': 'homestate'      , 'ref': ['phonebookaddress', 'home', 'state']},
	{'name': 'homezipcode'    , 'ref': ['phonebookaddress', 'home', 'zipcode']},
	{'name': 'homecountry'    , 'ref': ['phonebookaddress', 'home', 'country']},

	{'name': 'othernumber'    , 'ref': ['phonebooknumber' , 'other', 'number']},
	{'name': 'otheraddress1'  , 'ref': ['phonebookaddress', 'other', 'address1']},
	{'name': 'otheraddress2'  , 'ref': ['phonebookaddress', 'other', 'address2']},
	{'name': 'othercity'      , 'ref': ['phonebookaddress', 'other', 'city']},
	{'name': 'otherstate'     , 'ref': ['phonebookaddress', 'other', 'state']},
	{'name': 'otherzipcode'   , 'ref': ['phonebookaddress', 'other', 'zipcode']},
	{'name': 'othercountry'   , 'ref': ['phonebookaddress', 'other', 'country']},
]

def resolver(value, keys):
	for key in keys:
		value = value.get(key, None)
		if value is None or not value:
			value = None; break

	if value is not None:
		value = value.encode('utf-8')
	return value

def phonebook_export(csvfilename, options):
	global URI, FIELDS

	headers = {
		"Content-type" : "application/json",
		"Accept"       : "text/plain"
	}
	
	if options.password is not None:
		headers['Authorization'] = 'Basic ' + \
			base64.encodestring('%s:%s' % (options.username, options.password))[:-1]

	if options.ssl:
		conn = httplib.HTTPSConnection(options.server, options.port)
	else:
		conn = httplib.HTTPConnection(options.server, options.port)

	""" query XiVO phonebook """
	try:
		conn.request('GET', URI, None, headers)
	except Exception, e:
		print "Unable to connect to XiVO server (%s@%s:%d): %s" % \
			(options.username, options.server, options.port, e); 
		return False

	response = conn.getresponse()
	data     = response.read()

	if response.status != 200:
		print "Unable to query XiVO phonebook (%s@%s:%d): %s" % \
			(options.username, options.server, options.port, response.reason)
		return False

	try:
		phonebook = json.decode(data)
	except json.DecodeError, e:
		print "Unable to decode datastream returned by server: %s" % e
		return False
#	import pprint; pprint.pprint(phonebook)

	""" export in csv """
	try:
		export = csv.writer(open(csvfilename, 'wb'), delimiter='|')
		export.writerow([f['name'] for f in FIELDS])
		export.writerows([[resolver(contact, f['ref']) for f in FIELDS] for contact in phonebook])
	except IOError, e:
		print "Unable do create csv file: %s" % e; return False

	return True


if __name__ == '__main__':
	usage  = "Usage: %prog [options] csv-file"
	parser = OptionParser(usage=usage)
	parser.add_option('--no-ssl'         , dest='ssl'     , action='store_false',
		default=True, help="connect to XiVO without using SSL (default=false)")
	parser.add_option('-s', '--server'   , dest='server'  , action='store',
		type='string', default='localhost', help="XiVO server (default=localhost)")
	parser.add_option('--port'           , dest='port'    , action='store',
		type='int', default='-1', help="XiVO port (default=443 if ssl, 80 else)")
	parser.add_option('-u', '--username' , dest='username', action='store',
		type='string', default='root', help="XiVO username (default=root)")
	parser.add_option('-p', '--password' , dest='password', action='store',
		type='string', help="XiVO password (if not set, use no auth)")

	(options, args) = parser.parse_args()
	if len(args) != 1:
		parser.print_help(); sys.exit(2)

	if options.port == -1:
		if options.ssl:
			options.port = 443
		else:
			options.port = 80
#	print options, args

	if not phonebook_export(args[0], options):
		sys.exit(1)

