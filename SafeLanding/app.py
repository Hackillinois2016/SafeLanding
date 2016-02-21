import os
import re
import runnerClass
from flask import Flask,render_template, request,json
from flask.ext.scss import Scss

app = Flask(__name__)
app.config['DEBUG'] = True
Scss(app, static_dir='static/css', asset_dir='static/scss')

@app.route('/')
def query():
    return render_template('query.html')

@app.route('/searchAirport', methods=['POST'])
def searchAirport():
    airport =  request.form['Airport'];
    airport = airport[airport.find("(")+1:airport.find(")")];
    dest = runnerClass.giveOrigin(airport);
    
    fullNameList = open("apList.txt", 'r')
    
    nameListTuple = []
    
    for nameList in fullNameList:
        nameListSplit = nameList.split("(")
        nameTuple = [nameListSplit[0], nameListSplit[1][:-1]];
        nameListTuple.append(nameTuple)
    if dest == None:
        return "";
    destFile = open("static/txt/destFile.txt", 'w')
    dFile = open("static/txt/dFile.txt", 'w')
    for x in dest:
        x += ")"
        found = filter(lambda y: y[1] == x, nameListTuple)
        if found:
            x = found[0][0] + "(" + x
            destFile.write("<option>" + x + "</option>\n")
            dFile.write(x + "\n")
    destFile.close()
    return "";
    
@app.route('/searchDest', methods=['POST'])
def searchDest():
    destin = request.form['Destination'];
    destin = destin[destin.find("(")+1:destin.find(")")];
    dest = open("static/txt/dFile.txt", 'r');
    allDest = [];
    for line in dest:
        allDest.append(line[line.find("(")+1:line.find(")")]);
    tupleList = runnerClass.giveDestination(destin,allDest);
    if tupleList == []:
        return "";
    else:
        dFile = open("static/txt/diseases.txt", 'w');
        for t in tupleList:
            dFile.write(t[0] + "," + str(t[1])+ "\n");
        dFile.close();
        return "";
    

if __name__=="__main__":
    app.debug = True
    app.run()
