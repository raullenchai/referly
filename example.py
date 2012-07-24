from lib import client

KEY = r'12345'
SECRET = r'abcde'


if __name__ == "__main__":
	
	
	myclient = client.ReferlyAPI(KEY, SECRET)

	#Create Account 
	print myclient.create_account(r'foobar@gmail.com')
	
	#List Links
	print myclient.list_links()
	
	#Create Link
	print myclient.create_link(r'http://refer.ly')
	
	#List Rewards
	print myclient.list_rewards()
	
	#Add Reward
	print myclient.add_reward('12345', 1.00, '2012-06-01', '2012-08-01')
	

