from flask import Flask, render_template, request
import aicontent

def page_not_found(e):
	return render_template('404.html'), 404

app = Flask(__name__)
app.register_error_handler(404, page_not_found)

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == 'POST':

		future_career = request.form['future_career']
		prompt=aicontent.generate_prompt(future_career)
		openAIAnswerUnformatted = aicontent.openAIQuery(prompt)
		print(openAIAnswerUnformatted)
		openAIAnswer = openAIAnswerUnformatted.replace('\n','</br>')
		prompt = 'Great choice! Here are some goals ideas if you want to become a {} in the future:'.format(future_career)

	return render_template('index.html', **locals())