from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import googlemaps

consumer_key = 'YOUR_TOKEN'
consumer_secret = 'YOUR_TOKEN'
access_token = 'YOUR_TOKEN'
access_secret = 'YOUR_TOKEN'

AWS_ACCESS_KEY="YOUR_KEY"
AWS_SECRET_KEY="YOUR_KEY"
AWS_REGION="us-east-1"

AWS_ES_PORT  = 443
AWS_ES_HOST = "YOUR_URL"
AWS_ES_INDEX = 'twitter-map'
AWS_ES_TYPE = 'tweet'

awsauth = AWS4Auth(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, 'es')

es = Elasticsearch(
    hosts=[{'host': AWS_ES_HOST, 'port': AWS_ES_PORT}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

GMAP_KEY = 'YOUR_KEY'
gmaps = googlemaps.Client(key=GMAP_KEY)

FILTERS = ['China', 'USA', 'Japan', 'Russia', 'England', 'France', 'German', 'Donald Trump', 'vote', 'Justin Biber', 'Maroon 5', 'La La Land', 'Logan', 'The Shack']
