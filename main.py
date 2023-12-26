import requests 
import json

file_wal = 'wal.txt'


def write_t(text):
    with open('wal_true.txt', 'a') as f:
        f.write(f'{text}\n')

def wallett(file):
    try:
        private = open(file,'r').read().splitlines()
        wallet = private[00]
        write_t(wallet)
        return wallet
    except:
        print(f'Кошельки кончились {file}')

def wallett_del(file):
    ish = open(file,'r').readlines()
    del ish[00]
    with open(file, "w") as file:
        file.writelines(ish)


def chek(wal:str):

    params = {
        'address': f'{wal}',
    }
    response = json.loads(requests.get('https://starkrocket.xyz/api/check_wallet', params=params).content)['result']['points']
    print(f'{wal} points = {response}')

def main():
    while True:
        wal = wallett(file_wal)
        chek(wal)
        wallett_del(file_wal)

if __name__ == '__main__':
    main()