from flask import Flask
import json
#chercher le site qui peut heberger api get de Lex
app = Flask(__name__)
@app.route("/login", methods=["GET"])
def getFruit():
    variable = "youssef"
    var2 = "nom"
    return json.dumps({var2:variable,"passsword":"pouler22"})
if __name__ == "__main__":
    app.run(debug=True)
    print("api start")
