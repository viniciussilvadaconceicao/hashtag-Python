#pip install pandas oppenpyxl numpy
#pip install pyautogui
'''passo 1 - entrar no sistema da empresa
link:https://dlp.hashtagtreinamentos.com/python/intensivao/login
passo 2 fazer o loguin
passo 3 pegar/importar a base de dados
passo 4 cadatrar um produto
passo 5 repetir o passo 4 até cadastrar todos os produtos'''
 
import pyautogui
import time
'''
pyautogui.click - clicar com o mouse
pyautogui.write - escrever um texto
pyautogui.press - apertar uma tecla
payautogui.hotkey - combinação de teclas
payautogui.scroll - rolar o mouse

passo 1 - entrar no sistema da empresa
abrir o navegador
entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
'''
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=1888, y=177)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')
time.sleep(3)

#passo 2 fazer o loguin
pyautogui.click(x=731, y=465)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("viniscdeza@gmail.com")

#passar para o campo de senha
pyautogui.press('tab')
pyautogui.write("senha")

#clique no botão entrar
pyautogui.click(x=977, y=678)
time.sleep(2)
pyautogui.press('tab')

#passo 3 importar a base de dados
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)
#passo 4 - cadastrar um produto
"""para cada linha da minha tabela:"""
for linha in tabela.index:

    pyautogui.press('tab')
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press('tab')


    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, "obs"])
    if not pd.isna(obs):
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(1000)