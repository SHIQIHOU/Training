import requests
import execjs
import json
import jsonpath

with open('C:\\Users\\DELL-7000\\Desktop\\baidu_translate.js', 'r', encoding = 'utf-8') as f:
    ctx = execjs.compile(f.read())

query = input('Please input your sentence:')
sign = ctx.call('e', query)

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
                  ,  'Cookie' : 'BIDUPSID=823DE7F35A0D5848C40A7F9CF8F834B1; PSTM=1547651276; BAIDUID=2951C1152787DA5D660E57571F18A668:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=hLZFJhZDJQbExCcUUtRWQyWURJWmdPWVFQMHRmeUpvaFhkSkstMjZwNXdraXBlSVFBQUFBJCQAAAAAAAAAAAEAAAAycTwBaHNxODg2NjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHAFA15wBQNeN3; APPGUIDE_8_2_2=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1581582510,1581587018,1581672646,1581673220; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1581673220; yjs_js_security_passport=c1a1b772d7e00dd3a05e812225bed386b4e92cd4_1581673221_js; delPer=0; PSINO=7'
}
data = {}
data['from'] = 'en'
data['to'] = 'zh'
data['query'] = query
data['transtype'] = 'translang'
data['simple_means_flag'] = '3'
data['sign'] = sign
data['token'] = '30aa84a426f4d113ef4555628550efb1'

response = requests.post(url, headers=headers, data=data)
json_date = json.loads(response.text)
result = jsonpath.jsonpath(json_date, '$..data')
print(result[0][0]['dst'])

