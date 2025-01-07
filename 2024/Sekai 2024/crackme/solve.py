import pyrebase

config = {
    "apiKey": "AIzaSyCR2Al5_9U5j6UOhqu0HCDS0jhpYfa2Wgk",
    "authDomain": "crackme-1b52a.firebaseapp.com",
    "projectId": "crackme-1b52a",
    "storageBucket": "crackme-1b52a.appspot.com",
    "messagingSenderId": "544041293350",
    "appId": "1:544041293350:web:2abc55a6bb408e4ff838e7",
    "measurementId": "G-RDD86JV32R",
    "databaseURL": "https://crackme-1b52a-default-rtdb.firebaseio.com"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
try:
    user = auth.sign_in_with_email_and_password("admin@sekai.team", "s3cr3t_SEKAI_P@ss")
    id_token = user['idToken']
    uid = user['localId']
except Exception as e:
    print(f"Authentication failed: {e}")
    exit()
db = firebase.database()
try:
    data = db.child("users").child(uid).child("flag").get(id_token)
    print(data.val())
except Exception as e:
    print(f"Database fetch failed: {e}")
# SEKAI{15_React_N@71v3_R3v3rs3_H@RD???}
