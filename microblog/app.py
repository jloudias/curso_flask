from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # loads environment variables specified at .env file
def create_app():
    app = Flask(__name__)

    # Database connection - Atlas Server/cluster:sandbox/database:microblog/collection:entries
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        # insert document 
        if request.method == "POST":
            entry_content = request.form.get('content')
            entry_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content": entry_content, "date": entry_date})
        # select all documents and pass to template
        # NOTE: this is a list comprehension
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})

        ]  # NOTE: end of the list comprehension

        return render_template("home.html", entries=entries_with_date)
    
    return app

   
# if __name__ == "__main__":
#    app.run(debug=True)
