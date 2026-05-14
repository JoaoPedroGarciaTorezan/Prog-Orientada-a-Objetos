import os

# Pastas e arquivos a ignorar
IGNORAR = {".git", ".github", "scripts", "README.md", "__pycache__", "requirements.txt", "venv", "ENV"}

def listar(caminho=".", nivel=0):
    linhas = []
    try:
        itens = sorted(os.listdir(caminho))
    except PermissionError:
        return linhas

    for item in itens:
        if item in IGNORAR or item.startswith("."):
            continue

        caminho_completo = os.path.join(caminho, item)
        prefixo = "  " * nivel + ("📁 " if os.path.isdir(caminho_completo) else "📄 ")
        linhas.append(f"{prefixo}{item}")

        if os.path.isdir(caminho_completo):
            linhas.extend(listar(caminho_completo, nivel + 1))

    return linhas

with open("README.md", "r", encoding="utf-8") as f:
    conteudo = f.read()

estrutura = "\n".join(listar())
nova_secao = f"## 📁 Estrutura do Repositório\n\n```\n{estrutura}\n```"

INICIO = "<!-- ESTRUTURA_INICIO -->"
FIM = "<!-- ESTRUTURA_FIM -->"

novo_bloco = f"{INICIO}\n{nova_secao}\n{FIM}"

if INICIO in conteudo and FIM in conteudo:
    # Substitui o bloco existente
    antes = conteudo.split(INICIO)[0]
    depois = conteudo.split(FIM)[1]
    novo_conteudo = antes + novo_bloco + depois
else:
    # Adiciona ao final se os marcadores não existirem ainda
    novo_conteudo = conteudo.rstrip() + f"\n\n{novo_bloco}\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(novo_conteudo)

print("README atualizado!")
