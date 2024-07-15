import asyncio
import time
from TonTools import Wallet, LsClient, TonApiClient
from ton import TonlibClient
#from ton.sync import TonlibClient


SUMMA = 5 #сколько тонов должно прийти

loop = asyncio.get_event_loop()

end_adress = "ВАШ АДРЕС КОШЕЛЬКА" #ВПИШИТЕ СВОЙ КОШЛЁК
    

async def trans_to_wallet(end_adress, SUMMA):
    provider = TonApiClient('7cf850c4c02323291022269e9377e7a2b0dde558897eda655181748047656d6f',addresses_form='user_friendly',testnet=True)
    #client = LsClient(ls_index=2, default_timeout=20)
    #await client.init_tonlib()

    new_wallet = Wallet(provider=provider, version='v4r2')

    print(new_wallet.address) #вывод кошелёк
    print(new_wallet.mnemonics)
    balance = await new_wallet.sale.get_balance()
    print(balance)
    new_wallet.
    while(SUMMA > balance):
        time.sleep(5)
        print(balance) #выводится баланс нового кошелька
        balance = await new_wallet.sale.get_balance()

    print("успешный перевод на новый кошелёк")

    await new_wallet.transfer_ton(destination_adress = end_adress, amount = SUMMA,
                              message = 'hi from @puplip')
    
    print(SUMMA,"токенов успешно переведено!")


task1 = loop.create_task(trans_to_wallet(end_adress, SUMMA))
loop.run_until_complete(asyncio.wait({task1}))

    

#asyncio.run(trans_to_wallet())
#asyncio.get_event_loop().run_until_complete(trans_to_wallet())