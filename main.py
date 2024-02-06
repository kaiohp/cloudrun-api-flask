from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text
from flask import Flask
import json

app = Flask(__name__)


@app.route("/users", methods=["GET"])
def get_users():
    # # conn_url = 'postgresql+psycopg2://postgres:123456@postgresServer:5432/postgres'

    # # engine = create_engine(conn_url)

    # # db = scoped_session(sessionmaker(bind=engine))

    # query_rows = db.execute(text("SELECT * FROM tech_users;")).fetchall()
    # results = {"data": []}
    # for row in query_rows:
    #     results["data"].append([row[0], row[1]])
    # print(results)
    # return json.dumps(results)
    return "DEU CERTO!!"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)