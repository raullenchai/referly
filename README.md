## Referly -- A python wrapper of referly REST API


This repository contains a helpful set of classes to connect to and interact with the http://refer.ly API. For full details on the API and available methods please check out http://refer.ly/api.


## Usage
	
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

## Example
see example.py
