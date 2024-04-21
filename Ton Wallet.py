from tonsdk.contract.wallet import WalletVersionEnum, Wallets
from tonsdk.utils import bytes_to_b64str
from tonsdk.crypto import mnemonic_new
from colorama import init, Fore, Back, Style
import webbrowser

init()

print(Fore.GREEN + """                      Bản quyền thuộc về https://t.me/Justice0210
            Ngoài ra mình bán tool check live Twitter (X), Tool đọc mail,
                            ae nào cần có thể ủng hộ mình :3""" + Style.RESET_ALL)

webbrowser.open('https://youtu.be/eYEZZ5huOBo') 
wallet_workchain = 0
wallet_version = WalletVersionEnum.v3r2
f = open('Ton Wallet.txt','a')
quantity = int(input('Nhập số ví cần tạo: '))
for i in range(quantity):
    wallet_mnemonics = mnemonic_new()

    _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(
        wallet_mnemonics, wallet_version, wallet_workchain)
    query = wallet.create_init_external_message()
    base64_boc = bytes_to_b64str(query["message"].to_boc(False))
    address = wallet.address.to_string(True, True, False)
    print(f"""
    {i + 1}
    Mnemonic: {' '.join(wallet_mnemonics)}
    Bounceable, url safe, user friendly address: {address}

    """)
    f.write(f'{address} | {" ".join(wallet_mnemonics)}\n')

