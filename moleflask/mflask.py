# all the imports
import os
from moleflask import molecule

from flask import Flask, request

app = Flask(__name__) # create the application instance

clientpage = """
<!doctype html>
<html>
<head>
<title>Molecule Rules!</title>
<link rel=stylesheet type=text/css href="http://localhost:5000/static/style.css">
</head>
<body>
<div class=page>
  <h1>Molecule Mass</h1>
    <form action="http://localhost:5000/givemass" method=post class=add-entry>
      <br>Enter a molecule: <input type=text size=40 name=whatmolecule value="">
      <br><input type=submit value='Get the Mass'>
    </form>
    <!-- PLACEHOLDER -->
</div>
</body>
</html>

"""
@app.route('/nomass')
def mass_raw():
    return clientpage
    
@app.route('/givemass', methods=['POST'])
def mass_give():
    chem = request.form['whatmolecule']
    cmass = molecule.Molecule(chem).mass()

    msg = "Molecular mass of " + chem + " is " + str(cmass)
    return clientpage.replace('<!-- PLACEHOLDER -->', msg)

