from flask import Flask, json, request
import index3
import os
import uuid
# companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/', methods=['POST'])
def process():
    tmp_name = str(uuid.uuid4())
    uploads_dir="./audio2process"

    file=request.files["audio"]
    #fileName=file.filename
    fileName=tmp_name+"."+file.filename.split(".")[-1]

    file.save(os.path.join(uploads_dir, fileName))
    os.chmod(os.path.join(uploads_dir, fileName),0o777)


    data=index3.process(uploads_dir,fileName)

    #LIMPIAR FICHEROS
    # os.rename(os.path.join(uploads_dir, fileName),os.path.join(delete_dir, fileName))
    # os.remove(os.path.join(delete_dir, fileName))
    # os.remove(os.path.join(png_dir, tmp_name+".png"))

    return data
    #return params

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8000)