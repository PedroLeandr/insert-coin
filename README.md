# 🎮 Insert Coin

**Insert Coin** é uma aplicação de terminal desenvolvida em Python para gerir uma loja digital de videojogos de estúdios independentes.

O programa permite organizar estúdios, jogos e DLC, acompanhar vendas e calcular as comissões da loja.

> 🚧 **Estado:** em desenvolvimento — trabalho prático de Algoritmos e Programação (2026/2027).

## ✨ Funcionalidades previstas

- Gestão de estúdios, jogos e DLC (adicionar, consultar, editar e remover).
- Armazenamento persistente dos dados em JSON.
- Pesquisa de estúdios, jogos e DLC.
- Relatórios de vendas, receitas e comissões.
- Proteção das informações financeiras por palavra-passe.
- Gráficos de desempenho do catálogo.
- Histórico de alterações e possibilidade de as anular (*Undo*).

## 🛠️ Tecnologias

- **Python** — aplicação e lógica de funcionamento.
- **JSON** — armazenamento dos dados.
- **Matplotlib** — geração de gráficos.
- **Typst** — documentação do projeto.

## 🚀 Como executar

### 1. Obter o projeto

```bash
git clone https://github.com/PedroLeandr/insert-coin.git
cd insert-coin
```

### 2. Instalar a dependência dos gráficos

```bash
python -m pip install matplotlib
```

### 3. Iniciar a aplicação

```bash
python main.py
```

> É necessário ter o Python instalado. Os comandos e algumas funcionalidades podem mudar enquanto o projeto estiver em desenvolvimento.

## 💾 Armazenamento

Os dados dos estúdios, jogos, DLC e histórico são guardados em ficheiros **JSON** para permanecerem disponíveis após fechar o programa.

O enunciado original prevê CSV, mas a utilização de JSON foi autorizada pelo professor.

## 📚 Documentação

Estão previstos dois documentos em **Typst**:

- **Manual do Utilizador:** instruções de utilização com imagens.
- **Documentação Técnica:** organização e explicação do código.

O desenvolvimento pode ser acompanhado no [roadmap do projeto](ROADMAP_INSERT_COIN.md).
