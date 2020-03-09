from flask import Flask, render_template, request, redirect, url_for,render_template
import json
app=Flask(__name__)


@app.route('/', methods=['GET','POST'])
def main():
    file=open('data.json','r')
    data=json.load(file)
    data=json.loads(data)
    datah=data['data']
    file.close()
    n=len(data['data'])
    if request.method == 'POST':
        text= (request.form['textbox'])
        name= (request.form['name'])
        
        d={ 'id':n+1,'name':name,'text':text }
        file=open('data.json','w')
        data['data'].append(d)
        datah=data['data']
        n=len(data['data'])
        data=json.dumps(data)
        json.dump(data,file)
        file.close()
        n=len(text)
    return render_template('app.html',data=datah,n=n)

if __name__ == '__main__':
   app.run(threaded=Tree, port= 5000)