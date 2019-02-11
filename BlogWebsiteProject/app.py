from socialblogproject import app
from datetime import datetime, timedelta

@app.context_processor
def inject_now():
	return {'now': datetime.utcnow(), 'time':timedelta(days=2)} 


if __name__ == '__main__':
	app.run()