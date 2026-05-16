# Programação Orientada a Objetos

## 📋 Descrição

Repositório contendo aulas, exemplos práticos e exercícios da disciplina de **Programação Orientada a Objetos** do 3º período do curso na **UNIFEI** (Universidade Federal de Itajubá).

Este projeto demonstra os principais conceitos de Orientação a Objetos (OO) através de exemplos didáticos em Python, incluindo desde conceitos básicos até padrões mais avançados.

## 🎯 Conteúdo

<!-- BLOCO:classes_conceitos_INICIO -->
### 📚 Classes e Conceitos
A pasta `Classes/` contém exemplos práticos dos principais pilares da POO:

- **`Motocicleta.py`** - Exemplo básico de classe com atributos privados e métodos
- **`Herança/`** - Exemplos de herança e reutilização de código
  - `Ex1Veiculo.py` - Hierarquia de classes de veículos
  - `ExdeHeranca.py` - Exemplos gerais de herança
- **`Polimorfismo/`** - Implementação de polimorfismo
  - `poli_ex1.py`, `poli_ex2.py`, `poli_ex3.py` - Exemplos progressivos
- **`Classe abstrata/`** - Uso de classes abstratas
  - `academico1.py` - Exemplo com classe abstrata de acadêmicos
  - `empregada.py` - Exemplo com herança de empregados
  - `formas_geo.py` - Hierarquia de formas geométricas
- **`Associações/Agreg/`** - Agregação e composição de objetos
  - `aula09.py` - Conceitos de associação
  - `FolhasDePagamento.py` - Exemplo prático com múltiplas classes
<!--BLOCO:classes_conceitos_FIM -->

### 💼 Exercícios Práticos
A pasta `Exercicios/` contém problemas para aplicar os conceitos aprendidos:

| Arquivo | Descrição |
|---------|-----------|
| `Ex5-FolhasPagamento.py` | Sistema de folha de pagamento com diferentes tipos de funcionários |
| `Ex6-Trans_Banc.py` | Sistema bancário com transações |
| `Ex6-Trans_BancParte2.py` | Continuação do sistema bancário |
| `Ex7-NotaFiscal.py` | Geração de notas fiscais |
| `Ex8-Fisio.py` | Sistema de fisioterapia |
| `Exercicio10.py` | Exercício 10 |
| `Exercício9.py` | Exercício 9 |

### 📐 Projeto Especial: Frações
A pasta `Frações/` contém uma implementação completa de uma classe para manipular frações:

- `frac1.py` - Implementação básica de frações
- `frac2.py` - Versão melhorada
- `fracMista.py` - Frações mistas

## 🛠️ Requisitos

- **Python 3.6+**
- Nenhuma dependência externa (utiliza apenas biblioteca padrão)

## 🚀 Como Usar

### Executar um arquivo específico
```bash
python Classes/Motocicleta.py
```

### Executar um exercício
```bash
python Exercicios/Ex5-FolhasPagamento.py
```

### Explorar com Jupyter (se disponível)
```bash
jupyter notebook Aula01.ipynb
```
<!-- BLOCO:conceitos_cobertos_INICIO -->
## 📖 Conceitos Cobertos

### Conceitos Fundamentais
- ✅ Classes e Objetos
- ✅ Atributos privados
- ✅ Métodos de instância
- ✅ Construtores (`__init__`)

### Pilares da POO
- ✅ Encapsulamento
- ✅ Herança
- ✅ Polimorfismo
- ✅ Abstração

### Relacionamentos entre Objetos
- ✅ Associação / Agregação / Composição

### Outros Tópicos
- ✅ Exceções
- ✅ Frações (projeto especial)
- ✅ Jupyter Notebooks
<!-- BLOCO:conceitos_cobertos_FIM -->

<!-- BLOCO:estrutura_INICIO -->
## 📁 Estrutura do Repositório

```
📄 Aula01.ipynb
📁 Classes
  📁 Associações
    📁 Agreg
      📄 FolhasDePagamento.py
      📄 aula09.py
  📁 Classe abstrata
    📄 academico1.py
    📄 empregada.py
    📄 formas_geo.py
  📁 Herança
    📄 Ex1Veiculo.py
    📄 ExdeHeranca.py
  📄 Motocicleta.py
  📁 Polimorfismo
    📄 poli_ex1.py
    📄 poli_ex2.py
    📄 poli_ex3.py
📁 Documentos
  📄 Casos de uso - Cinema.docx
  📄 Diagrama de Casos de Uso - Sist.Acadêmico.docx
  📄 Diagrama de Casos de Uso - Sist.Consultas.pdf
  📄 Diagrama de Casos de Uso - Sist.Gest.Acad.pdf
  📄 Diagrama de Classes - Sist.Consultas.pdf
  📄 Estudo de Caso - Gestão de Consultas Médicas.docx
  📄 Estudo de Casos.docx
  📄 Sistema de Gestão Acadêmica.zip
  📄 Sistema de Gestão de Consultas.zip
  📄 Template_RF.docx
📁 Exceções
  📄 exception1.py
  📄 exception2.py
  📄 exception3.py
  📄 exception4.py
  📄 exercicio_aula.py
📁 Exercicios
  📄 Ex5-FolhasPagamento.py
  📄 Ex6-Trans_Banc.py
  📄 Ex6-Trans_BancParte2.py
  📄 Ex7-NotaFiscal.py
  📄 Ex8-Fisio.py
  📄 Ex9-Exceção.py
  📄 Exercicio.py
  📄 Exercicio10.py
  📄 Exercicio8.py
  📄 Exercício9.py
📁 Frações
  📄 frac1.py
  📄 frac2.py
  📄 fracMista.py
📄 diagrama.tex
```
<!-- BLOCO:estrutura_FIM -->


## 💡 Dicas de Uso

1. **Comece pelas bases**: Explore primeiro `Motocicleta.py` para entender a estrutura básica
2. **Progressão**: Siga a ordem: Classes → Herança → Polimorfismo → Classes Abstratas → Associações
3. **Prática**: Execute os exercícios e tente modificar o código para consolidar o aprendizado
4. **Projeto**: Implemente suas próprias soluções para os problemas propostos

## 🔗 Recursos Úteis

- [Documentação Python](https://docs.python.org/3/)
- [ABC - Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- Conceitos de Design Patterns e SOLID

## 📝 Notas

Este repositório foi criado como material de estudo para a disciplina de Programação Orientada a Objetos na UNIFEI. Contém exemplos didáticos que evoluem em complexidade e demonstram os conceitos fundamentais da OO de forma progressiva.

## 👨‍💻 Autor

João Pedro Garcia Torezan  
UNIFEI - Universidade Federal de Itajubá  
3º Período

---

**Última atualização:** Maio de 2026

<!-- BLOCO:classes_conceitos_INICIO -->
## 📚 Classes e Conceitos
A pasta `Classes/` contém exemplos práticos dos principais pilares da POO:

- **`Associações/`**
- **`Classe abstrata/`**
  - `academico1.py`
  - `empregada.py`
  - `formas_geo.py`
- **`Herança/`**
  - `Ex1Veiculo.py`
  - `ExdeHeranca.py`
- **`Motocicleta.py`**
- **`Polimorfismo/`**
  - `poli_ex1.py`
  - `poli_ex2.py`
  - `poli_ex3.py`
<!-- BLOCO:classes_conceitos_FIM -->
