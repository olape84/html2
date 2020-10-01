from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)