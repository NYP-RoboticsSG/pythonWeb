from flask import Flask, render_template, url_for, request, redirect, send_from_directory
import os
import time

app = Flask(__name__)
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='img/vnd.microsoft.icon')

@app.route("/")
def index():
    return render_template("index_static_css_favicon.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route("/submit_form", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)

        if len([i for i in data.values() if i != '']) == 7:
            return render_template("done.html"), {"Refresh": f"5; url={url_for('index')}"}
        else:
            return redirect(url_for('html_page', page_name='register.html'))
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
