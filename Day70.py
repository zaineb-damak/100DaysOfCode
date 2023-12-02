import os

os.environ['admin_user'] = 'admin'
os.environ['password_admin'] = 'adpass'

os.environ['normal_user'] = 'normal'
os.environ['password_normal'] = 'normpass' 

user = input('enter username: ')
psw = input('enter password : ')

if user == os.environ['admin_user'] and psw == os.environ['password_admin']:
    print('hello admin')
elif user == os.environ['normal_user'] and psw == os.environ['password_normal']:
    print('hello normy')
else:
    print('account does not exist')