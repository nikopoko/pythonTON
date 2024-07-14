from tonsdk.contract.wallet import Wallets, WalletVersionEnum


# Создание нового кошелька

mnemonics, pub_k, priv_k, newallet = Wallets.create(version=WalletVersionEnum.v3r2, workchain= 0)

mnemonicsOld = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] # Напишите свои данные
mnemonicsOld, pub1_k, priv1_k, Wallet1 = Wallets.from_mnemonics(mnemonics=mnemonicsOld, version=WalletVersionEnum.v3r2, workchain=0)


if __name__=='__main__':
    print(mnemonics)
    print(newallet.address.to_string(True, True, True))
