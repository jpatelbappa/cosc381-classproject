from flask import Flask, render_template, request, jsonify
#import test_module
import query_on_whoosh
#
app=Flask(__name__)
app.config.update(dict(JSONIFY_PRETTYPRINT_REGULAR=True))
#
#@app.route("/")
#def handle_slash():
    #requested_name = request.args.get("name")
    #return render_template("index.html", user_name=requested_name)

#@app.route("/test")
#def handle_tset():
    #input="abc"
    #return test_module.test(input)

@app.route("/query", strict_slashes=False)
def handle_query():
    search_term = request.args.get("q")
    n = int(request.args.get('p'))
    return jsonify(query_on_whoosh.query(search_term, 10, n))