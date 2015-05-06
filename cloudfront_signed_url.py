#!/usr/bin/python
import time,boto
from boto.cloudfront import distribution

AWS_ACCESS_KEY_ID="key"
AWS_SECRET_ACCESS_KEY="secret"


my_connection = boto.cloudfront.CloudFrontConnection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

dist = my_connection.get_all_distributions()
a=dist[0].get_distribution()
#Set parameters for URL
key_pair_id = "key_pair_id" #from the AWS accounts page
priv_key_file = "pk.pem" #your private keypair file
expires = int(time.time()) + 15 #5 min
url="http://di53i9yykewl5.cloudfront.net/coollogo_com-29935365.png" #the url you want to sign
signed_url = a.create_signed_url(url, key_pair_id, expires, private_key_file=priv_key_file)
print(signed_url)
