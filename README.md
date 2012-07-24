#Referly -- A python wrapper of referly REST API#
=======

##Usage##
	
1. import the lib
		from lib import client

2. create an instance
		myclient = client.ReferlyAPI(KEY, SECRET)

3. create an account 
		myclient.create_account(r'foobar@gmail.com')

4. list links
		myclient.list_links()

5. create a link
		myclient.create_link(r'http://refer.ly')

6. list rewards
		myclient.list_rewards()

7. add a reward
		myclient.add_reward('12345', 1.00, '2012-06-01', '2012-08-01')

##Example##
see example.py
