import pyautogui
import time
import subprocess

# Configurações
mensagem_commit = "First commit"
link_repositorio_remoto = "https://github.com/italobovier/teste_do.git"
diretorio_projeto = r'C:\Users\Aluno Manhã\Documents\envio_github'

# Abre o Git Bash
subprocess.Popen(['C:\\Program Files\\Git\\bin\\bash.exe'])  # Caminho padrão para Git Bash
time.sleep(2)  # Espera o Git Bash abrir

# Navegue até o diretório do projeto
pyautogui.typewrite(f'cd "{diretorio_projeto}"')
pyautogui.press('enter')
time.sleep(1)

# Inicializa o repositório Git
pyautogui.typewrite('git init')
pyautogui.press('enter')
time.sleep(1)

# Adiciona todos os arquivos ao commit
pyautogui.typewrite('git add .')
pyautogui.press('enter')
time.sleep(1)

# Cria o commit
pyautogui.typewrite(f'git commit -m "{mensagem_commit}"')
pyautogui.press('enter')
time.sleep(2)

# Muda o nome da branch para 'main'
pyautogui.typewrite('git branch -M main')
pyautogui.press('enter')
time.sleep(1)

# Adiciona o repositório remoto
pyautogui.typewrite(f'git remote add origin {link_repositorio_remoto}')
pyautogui.press('enter')
time.sleep(1)

# Empurra para o repositório remoto
pyautogui.typewrite('git push -u origin main')
pyautogui.press('enter')
time.sleep(5)

# Fecha o Git Bash
pyautogui.typewrite('exit')
pyautogui.press('enter')

print("Programa enviado para o repositório remoto com sucesso!")
cd "C:\Users\Aluno Manh\Documents\envio_github"