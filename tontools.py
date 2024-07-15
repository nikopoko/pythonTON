import asyncio
import time
from TonTools import Wallet, LsClient, TonApiClient


SUMMA = 5 #сколько тонов должно прийти
end_adress = "kQBWtsaGAc7WQInphnDBaz6D0LqVW09ysY1rNX5RcKnI_ElC" #ВПИШИТЕ СВОЙ КОШЛЁК
my_mnemoics= ['school', 'over', 'flight', 'ball', 'useful', 'confirm', 'fog', 'hidden', 'luxury', 'oxygen', 'car', 'climb', 'person', 'stuff', 'try', 'chef', 'code', 'anxiety', 'pelican', 'trust', 'quantum', 'oxygen', 'border', 'during']

async def trans_to_wallet():
    provider = TonApiClient('7cf850c4c02323291022269e9377e7a2b0dde558897eda655181748047656d6f')
    client = LsClient(ls_index=2, default_timeout=20)
    await client.init_tonlib()

    new_wallet = Wallet(provider=client, version='v4r2')
    new_wallet_address = new_wallet.address
    print(new_wallet_address)
    balance = await new_wallet.get_balance()
    print(balance)
    while(SUMMA > balance):
        time.sleep(5)
        print(balance) #выводится баланс нового кошелька
        balance = await new_wallet.get_balance()

    await new_wallet.transfer_ton(destination_adress = end_adress, amount = SUMMA,
                              message = 'hi from @puplip')
    
    print(SUMMA,"токенов успешно переведено!")


if __name__ == '__main__':
    asyncio.run(trans_to_wallet())