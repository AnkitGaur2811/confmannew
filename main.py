from flask import Flask,request
import KeywordExtract as ex
import Reviwerass as Reass

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

@app.route("/extract",methods = ["POST"])
def extractor():
    data = request.json
    abs1 =data["abs"]
    keys = ex.keyword_extractor(abs1)
    result = {"Keywords":keys}
    return result

@app.route("/assignreviewer",methods=["POST"])
def assigner():
    data = request.json
    allreviewer = data["allreviewer"]
    allpaperkeywords = data["allpaperkeywords"]
    assignedreview = data["assignedreview"]
    result = Reass.assgin(allreviewer,allpaperkeywords,assignedreview)
    return {"result": result}

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0")