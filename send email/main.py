from flask import Flask, request, flash, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "gopi"

@app.route("/", methods=["POST","GET"])
def mail():
    if request.method == "POST":
        fmail = request.form["fmail"]
        fpass = request.form["fpass"]
        tmail = request.form["tmail"]
        message = request.form["message"]
        body = request.form["body"]
        app.config['MAIL_SERVER']='smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = fmail
        app.config['MAIL_PASSWORD'] = fpass
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True

        mail = Mail(app)

        msg = Message(message, sender=fmail, recipients=[tmail])
        msg.body = body
        mail.send(msg)
        flash("Mail Sented Successfully",'success')

    return render_template('mail.html')


if __name__ == '__main__':
    app.run(debug=True)