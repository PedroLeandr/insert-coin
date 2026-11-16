# 🎮 Insert Coin — O que fazer a seguir?

Guia rápido do trabalho de **Algoritmos e Programação**. Faz as tarefas por ordem e assinala `[x]` quando estiverem a funcionar.

## 📍 Próxima tarefa

**Arrumar os menus e corrigir a navegação.** Estavas a separar os submenus de `menu.py` para os ficheiros respetivos. Acaba isso antes de voltar ao CRUD.

## ✅ Checklist de desenvolvimento

### 1. Menus
- [ ] Menu principal e submenus funcionam.
- [ ] Cada submenu está no seu módulo (`estudios.py`, `jogos.py`, `dlcs.py`).
- [ ] É possível voltar e sair sem erros; opções inválidas não bloqueiam.

### 2. Guardar dados
- [ ] Criar `dados.json` para estúdios, jogos e DLC.
- [ ] Carregar dados ao iniciar e guardar após cada alteração.
- [ ] Usar IDs únicos. **Teste:** criar, fechar e reabrir sem perder dados.

### 3. Estúdios
- [ ] Adicionar (nome, país e comissão).
- [ ] Listar estúdios e os seus jogos.
- [ ] Editar e remover estúdios.
- [ ] Esconder a comissão sem palavra-passe válida.

### 4. Jogos e DLC
- [ ] Adicionar jogos a um estúdio (nome, género, data, cópias vendidas e preço).
- [ ] Listar e editar jogos de cada estúdio.
- [ ] Adicionar, listar e editar DLC de cada jogo.
- [ ] Ao apagar um estúdio, apagar também os seus jogos e DLC.

### 5. Pesquisa
- [ ] Pesquisar estúdios, jogos e DLC.
- [ ] Ao encontrar um DLC, mostrar o **jogo e o estúdio** a que pertence.

### 6. Relatórios e segurança
- [ ] Pedir palavra-passe para mostrar comissões e relatórios.
- [ ] Calcular a receita de cada jogo: `cópias × preço`.
- [ ] Calcular a comissão do estúdio: `receita × comissão / 100`.
- [ ] Mostrar tabela: **estúdio, %, nº jogos, cópias, receita e comissão**.
- [ ] Mostrar totais por estúdio e total geral.
- [ ] Permitir ordenar por nome, receita ou comissão.

### 7. Histórico e Undo
- [ ] Registar cada inserção, edição e remoção no histórico.
- [ ] Guardar o histórico entre execuções.
- [ ] Anular a última alteração e recuperar os dados anteriores.
- [ ] **Teste:** apagar um estúdio com jogos/DLC e usar Undo para recuperar tudo.

> **Dica:** ao criares os CRUD, guarda desde logo o estado anterior de cada alteração. Assim o Undo não exige refazer tudo no fim.

### 8. Gráficos
- [ ] Usar **Matplotlib** (biblioteca externa).
- [ ] Mostrar cópias vendidas por jogo.
- [ ] Mostrar receita por género (ou outro gráfico útil).

### 9. Finalizar
- [ ] Testar as funcionalidades, incluindo entradas erradas e reinícios.
- [ ] Fazer **Manual do Utilizador** em Typst, com imagens.
- [ ] Fazer **Documentação Técnica** em Typst, com explicação do código.
- [ ] Preparar demonstração para o exame da época normal.

---

## 🧭 Quando não souberes o que fazer

1. Procura a **primeira caixa vazia**.
2. Implementa só essa funcionalidade.
3. Testa, faz commit e assinala `[x]`.

**Regras importantes:** JSON foi autorizado pelo professor em vez de CSV; as comissões são protegidas; os dados têm de sobreviver ao reinício; o Undo tem de recuperar inserções, edições e remoções. Não gastes tempo em extras antes de concluir esta lista.
