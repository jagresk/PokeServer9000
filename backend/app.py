from fastapi import FastAPI
from rpy2.robjects import r, FloatVector

app = FastAPI()

@app.get("/usage")
def get_usage():
	r.source("rlogic.R")
	data = FloatVector([15.2, 33.4, 27.8])
	summary = r['summary_stats'](data)
	return {name: summary.rx2(name[0] for name in summary.names}
