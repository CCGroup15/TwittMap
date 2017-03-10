from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import googlemaps

consumer_key = 'k20CumsFv7l5JO0KqVIT03DeL'
consumer_secret = 'V57rHUlKcijBPzU6GlyYKNPQzjwM7bJEOmdKlTfWNEixh0y4er'
access_token = '4604284034-ZlWxWhxT9UTtNX42SmehU63XoA7ZsUGtyWxBWfn'
access_secret = 'HNbiT0w6UWiNxmhiGPhEI5xDR3kEKkGyswVmNSwTDA9ot'

AWS_ACCESS_KEY="AKIAJVL7ORHB3FBM4FVQ"
AWS_SECRET_KEY="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"
AWS_REGION="us-east-1"

AWS_ES_PORT  = 443
AWS_ES_HOST = "search-twitter-map-3xazlsfl474stlzm4n2ekixjl4.us-east-1.es.amazonaws.com"
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
# print(es.info())

GMAP_KEY = 'AIzaSyAovkBO68rNju_an3XHa29XmUQ0RWq55Is'
gmaps = googlemaps.Client(key=GMAP_KEY)

FILTERS = ['china', 'usa', 'japan', 'russia', 'england', 'france', 'german']
