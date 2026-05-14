import os

# Pastas e arquivos a ignorar
IGNORAR = {".git", ".github", "scripts", "README.md", "__pycache__"}

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

estrutura = "\n".join(listar())

readme = f"""# Meu Repositório

## 📂 Estrutura

"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README atualizado!")
