from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "Hello, world from Flask!"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
    
    
    
    
    # import time
#while True:#    time.sleep(1)

#print("hello python")
