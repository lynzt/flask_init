from flask import Flask, jsonify, request
from pymemcache.client.base import Client
from urllib import parse
from os import environ
import psycopg2
import psycopg2.extras

memcache = Client(environ['MEMCACHE_SERVER'], serializer=json_serializer, deserializer=json_deserializer)
db_url = parse.urlparse(environ["DATABASE_URL"])
db = "dbname=%s user=%s password=%s host=%s port=%s" % (db_url.path[1:], db_url.username, db_url.password, db_url.hostname, db_url.port)
conn = psycopg2.connect(db)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'works'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
