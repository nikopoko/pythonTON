import asyncio
import time
from TonTools import Wallet, LsClient, TonApiClient
from pytonapi import Tonapi

API_KEY = "AFH7AUTQMY4CKMAAAAAA76X6K36GZN2YICGMSAS2Q5TOIL3WRXCKQ7QCFORMLXAIXUQWICA"


ACCOUNT_ID = "kQBWtsaGAc7WQInphnDBaz6D0LqVW09ysY1rNX5RcKnI_ElC" 


SUMMA = 6 #сколько тонов должно прийти

loop = asyncio.get_event_loop()

end_adress = "ВАШ АДРЕС КОШЕЛЬКА" #ВПИШИТЕ СВОЙ КОШЛЁК
    

async def trans_to_wallet(end_adress, SUMMA):
    provider = TonApiClient(API_KEY,addresses_form='user_friendly',testnet=True)
    #client = LsClient(ls_index=2, default_timeout=20)
    #await client.init_tonlib()

    new_wallet = Wallet(provider=provider, version='v4r2')

    print(new_wallet.address) #вывод кошелёк
    print(new_wallet.mnemonics)

    tonapi = Tonapi(api_key=API_KEY,is_testnet=True)
    account = tonapi.accounts.get_info(account_id=ACCOUNT_ID)

    balance = account.balance.to_amount()
    print(f"Balance TON: {balance}")

    while(SUMMA > balance):
        time.sleep(5)
        print(f"Balance TON: {balance}") #выводится баланс нового кошелька
        balance = account.balance.to_amount()

    print("успешный перевод на новый кошелёк")

    await new_wallet.transfer_ton(destination_adress = end_adress, amount = SUMMA,
                              message = 'hi from @puplip')
    
    print(SUMMA,"токенов успешно переведено!")


task1 = loop.create_task(trans_to_wallet(end_adress, SUMMA))
loop.run_until_complete(asyncio.wait({task1}))

    

#asyncio.run(trans_to_wallet())
#asyncio.get_event_loop().run_until_complete(trans_to_wallet())