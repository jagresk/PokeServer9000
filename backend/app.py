import psycopg2
from fastapi import FastAPI
from rpy2.robjects import r, FloatVector

app = FastAPI()

@app.get("/usage")
def get_usage():
	r.source("rlogic.R")
	data = FloatVector([15.2, 33.4, 27.8])
	summary = r['summary_stats'](data)
	return {name: summary.rx2(name[0] for name in summary.names)}
	
def test_db():
    conn = psycopg2.connect(
        dbname="poke9000",
        user="jeb",
        password="jebbybebby",
        host="db",
        post="5432",
    )
    cur = conn.cursor()
    cur.execute("SELECT 1 + 1;")
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"result": result}
