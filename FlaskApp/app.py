import flask
from flask import Flask, request, render_template, url_for, redirect
from PyPDF2 import PdfFileMerger

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('PDF.html')

@app.route('/handleUpload', methods=['GET', 'POST'])
def handleFileUpload(pdf_file=None):
    if flask.request.method == "POST":
        files = flask.request.files.getlist("photo1")
        namer = request.form['name']
        merger = PdfFileMerger()
        for file in files:
            merger.append(file)
        merger.write(namer + ".pdf")
        merger.close()
        # The line below will force the download of the merged pdf
        return flask.send_file(namer + '.pdf', as_attachment=True, attachment_filename=namer + '.pdf'
                               )
if __name__ == '__main__':
    app.run()
