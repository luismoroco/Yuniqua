## Setup

### Mode 
- `chmod +x setup.sh`
- `bash ./setup.sh --mode <local|cluster>`

### server 

- `cd server`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip3 install requirements.txt`


### app

- `cd app`
- `npm install`
- `npm run dev`

### kind 

- You must install `KIND`
- Init cluster `kind create cluster --name=yuniqua-cluster`
