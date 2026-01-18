from flask import Flask,jsonify,request
from flask_cors import CORS
import phonenumbers
from phonenumbers import geocoder,carrier,timezone,number_type,PhoneNumberType
def check_phone(number):
    parsed=phonenumbers.parse(number ,"US")
    try:
        valid=phonenumbers.is_valid_number(parsed)
        dit={
            "valid":valid,
            "location":geocoder.description_for_number(parsed,"en") if geocoder.description_for_number(parsed,"en") else "Not found" ,
            "carrier":carrier.name_for_number(parsed,'en') if carrier.name_for_number(parsed,'en') else "Not found" ,
            "time_zone":timezone.time_zones_for_number(parsed) if timezone.time_zones_for_number(parsed) else "Not found",
            "number_type":number_type(parsed),
            "country_code":parsed.country_code
            }
        return dit
    except Exception as e:
        return{"msg":"error"}
app=Flask(__name__)
CORS(app)
@app.route('/')
def api_home():
    return jsonify({
        "message":"hello world",
        "status":"success"
    })

@app.route("/phone",methods=["GET"])
def phone():
    number=request.args.get("number")
    dic=check_phone(number)
    return jsonify(dic)
if __name__=="__main__":
    app.run()
