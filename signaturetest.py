# Python3.x
from hashlib import sha256
app_id = "SX44ZQ3WMAR794PP0POS2DAF_DEBUG" #(Please refer to required parameters section)
campaign_name = "missed_call_alerts_v3"
api_secret = "A5WV3WBXCZ01" # This is the sample key. Each app has a different secret key
signature_key = app_id+'|'+ campaign_name+'|'+ api_secret
signature = sha256(signature_key.encode('utf-8')).hexdigest()
print(signature)

