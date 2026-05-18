import os

IGNORAR = {".git", ".github", "scripts", "README.md", "__pycache__", "requirements.txt", "venv", "ENV"}

# ─────────────────────────────────────────
# Funções geradoras de cada bloco
# ─────────────────────────────────────────

def gerar_estrutura():
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
    return f"## 📁 Estrutura do Repositório\n\n```\n{estrutura}\n```"


def gerar_classes_conceitos():
    pasta = "Classes"
    if not os.path.isdir(pasta):
        return "## 📚 Classes e Conceitos\n\nPasta `Classes/` não encontrada."

    linhas = ["## 📚 Classes e Conceitos", f"A pasta `{pasta}/` contém exemplos práticos dos principais pilares da POO:", ""]

    for subpasta in sorted(os.listdir(pasta)):
        caminho_sub = os.path.join(pasta, subpasta)
        if not os.path.isdir(caminho_sub) or subpasta.startswith(".") or subpasta in IGNORAR:
            # arquivo solto dentro de Classes/
            if os.path.isfile(caminho_sub) and caminho_sub.endswith(".py"):
                linhas.append(f"- **`{subpasta}`**")
            continue

        linhas.append(f"- **`{subpasta}/`**")
        for arquivo in sorted(os.listdir(caminho_sub)):
            if arquivo.endswith(".py") and not arquivo.startswith("."):
                linhas.append(f"  - `{arquivo}`")

    return "\n".join(linhas)


def gerar_conceitos_cobertos():
    # Detecta quais conceitos existem com base nas pastas e arquivos presentes
    conceitos_fundamentais = {
        "Classes e Objetos":            lambda: any(f.endswith(".py") for f in os.listdir(".") if os.path.isfile(f)) or os.path.isdir("Classes"),
        "Atributos privados":           lambda: os.path.isdir("Classes"),
        "Métodos de instância":         lambda: os.path.isdir("Classes"),
        "Construtores (`__init__`)":    lambda: os.path.isdir("Classes"),
    }
    pilares = {
        "Encapsulamento":               lambda: os.path.isdir("Classes"),
        "Herança":                      lambda: os.path.isdir(os.path.join("Classes", "Herança")),
        "Polimorfismo":                 lambda: os.path.isdir(os.path.join("Classes", "Polimorfismo")),
        "Abstração":                    lambda: os.path.isdir(os.path.join("Classes", "Classe abstrata")),
    }
    relacionamentos = {
        "Associação / Agregação / Composição": lambda: os.path.isdir(os.path.join("Classes", "Associações")),
    }
    extras = {
        "Exceções":                     lambda: os.path.isdir("Exceções"),
        "Frações (projeto especial)":   lambda: os.path.isdir("Frações"),
        "Jupyter Notebooks":            lambda: any(f.endswith(".ipynb") for f in os.listdir(".")),
    }

    def marca(fn):
        return "✅" if fn() else "⬜"

    linhas = ["## 📖 Conceitos Cobertos", "", "### Conceitos Fundamentais"]
    for nome, fn in conceitos_fundamentais.items():
        linhas.append(f"- {marca(fn)} {nome}")

    linhas += ["", "### Pilares da POO"]
    for nome, fn in pilares.items():
        linhas.append(f"- {marca(fn)} {nome}")

    linhas += ["", "### Relacionamentos entre Objetos"]
    for nome, fn in relacionamentos.items():
        linhas.append(f"- {marca(fn)} {nome}")

    linhas += ["", "### Outros Tópicos"]
    for nome, fn in extras.items():
        linhas.append(f"- {marca(fn)} {nome}")

    return "\n".join(linhas)


# ─────────────────────────────────────────
# Motor de substituição de blocos
# ─────────────────────────────────────────

BLOCOS = {
    "estrutura":         gerar_estrutura,
    "classes_conceitos": gerar_classes_conceitos,
    "conceitos_cobertos": gerar_conceitos_cobertos,
}

def substituir_bloco(conteudo, nome, novo_conteudo):
    inicio = f"<!-- BLOCO:{nome}_INICIO -->"
    fim    = f"<!-- BLOCO:{nome}_FIM -->"
    bloco  = f"{inicio}\n{novo_conteudo}\n{fim}"

    if inicio in conteudo and fim in conteudo:
        antes        = conteudo.split(inicio, 1)[0]   # tudo antes do marcador de início
        resto        = conteudo.split(inicio, 1)[1]   # tudo depois do marcador de início
        depois       = resto.split(fim, 1)[1]         # tudo depois do marcador de fim
        return antes + bloco + depois
    else:
        return conteudo.rstrip() + f"\n\n{bloco}\n"

# ─────────────────────────────────────────
# Execução
# ─────────────────────────────────────────

with open("README.md", "r", encoding="utf-8") as f:
    conteudo = f.read()

for nome, fn in BLOCOS.items():
    conteudo = substituir_bloco(conteudo, nome, fn())

with open("README.md", "w", encoding="utf-8") as f:
    f.write(conteudo)

print("README atualizado!")
