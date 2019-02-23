from socialblogproject import app
from datetime import datetime, timedelta

# Creates datetime instances to be used in 'index.html' template.
@app.context_processor
def inject_now():
	return {'now': datetime.utcnow(), 'time':timedelta(days=2)} 

# Runs the app.
if __name__ == '__main__':
	app.run(debug = True)