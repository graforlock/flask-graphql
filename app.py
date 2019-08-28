from database import init_db
from flask import Flask, render_template
from flask_graphql import GraphQLView
from schema import schema
import srsly

app = Flask(__name__, static_url_path="", static_folder="./")
app.debug = True

default_query = '''
query Emails {
  emails {
    id,
    eid,
    subject,
    content
  }
}
'''.strip()

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, default_query=default_query))

@app.route('/emails.json')
def get_emails():
    result = schema.execute(default_query)
    return srsly.json_dumps(result.data)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run()