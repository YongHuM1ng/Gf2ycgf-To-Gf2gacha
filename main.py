import requests

uid = input('请输入游创工坊内的手机号：')
print('正在获取数据...')
r = requests.get('https://www.ycgf.cc/api/snqx/getGacha', params={'uid': uid})
data = r.json()
if data['data']:
    with open(f'gf2gacha-raw-{data["data"]["id"]}.json', 'w') as f:
        f.write(str(data['data']['pageData']).replace('_list', ''))
    print(f'gf2gacha-raw-{data["data"]["id"]}.json 导出完成，请使用gf2gacha"导入RawJson(时间倒序)"')
    input('按回车键退出...')
else:
    print('出现错误')
    input('按回车键退出...')