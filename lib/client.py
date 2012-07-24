from urllib2 import Request, urlopen, HTTPError
from urllib import urlencode
import base64
import simplejson


class ReferlyException(Exception):
	def __init__(self, description):
		self.description = description

	def __str__(self):
		return self.description

		


class ReferlyAPI():
	def __init__(self, key, secret):
		self.prefix_path = r'https://refer.ly/api/120701'
		self.key = key
		self.secret = secret

		#fetch account's ids associated
		try: 
			response = self.URLRequest(r'/accounts', {}, 'GET')
		except HTTPError, e:
			if e.code == 403:
				raise ReferlyException(r'Invalid API key or secret')
			raise ReferlyException(r'Error Authenticating')

		#there could be many account_ids, pick the first one as default (confirm with refer.ly later)
		self.account_id = simplejson.loads(response)[r'accounts'][0][r'account_id']


	def create_account(self, email):

		if email:
			params = {'email' : email}
		else:
			raise ReferlyException(r'Missing Parameters')
		try: 
			response = self.URLRequest(r'/accounts', params, 'POST')
		except HTTPError, e:
			raise ReferlyException(r'Error Creating Account')

		self.account_id = simplejson.loads(response)[r'account_id']
		return response


	def create_link(self, url):

		if url and self.account_id:
			params = {'url' : url, 'account_id' : self.account_id}
		else:
			raise ReferlyException(r'Missing Parameters')

		try: 
			response = self.URLRequest(r'/links', params, 'POST')
		except HTTPError, e:
			raise ReferlyException(r'Error Creating Link')

		return response


	def list_links(self, count=50, page=0):

		if self.account_id:
			params = {'account_id': self.account_id, 'count' : count, 'page' : page}
		else:
			raise ReferlyException(r'Missing Parameters')

		try:
			response = self.URLRequest(r'/links', params, 'GET')
		except HTTPError, e:
			raise ReferlyException(r'Error Listing Links')
		return response


	def add_reward(self, visit_id, amount, earned_on, payable_on, vendor_external_id=None):

		if vendor_external_id:
			params = {'visit_id': visit_id, 'amount' : amount, 'earned_on' : earned_on, 'payable_on' : payable_on, 'vendor_external_id' : vendor_external_id}
		else:
			params = {'visit_id': visit_id, 'amount' : amount, 'earned_on' : earned_on, 'payable_on' : payable_on}
		
		try:
			response = self.URLRequest(r'/rewards', params, r'POST')
		except HTTPError, e:
			if e.code == 402:
				raise ReferlyException(r'Insufficient account balance for requested reward')
			raise ReferlyException(r'Error Add Reward')

		return response


	def list_rewards(self, link_id=None):

		if self.account_id:
			if link_id:
				params = {'account_id': self.account_id, 'link_id' : link_id}
			else:
				params = {'account_id': self.account_id}
		else:
			raise ReferlyException(r'Missing Parameters')
		
		try:
			response = self.URLRequest(r'/rewards', params, 'GET')
		except HTTPError, e:
			raise ReferlyException(r'Error Listing Rewards')

		return response
		

	def URLRequest(self, path, params, method=r'GET'):

		if method == r'POST':
			req = Request(self.prefix_path+path, data = urlencode(params))
		else:
			req = Request(self.prefix_path+path + '?' + urlencode(params))

		#basic auth
		base64string = base64.encodestring('%s:%s' % (self.key, self.secret)).replace('\n', '')
		req.add_header(r'Authorization', r'Basic %s' % base64string)

		return urlopen(req).read() 