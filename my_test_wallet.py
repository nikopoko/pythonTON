import asyncio
import time
from TonTools import Wallet, LsClient, TonApiClient

async def wal():
    provider = TonApiClient('cb663641775f46d27ad9aa306cf39217d7a3adc04a23087f1cdfb3c632093e2d','user_friendly',True)
    
    

    end_adress = "kQBWtsaGAc7WQInphnDBaz6D0LqVW09ysY1rNX5RcKnI_ElC" #ВПИШИТЕ СВОЙ КОШЛЁК
    my_mnemoics= ['school', 'over', 'flight', 'ball', 'useful', 'confirm', 'fog', 'hidden', 'luxury', 'oxygen', 'car', 'climb', 'person', 'stuff', 'try', 'chef', 'code', 'anxiety', 'pelican', 'trust', 'quantum', 'oxygen', 'border', 'during']

    my_wallet = Wallet(provider,end_adress,my_mnemoics ,'v4r2')
    print(await my_wallet.get_transactions())
asyncio.run(wal())