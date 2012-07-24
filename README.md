## Referly -- A python wrapper of referly REST API


This repository contains a helpful set of classes to connect to and interact with the http://refer.ly API. For full details on the API and available methods please check out http://refer.ly/api.


## Usage
	
To import the lib
    from lib import client

To create an instance
    myclient = client.ReferlyAPI(KEY, SECRET)

To create an account 
    myclient.create_account(r'foobar@gmail.com')

To list links
    myclient.list_links()

To create a link
    myclient.create_link(r'http://refer.ly')

To list rewards
    myclient.list_rewards()

To add a reward
    myclient.add_reward('12345', 1.00, '2012-06-01', '2012-08-01')

## Example
see example.py
