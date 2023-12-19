import requests
import json

url = "https://api.apilayer.com/image_to_text/url?url=https://lh3.googleusercontent.com/pw/ABLVV85axRr2oyqb_vDxH8TpKKEjAXGJoFGSGMPmLsZfTLJFdbUoa-Kho68evBoACvzCIkHHzi1_0xhtF7Md4yW_XL42sX-EU9GfE8kQAQMOri-4gk6WObPsI6jFSwXVkB9Brd0yWu4PQTmvKqsjCvxM7i6WHbU7c9XF_BXK52m_357Wnmmdyg2Z_S0JEttrXZ69oFHVwJf6wOGMlFBE4jiKySPdKbGnpse1d5fsTvQeRAjZ_FXLXqQvcG1T4PRBNE36oSCM0tsHLVGmSDgB24EjHXl4yr-zKJIdtbMbSw1xKsB2GuHyshyL5rUFPEaZ9fgRWK_UmsLKnCKRGZu04sCTzJ4WiTVGyZoCXeOaTqwpDJjwrWWMNjJBrfIL17n2Mn2rY45emF7H5UPGLi2Epjdm1UUu-W5cL3npTKU50ptDNcbdxqYYtQ0iYbWPIO9pBNz2i4ywPYMrcVE1AOJ3xtBooZvzjF5fiE-lZ4gJEDYn9mtPqGKVcSXDmk2N7zRVsewubHwVf6zsCXf-Cac4PbkrfCDP_RBE7mocXrCSKjZLhOoxDgOv3DUdQxL0rom6tTrVl0PMj8Pvw1UhKbM1HprY4_DNtB5_bKHx-Eqgs7Ql9dnVW8SVdXWtyQaeYZvxk0Zb2DF6rsZZUkeePPGPR27kvh4gtPD6zXGD8Sw63EmSHR9EuvQgftJ4NYZ-JOMkl48m-CRbrCun_vb9Wb3ynLjax1RN02cOfgvGiEZYDDcJ7zkAdn1zfxPB6KYSB7igdHg4fQ-RO1npz5Ay6hmh5W5Rm_UnYBMUpyNxe1Ax3-Q9lZUQhVPtL_z6eWK0gMEaeCl7iMIdFifX8VQgw-W0jRPEGEmjWvb5RX_b_Rd_IkMzSK5Z2OJ_6edfJRkDbq1RrxXXJe1xhmrPcCV-_TNB7qXbQYdbp6QwYH-6a4S9q-9CWJJi6S6jnIpnbWCzsbbpNGQyxsp7j2B1anWr=w760-h388-s-no-gm?authuser=0"

payload = {}
headers= {
  "apikey": "bOw6cAeOWem618XC5WRlgwXP3Vl61Lqu"
}
response = requests.request("GET", url, headers=headers, data = payload)
status_code = response.status_code
result = response.text
print(type(result))
json_object = json.loads(result)
# print(json_object)
# print(type(json_object['annotations']))

# ls=['Test', 'No.', '1', 'EW', '-', '1', 'Name', 'of', 'Test', '2', 'Soil', 'gradation', 'Quality', 'Control', 'Register', 'Part', '1', 'Record', 'of', 'Tests', ':', 'Section', '-', '1', 'Earthwork', 'Abstract', 'of', 'tests', 'Conducted', 'Result', ',', 'Qualified', '(', 'Yes', '/', 'No', ')', '5', 'Test', 'No.', '3', 'Test', '1', 'Test', '2', 'Test', '3', 'Test', '4', 'Test', '5', 'Test', '6', 'Test', '7', 'Test', '8', 'Test', '9', 'Date', 'of', 'Test', '4', '11/10/23', '13/10/23', '16/10/23', '19/10/23', '24/10/23', '29/10/23', '3/11/23', '7/11/23', '19/11/23', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'If', 'No', ',', 'Page', 'No', 'and', 'Date', 'of', 'NCR', '6', 'Page', 'No', '&', 'Date', 'on', 'which', 'Test', 'Qualified', '8']

ls=json_object['annotations']

date=[]
result=[]
test_no=[]
for i in range(63,72):
    date.append(ls[i])

for i in range(72,81):
    result.append(ls[i])

i=41
while i<59:
    a=ls[i]+" "+ls[i+1]
    test_no.append(a)
    i+=2

import pandas as pd
data=pd.DataFrame({'Test No.':test_no,'Date of Test':date,'Result Qualified (Yes/No)':result})
print(data.head())
report_2=data.to_csv('report2.csv',index=False)