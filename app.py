import pyautogui
import time

# Configurações
mensagem_commit = "First commit"
link_repositorio_remoto = "https://github.com/italobovier/teste_do.git"  # Substitua pelo link do repositório remoto
diretorio_projeto = r'C:\Users\Aluno Manhã\Documents\envio_github'

# Abra o terminal integrado do Visual Studio Code
pyautogui.hotkey('ctrl', 'shift', '`')  # Abre um novo terminal
time.sleep(2)  # Espera o terminal abrir

# Adicione todos os arquivos ao commit
pyautogui.typewrite('git init')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('git add .')
pyautogui.press('enter')
time.sleep(1)

# Crie o commit
pyautogui.typewrite(f'git commit -m "{mensagem_commit}"')
pyautogui.press('enter')
time.sleep(2)

# Mude o nome da branch para 'main'
pyautogui.typewrite('git branch -M main')
pyautogui.press('enter')
time.sleep(1)

# Adicione o repositório remoto
pyautogui.typewrite(f'git remote add origin {link_repositorio_remoto}')
pyautogui.press('enter')
time.sleep(1)

# Empurre para o repositório remoto
pyautogui.typewrite('git push -u origin main')
pyautogui.press('enter')
time.sleep(5)

# Feche o terminal
pyautogui.typewrite('exit')
pyautogui.press('enter')

print("Programa enviado para o repositório remoto com sucesso!")
