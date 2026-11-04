# Insert Coin — Plano Completo do Trabalho Prático

> **Disciplina:** Algoritmos e Programação  
> **Ano letivo:** 2026/2027  
> **Linguagem:** Python  
> **Interface:** Terminal / linha de comandos  
> **Persistência:** JSON  
> **Documentação final:** Typst (2 documentos separados)  
> **Estado:** Planeamento

---

## 1. Visão geral

A **Insert Coin** é uma loja digital de videojogos de estúdios independentes. A loja recebe uma comissão sobre as vendas dos jogos de cada estúdio parceiro.

A aplicação deverá permitir gerir estúdios, jogos e DLC, consultar e alterar os dados, pesquisar o catálogo, calcular receitas e comissões, consultar o histórico, anular alterações e gerar gráficos.

**Objetivo:** cumprir todos os requisitos do trabalho prático, com uma aplicação funcional, dados persistentes, código compreensível e documentação adequada para apresentação e avaliação.

### 1.1. Decisão sobre armazenamento

O enunciado original refere ficheiros `.csv`, mas **o professor autorizou a utilização de JSON**, desde que exista **persistência dos dados**. Assim:

- Os dados são carregados dos ficheiros JSON quando o programa inicia.
- Cada inserção, edição, remoção ou anulação é guardada no disco.
- Ao fechar e voltar a abrir o programa, os dados e o histórico continuam disponíveis.
- Não é necessária uma base de dados externa.

### 1.2. Critérios para considerar o projeto concluído

- Todos os requisitos obrigatórios funcionam.
- A aplicação não perde dados após reiniciar.
- Um utilizador sem autorização não consegue consultar comissões ou relatórios financeiros.
- É possível anular inserções, edições e remoções, incluindo operações que afetem um estúdio inteiro.
- Os cálculos e os totais são corretos.
- Os menus suportam entradas inválidas sem terminar inesperadamente.
- Existem **dois documentos finais em Typst**, um para o utilizador e outro técnico para o professor.
- A equipa consegue explicar e demonstrar o funcionamento de cada módulo.

---

## 2. Requisitos funcionais

### RF01 — Menu principal

- [x] Menu navegável na linha de comandos.
- [ ] Submenus organizados por funcionalidade.
- [x] Opção de voltar atrás e de sair.
- [ ] Tratamento de opções inválidas.

### RF02 — Consultar estúdios

- [ ] Mostrar o nome e o país de cada estúdio.
- [ ] Mostrar os jogos associados a cada estúdio.
- [ ] Mostrar a percentagem da comissão **apenas após autenticação válida**.
- [ ] Apresentar uma mensagem adequada quando não existem estúdios.

### RF03 — Consultar jogos e DLC

- [ ] Listar os jogos de um estúdio.
- [ ] Mostrar nome, género, data de lançamento, cópias vendidas e preço de cada jogo.
- [ ] Mostrar os DLC associados a cada jogo.
- [ ] Tratar estúdios sem jogos e jogos sem DLC.

### RF04 — Persistência em JSON

- [ ] Carregar os dados ao iniciar.
- [ ] Criar a estrutura de dados inicial quando não existem ficheiros.
- [ ] Guardar alterações imediatamente.
- [ ] Preservar corretamente acentos e caracteres portugueses.
- [ ] Tratar erros de leitura, escrita e ficheiros JSON inválidos sem destruir dados.

### RF05 — Inserir dados

- [ ] Adicionar estúdios.
- [ ] Adicionar jogos a estúdios existentes.
- [ ] Adicionar DLC a jogos existentes.
- [ ] Criar identificadores únicos.
- [ ] Validar os campos introduzidos.

### RF06 — Editar dados

- [ ] Editar nome, país e comissão de um estúdio.
- [ ] Editar nome, género, lançamento, cópias vendidas e preço de um jogo.
- [ ] Editar os dados de um DLC.
- [ ] Guardar automaticamente cada alteração.

### RF07 — Remover dados

- [ ] Remover um estúdio, incluindo os seus jogos e DLC.
- [ ] Permitir remover jogos e DLC individualmente (funcionalidade complementar útil).
- [ ] Pedir confirmação antes de eliminar.
- [ ] Registar a remoção para permitir a sua anulação.

### RF08 — Pesquisar

- [ ] Pesquisar estúdios pelo nome.
- [ ] Pesquisar jogos pelo nome.
- [ ] Pesquisar DLC pelo nome.
- [ ] Mostrar, em cada resultado de DLC, o respetivo jogo e estúdio.
- [ ] Permitir correspondências parciais, sem distinguir maiúsculas de minúsculas.
- [ ] Informar quando não existem resultados.

### RF09 — Relatório financeiro protegido

- [ ] Pedir uma palavra-passe válida para aceder ao relatório.
- [ ] Calcular a receita de cada jogo: `cópias_vendidas × preço`.
- [ ] Calcular a receita de cada estúdio: soma das receitas dos seus jogos.
- [ ] Calcular a comissão da loja: `receita_estudio × (percentagem_comissao / 100)`.
- [ ] Mostrar tabela com nome, percentagem, número de jogos, cópias, receita e comissão.
- [ ] Incluir totais por estúdio e totais gerais.
- [ ] Permitir ordenação por nome, receita e comissão (e, opcionalmente, cópias).
- [ ] Formatar valores monetários com duas casas decimais.

> **Nota:** o enunciado não define preço nem vendas de DLC; por isso, a receita obrigatória é calculada a partir dos **jogos**, não dos DLC.

### RF10 — Histórico de ações

- [ ] Registar inserções, edições e remoções.
- [ ] Guardar a data e hora, o tipo e a descrição de cada ação.
- [ ] Consultar o histórico no terminal.
- [ ] Manter o histórico persistente entre execuções.

### RF11 — Anular ações (Undo)

- [ ] Anular a última alteração ainda não anulada.
- [ ] Restaurar os dados exatamente ao estado anterior à ação.
- [ ] Restaurar também jogos e DLC ao anular a remoção de um estúdio.
- [ ] Atualizar o JSON após a anulação.
- [ ] Assinalar no histórico que a ação foi anulada.
- [ ] Tratar o caso de não existirem ações para anular.

### RF12 — Gráficos

- [ ] Gerar pelo menos um gráfico com **Matplotlib**, biblioteca externa ao Python padrão.
- [ ] Gráfico de barras: cópias vendidas por jogo.
- [ ] Gráfico de barras ou circular: receita por género.
- [ ] Adicionar títulos, legendas e etiquetas legíveis.
- [ ] Tratar a ausência de dados.

---

## 3. Requisitos não funcionais

- **Facilidade de utilização:** menus consistentes e mensagens claras.
- **Organização:** funções pequenas, nomes compreensíveis e responsabilidades separadas.
- **Robustez:** validação de números, datas, respostas e ficheiros.
- **Integridade:** nenhuma operação pode deixar associações inválidas entre estúdios, jogos e DLC.
- **Persistência:** uma alteração confirmada tem de sobreviver ao reinício da aplicação.
- **Segurança:** não revelar comissões sem autenticação; não publicar a palavra-passe real no repositório.
- **Documentação:** código explicado, manual ilustrado e instruções de execução.

---

## 4. Tecnologias

| Tecnologia | Função | Origem |
|---|---|---|
| `Python 3` | Aplicação e lógica | Linguagem principal |
| `json` | Ler e escrever dados | Biblioteca padrão |
| `pathlib` | Gerir caminhos de ficheiros | Biblioteca padrão |
| `datetime` | Datas, horas e validação | Biblioteca padrão |
| `copy` | Cópias independentes para Undo | Biblioteca padrão |
| `decimal` | Cálculos monetários com controlo do arredondamento | Biblioteca padrão |
| `hashlib` e `secrets` | Armazenamento/verificação segura da palavra-passe, se implementado | Biblioteca padrão |
| `matplotlib` | Gráficos | Biblioteca externa obrigatória para os gráficos |
| `Typst` | Manual e documentação técnica | Ferramenta de documentação |

**Instalação da dependência de gráficos:**

```bash
python -m pip install matplotlib
```

---

## 5. Estrutura planeada de pastas

```text
insert-coin/
├── main.py                     # Entrada e execução do programa
├── menu.py                     # Menu principal e submenus
├── estudios.py                 # Operações sobre estúdios
├── jogos.py                    # Operações sobre jogos
├── dlcs.py                     # Operações sobre DLC
├── dados.py                    # Leitura, escrita e validação do JSON
├── pesquisas.py                # Pesquisas no catálogo
├── relatorios.py               # Receitas, comissões e tabelas
├── graficos.py                 # Gráficos Matplotlib
├── historico.py                # Histórico e anulação de operações
├── seguranca.py                # Autenticação e permissões
├── validacoes.py               # Funções reutilizáveis de validação
├── data/
│   ├── dados.json              # Catálogo persistente
│   └── historico.json          # Registo e informação para Undo
├── docs/
│   ├── manual_utilizador.typ   # Documento visual para o cliente
│   ├── documentacao_tecnica.typ # Documento do código para o professor
│   ├── imagens/               # Capturas de ecrã reais da aplicação
│   └── export/                # PDF finais produzidos pelo Typst
├── README.md                   # Como instalar, executar e navegar
└── PLANO_INSERT_COIN.md        # Este plano de desenvolvimento
```

> A estrutura é um **objetivo**, não uma exigência para o primeiro dia. Começar com menos módulos e separar apenas quando houver código suficiente é aceitável.

---

## 6. Estrutura dos dados JSON

### 6.1. `data/dados.json`

Um único ficheiro pode guardar os estúdios e os seus jogos e DLC de forma hierárquica:

```json
{
  "proximos_ids": {
    "estudio": 3,
    "jogo": 3,
    "dlc": 2
  },
  "estudios": [
    {
      "id": 1,
      "nome": "Ctrl+Z Games",
      "pais": "Portugal",
      "comissao": 30,
      "jogos": [
        {
          "id": 1,
          "nome": "Pixel Adventure",
          "genero": "Aventura",
          "lancamento": "2026-05-15",
          "copias_vendidas": 1000,
          "preco": 19.99,
          "dlcs": [
            {
              "id": 1,
              "nome": "Expansion Pack"
            }
          ]
        },
        {
          "id": 2,
          "nome": "Neon Racer",
          "genero": "Corridas",
          "lancamento": "2025-11-01",
          "copias_vendidas": 500,
          "preco": 12.5,
          "dlcs": []
        }
      ]
    },
    {
      "id": 2,
      "nome": "Patch Day One",
      "pais": "Espanha",
      "comissao": 25,
      "jogos": []
    }
  ]
}
```

**Relações:**

- Cada estúdio tem uma lista `jogos`.
- Cada jogo tem uma lista `dlcs`.
- Ao eliminar um estúdio do catálogo, eliminam-se automaticamente os seus jogos e DLC.
- Os IDs identificam cada entidade, independentemente de existirem nomes repetidos.
- Os contadores `proximos_ids` evitam reutilizações acidentais.

**Validações propostas:**

- Nome e país: texto não vazio.
- Comissão: número entre 0 e 100.
- Cópias: inteiro maior ou igual a 0.
- Preço: número maior ou igual a 0.
- Lançamento: data válida no formato `AAAA-MM-DD`.
- IDs: positivos e únicos dentro do respetivo tipo.

### 6.2. `data/historico.json`

A estratégia inicial recomendada é guardar, para cada operação, **uma cópia completa do catálogo antes da alteração**. É simples de explicar e fiável para um trabalho académico com poucos registos.

Exemplo conceptual:

```json
{
  "acoes": [
    {
      "id": 1,
      "data_hora": "2026-10-31T14:30:00",
      "tipo": "editar",
      "entidade": "jogo",
      "descricao": "Alterado o preço de Pixel Adventure",
      "anulada": false,
      "estado_anterior": {
        "proximos_ids": {
          "estudio": 3,
          "jogo": 3,
          "dlc": 2
        },
        "estudios": []
      }
    }
  ]
}
```

> `estado_anterior` acima é apenas um **exemplo de formato**: numa ação real, contém o catálogo completo imediatamente antes dessa ação. A lista vazia é ilustrativa, não um estado correto para a edição apresentada.

**Fluxo de alteração:**

1. Validar a operação.
2. Criar uma cópia do estado atual dos dados.
3. Aplicar a alteração em memória.
4. Guardar os dados atualizados e o registo da alteração.
5. Informar o utilizador do resultado.

**Fluxo de Undo:**

1. Encontrar a última ação anulável ainda ativa.
2. Restaurar o respetivo `estado_anterior`.
3. Persistir o catálogo restaurado no ficheiro de dados.
4. Marcar a ação como anulada e guardar o histórico.
5. Confirmar ao utilizador que a reposição foi efetuada.

**Cuidado de implementação:** as gravações dos dois ficheiros precisam de tratamento de erros e de uma estratégia de recuperação para evitar inconsistências se a aplicação falhar entre a escrita de um e do outro. O projeto pode começar com gravações cuidadosas e cópias de segurança, sendo esta robustez testada antes da entrega.

### 6.3. Regras de escrita dos ficheiros

- Utilizar `encoding="utf-8"` e `ensure_ascii=False`.
- Utilizar `indent=2` ou `indent=4` para facilitar a leitura.
- Preferir escrever primeiro num ficheiro temporário e substituí-lo só quando a escrita terminar corretamente.
- Nunca transformar automaticamente um JSON inválido num catálogo vazio sem avisar, porque isso poderia destruir informação.
- Evitar editar os JSON manualmente enquanto a aplicação está aberta.

---

## 7. Navegação da aplicação

```text
================================================
                 INSERT COIN
================================================
  1. Gerir estúdios
  2. Gerir jogos
  3. Gerir DLC
  4. Pesquisar catálogo
  5. Relatórios financeiros [protegido]
  6. Gráficos
  7. Histórico de ações
  8. Anular última alteração
  0. Sair
================================================
Escolha uma opção:
```

### 7.1. Submenus esperados

**Estúdios:** listar, consultar detalhes, adicionar, editar, remover, voltar.  
**Jogos:** listar por estúdio, consultar, adicionar, editar, remover, voltar.  
**DLC:** listar por jogo, adicionar, editar, remover, voltar.  
**Pesquisar:** estúdio, jogo, DLC, voltar.  
**Relatórios:** autenticação, apresentação da tabela, ordenação, voltar.  
**Gráficos:** cópias por jogo, receitas por género, voltar.  
**Histórico:** listar ações e consultar estado (incluindo anulações).

### 7.2. Comportamento esperado

- O menu principal mantém-se aberto até ser escolhida a opção de sair.
- Uma ação concluída regressa ao menu respetivo.
- Uma entrada inválida apresenta uma mensagem e permite repetir.
- A remoção de dados pede confirmação explícita.
- Não revelar o valor das comissões num menu ou mensagem que não tenha validação de acesso.

---

## 8. Organização do código e responsabilidades

| Módulo | Responsabilidades principais |
|---|---|
| `main.py` | Inicializar dados e iniciar o programa. |
| `menu.py` | Mostrar menus, recolher opções e chamar funções. |
| `dados.py` | Carregar, validar e guardar catálogo e histórico. |
| `estudios.py` | Listar, adicionar, editar e remover estúdios. |
| `jogos.py` | Listar, adicionar, editar e remover jogos. |
| `dlcs.py` | Listar, adicionar, editar e remover DLC. |
| `pesquisas.py` | Encontrar dados e apresentar relações. |
| `relatorios.py` | Calcular receitas, comissões, totais e ordenações. |
| `graficos.py` | Preparar dados e gerar gráficos. |
| `historico.py` | Registar mudanças, consultar histórico e anular. |
| `seguranca.py` | Validar palavra-passe e restringir acesso. |
| `validacoes.py` | Validar texto, preços, datas e números. |

**Regra de organização:** a lógica de negócio não deve ficar toda misturada com os `input()` e `print()`. Isto simplifica testes, manutenção e documentação.

### 8.1. Algumas funções previstas

```python
# Nomes ilustrativos; implementação faseada.
carregar_dados()
guardar_dados(dados)

listar_estudios(dados)
adicionar_estudio(dados, nome, pais, comissao)
remover_estudio(dados, estudio_id)

adicionar_jogo(dados, estudio_id, jogo)
editar_jogo(dados, jogo_id, alteracoes)

adicionar_dlc(dados, jogo_id, nome)
pesquisar_dlc(dados, termo)

calcular_receita_jogo(jogo)
calcular_receita_estudio(estudio)
calcular_comissao_estudio(estudio)

registar_acao(historico, acao, estado_anterior)
anular_ultima_acao(dados, historico)
```

> Esta lista serve para orientar o desenho; não obriga a criar funções ou ficheiros vazios antes de serem necessários.

---

## 9. Regras de cálculo e apresentação

### 9.1. Fórmulas

```text
receita_jogo = copias_vendidas * preco

receita_estudio = soma(receita_jogo de cada jogo do estúdio)

comissao_loja = receita_estudio * (comissao_percentual / 100)

receita_total = soma(receita_estudio de todos os estúdios)

comissao_total = soma(comissao_loja de todos os estúdios)
```

**Exemplo:**

- Jogo vendido a `19,99 €` com `1000` cópias: receita `19 990,00 €`.
- Estúdio com comissão de `30%`: comissão da loja `5 997,00 €`.

Recomenda-se utilizar `Decimal` na lógica financeira para controlar o arredondamento em euros.

### 9.2. Relatório mínimo

```text
Nome             %      Jogos   Cópias    Receita (€)    Comissão (€)
-----------------------------------------------------------------------
Ctrl+Z Games     30.0       2    1 500      26 240.00         7 872.00
Patch Day One    25.0       0        0           0.00             0.00
-----------------------------------------------------------------------
TOTAL                       2    1 500      26 240.00         7 872.00
```

O exemplo baseia-se nos dados ilustrativos do capítulo 6, não nos valores do enunciado.

### 9.3. Ordenação

- Nome: alfabética.
- Receita: do maior para o menor (ou ordem escolhida pelo utilizador).
- Comissão: do maior para o menor (ou ordem escolhida pelo utilizador).
- Opcional: número de jogos e cópias vendidas.

---

## 10. Segurança

**Ações protegidas obrigatórias:**

1. Consultar a percentagem da comissão dos estúdios.
2. Abrir os relatórios financeiros que apresentam valores de comissão.

**Proposta de implementação:**

- Solicitar a palavra-passe quando o utilizador entra numa funcionalidade protegida.
- Devolver apenas sucesso/insucesso da autenticação.
- Não guardar uma palavra-passe real em texto simples no código nem no repositório público.
- Se for implementado armazenamento de credenciais, utilizar um hash com sal em vez de texto simples.
- Decidir e documentar se a autenticação vale apenas para a operação atual ou para uma sessão.

> Para este trabalho, a segurança exigida pelo enunciado é o **controlo de acesso por palavra-passe**. A implementação deverá ser adequada ao âmbito escolar e explicável ao professor.

---

## 11. Plano de desenvolvimento por fases

### Fase 1 — Esqueleto e persistência

- [x] Criar pasta e repositório do projeto.
- [x] Criar `main.py` e um menu simples.
- [ ] Criar `data/dados.json` e `data/historico.json`.
- [ ] Implementar carregamento e gravação de JSON.
- [ ] Testar alterações que sobrevivam ao reinício.

**Concluída quando:** a aplicação inicia, lê dados e consegue alterar e guardar o JSON.

### Fase 2 — Gestão de estúdios

- [ ] Listar estúdios e respetivas informações.
- [ ] Adicionar estúdios.
- [ ] Editar estúdios.
- [ ] Remover estúdios com confirmação.
- [ ] Validar campos e IDs.

**Concluída quando:** o CRUD de estúdios funciona e fica guardado.

### Fase 3 — Gestão de jogos e DLC

- [ ] Listar jogos por estúdio.
- [ ] Adicionar, editar e remover jogos.
- [ ] Listar e gerir DLC.
- [ ] Assegurar a eliminação em cascata ao remover um estúdio.

**Concluída quando:** as relações estúdio → jogo → DLC se mantêm corretas.

### Fase 4 — Pesquisa e controlo de acesso

- [ ] Pesquisa por estúdios, jogos e DLC.
- [ ] Mostrar as relações de cada DLC encontrado.
- [ ] Implementar palavra-passe e permissões.
- [ ] Ocultar comissões a utilizadores não autorizados.

**Concluída quando:** a pesquisa está correta e as informações sensíveis estão protegidas.

### Fase 5 — Relatórios e gráficos

- [ ] Programar funções de cálculo financeiro.
- [ ] Gerar tabelas e totais.
- [ ] Implementar ordenação.
- [ ] Restringir relatórios com autenticação.
- [ ] Gerar gráficos com Matplotlib.

**Concluída quando:** cálculos, relatórios, permissões e gráficos são verificáveis.

### Fase 6 — Histórico e Undo

- [ ] Registar o estado anterior a cada alteração.
- [ ] Guardar o histórico em JSON.
- [ ] Implementar anulação da última ação ativa.
- [ ] Verificar a restauração de estúdios com jogos e DLC.
- [ ] Testar histórico e Undo após reiniciar.

**Concluída quando:** as operações podem ser anuladas sem perda de dados.

### Fase 7 — Revisão e qualidade

- [ ] Testar entradas inválidas.
- [ ] Tratar ficheiros em falta e erros de escrita.
- [ ] Rever permissões e cálculos.
- [ ] Eliminar código duplicado e mensagens confusas.
- [ ] Fazer uma execução completa de demonstração.

### Fase 8 — Documentação em Typst

- [ ] Criar manual do utilizador com imagens reais da aplicação.
- [ ] Criar documentação técnica para o professor, com explicações do código.
- [ ] Gerar os dois PDFs a partir dos ficheiros `.typ`.
- [ ] Rever imagens, títulos, paginação e legibilidade.
- [ ] Confirmar que os documentos correspondem à versão final do programa.

### Fase 9 — Preparação para apresentação

- [ ] Definir uma demonstração curta e ordenada.
- [ ] Preparar dados de exemplo para a demonstração.
- [ ] Testar a aplicação no computador de apresentação.
- [ ] Ensaiar a explicação de funções, JSON, cálculos, autenticação e Undo.

**Prazo:** apresentação no dia do exame da época normal. O enunciado fornecido não especifica a data exata.

---

## 12. Plano de documentação — Typst

**Decisão do projeto:** a documentação final não será escrita em Markdown nem em Word. Serão entregues **dois documentos separados, escritos em Typst e exportados para PDF**.

### Documento A — Manual do Utilizador (`docs/manual_utilizador.typ`)

**Público-alvo:** utilizadores e administração da loja, sem necessidade de conhecimentos de programação.

**Objetivo:** ensinar a utilizar a aplicação, através de instruções simples e capturas de ecrã.

**Estrutura proposta:**

1. Capa: Insert Coin, equipa, disciplina, ano letivo.
2. Índice.
3. Introdução e objetivo da aplicação.
4. Requisitos e como iniciar o programa.
5. Apresentação do menu principal, com imagem.
6. Como consultar estúdios, jogos e DLC, com imagens.
7. Como adicionar um estúdio, um jogo e um DLC, passo a passo.
8. Como editar informação, com capturas antes/depois.
9. Como remover dados e confirmar a operação.
10. Como pesquisar estúdios, jogos e DLC.
11. Como aceder às funcionalidades protegidas por palavra-passe.
12. Como consultar e ordenar relatórios.
13. Como gerar e interpretar gráficos.
14. Como consultar o histórico e anular alterações.
15. Problemas frequentes e soluções.
16. Conclusão / informações finais.

**Regras de escrita:**

- Linguagem acessível, sem detalhes internos desnecessários.
- Imagens **reais** do terminal, obtidas depois de cada funcionalidade estar pronta.
- Cada imagem deve ter legenda e ser referida no texto.
- Preferir exemplos curtos e reproduzíveis.
- Explicar o resultado esperado de cada ação.
- Não incluir código fonte longo neste documento.

**Capturas de ecrã planeadas:**

```text
docs/imagens/
├── 01_menu_principal.png
├── 02_listar_estudios.png
├── 03_listar_jogos.png
├── 04_adicionar_estudio.png
├── 05_editar_jogo.png
├── 06_confirmar_remocao.png
├── 07_pesquisar_dlc.png
├── 08_pedir_palavra_passe.png
├── 09_relatorio_financeiro.png
├── 10_grafico_copias.png
├── 11_historico.png
└── 12_anular_acao.png
```

> Os nomes são sugestões. As imagens serão tiradas à aplicação terminada, nunca inventadas para parecer que uma funcionalidade já está implementada.

### Documento B — Documentação Técnica (`docs/documentacao_tecnica.typ`)

**Público-alvo:** professor / avaliador de Algoritmos e Programação.

**Objetivo:** explicar a arquitetura, o código e as decisões técnicas, permitindo avaliar a compreensão do projeto.

**Estrutura proposta:**

1. Capa, identificação da equipa, disciplina e ano letivo.
2. Índice.
3. Contexto e requisitos do enunciado.
4. Tecnologias utilizadas e justificação da escolha de JSON.
5. Arquitetura e organização das pastas.
6. Estrutura do catálogo e exemplos do formato JSON.
7. Fluxo de carregamento e gravação dos ficheiros.
8. Funcionamento do menu principal e dos submenus.
9. Explicação das funções de gestão de estúdios.
10. Explicação das funções de gestão de jogos e DLC.
11. Explicação das funções de pesquisa.
12. Explicação da autenticação e das restrições de acesso.
13. Fórmulas e implementação de relatórios.
14. Implementação dos gráficos com Matplotlib.
15. Implementação do histórico e do Undo, com exemplos de antes/depois.
16. Validação de entradas e tratamento de erros.
17. Testes efetuados, resultados e limitações.
18. Conclusão e possíveis melhorias.
19. Anexo com o código fonte completo, organizado por ficheiro, **se for adequado ao formato de entrega**.

**Como explicar código:**

- Identificar o ficheiro e a função.
- Indicar o propósito.
- Explicar parâmetros, valores devolvidos e dados modificados.
- Apresentar um excerto de código relevante.
- Explicar a lógica ou o algoritmo por etapas.
- Mostrar um exemplo de entrada e saída quando fizer sentido.
- Justificar decisões técnicas importantes.

**Importante:** incluir **excertos explicados no corpo do relatório** e, se necessário, **o código completo num anexo**. Evita-se transformar a documentação num monte de código sem contexto.

### Compilar os documentos

Quando os ficheiros `.typ` existirem, poderão ser compilados assim (com Typst instalado):

```bash
typst compile docs/manual_utilizador.typ docs/export/manual_utilizador.pdf
typst compile docs/documentacao_tecnica.typ docs/export/documentacao_tecnica.pdf
```

Criar a pasta `docs/export/` antes de compilar, caso ainda não exista.

### Identidade visual sugerida

- Estilo moderno e limpo, inspirado numa plataforma de videojogos.
- Cor principal: roxo, com amarelo para destaques pontuais.
- Mesma tipografia, cabeçalhos, rodapés e estilo de legendas nos dois documentos.
- **Manual:** mais visual, com imagens e tutoriais.
- **Documento técnico:** mais estruturado, com blocos de código, tabelas e esquemas.

---

## 13. Plano de testes

| ID | Teste | Resultado esperado |
|---|---|---|
| T01 | Abrir a aplicação sem ficheiro de dados | Criar dados iniciais ou informar sobre inicialização, sem falhar. |
| T02 | Inserir um estúdio e reiniciar | Estúdio continua presente. |
| T03 | Inserir um jogo e DLC | Surgem dentro do estúdio/jogo correto. |
| T04 | Editar preço e cópias e reiniciar | Novos valores permanecem guardados. |
| T05 | Introduzir preço negativo ou texto onde se espera um número | Operação rejeitada com mensagem clara. |
| T06 | Remover um estúdio com vários jogos e DLC | Estúdio e todos os elementos associados desaparecem. |
| T07 | Anular a remoção do estúdio | Estúdio, jogos e DLC regressam integralmente. |
| T08 | Reiniciar e voltar a anular uma ação pendente | Anulação funciona com histórico persistido. |
| T09 | Pesquisar um DLC por parte do nome | Exibe DLC, jogo e estúdio correspondentes. |
| T10 | Consultar comissões sem palavra-passe | Informação protegida não é mostrada. |
| T11 | Introduzir palavra-passe incorreta | Acesso negado. |
| T12 | Introduzir palavra-passe correta | Acesso permitido à funcionalidade protegida. |
| T13 | Calcular relatório com valores conhecidos | Receita, comissão e totais coincidem com contas manuais. |
| T14 | Ordenar por nome, receita ou comissão | Linhas são apresentadas na ordem escolhida. |
| T15 | Gerar gráfico sem jogos | Mensagem adequada, sem erro inesperado. |
| T16 | Gerar gráfico com dados válidos | Gráfico correspondente aos dados apresentados. |
| T17 | Tentar anular sem histórico | Informação clara, sem modificar os ficheiros. |
| T18 | Abrir JSON malformado | Erro informado; dados antigos não são apagados silenciosamente. |
| T19 | Criar vários registos com o mesmo nome | IDs continuam distintos e operações escolhem o registo correto. |
| T20 | Executar duas alterações e duas anulações | Estado original é recuperado na ordem inversa. |

### Registo de testes

Para cada teste, preencher na fase de validação:

- **Estado:** por testar / aprovado / falhou.
- **Data:** data da execução.
- **Resultado observado:** descrição breve.
- **Correção:** caso exista um erro.

---

## 14. Demonstração sugerida para o exame

1. Iniciar a aplicação e mostrar o menu.
2. Listar os estúdios e os jogos registados.
3. Adicionar um estúdio, um jogo e um DLC.
4. Editar o preço e as cópias vendidas de um jogo.
5. Reiniciar a aplicação para comprovar a persistência.
6. Pesquisar um DLC e identificar o jogo e o estúdio.
7. Mostrar que comissões e relatórios estão protegidos por palavra-passe.
8. Entrar com a palavra-passe e gerar/ordenar o relatório.
9. Gerar um gráfico.
10. Eliminar um estúdio e demonstrar a remoção em cascata.
11. Consultar o histórico e anular essa eliminação.
12. Confirmar que o estúdio, os jogos e os DLC foram restaurados.

> A duração da apresentação não foi indicada no enunciado. Ajustar o guião ao tempo definido pelo professor.

---

## 15. Prioridades, riscos e decisões

### Prioridades

1. **Essencial:** persistência, menus e CRUD de estúdios/jogos/DLC.
2. **Essencial:** pesquisa, controlo de acesso e relatórios financeiros.
3. **Essencial:** histórico, Undo e pelo menos os gráficos exigidos.
4. **Essencial:** documentação em dois documentos Typst e testes.
5. **Opcional:** gráficos extra, filtros avançados, interface colorida e funcionalidades não exigidas.

### Riscos a evitar

- Escrever tudo num único ficheiro gigante sem funções reutilizáveis.
- Guardar apenas em memória e perder dados ao sair.
- Duplicar IDs ou confundir registos com o mesmo nome.
- Mostrar comissões inadvertidamente ao listar estúdios.
- Apagar um estúdio sem guardar o estado necessário para Undo.
- Arredondar valores monetários de forma incoerente.
- Gastar demasiado tempo em aspetos visuais antes de cumprir os requisitos.
- Deixar as capturas de ecrã e a documentação técnica para depois da apresentação.

### Decisões já tomadas

- **Python** como linguagem.
- **Terminal** como interface.
- **JSON** para dados persistentes, conforme autorização verbal do professor informada pelo aluno.
- **Matplotlib** para gráficos.
- **Typst** para a documentação, em **dois documentos separados**:
  - manual do utilizador com capturas de ecrã;
  - documentação técnica para o professor, explicando código e decisões.

### Decisões que podem ser afinadas durante o desenvolvimento

- Quantidade final de módulos Python.
- Formato visual dos menus e das tabelas.
- Política de sessão/autenticação.
- Estrutura interna exata do histórico e forma de recuperar de falhas de escrita.
- Quantidade e tipos de gráficos adicionais.
- Formato de apresentação do código completo no anexo técnico.

---

## 16. Checklist de entrega

- [ ] Código Python final, executável e organizado.
- [ ] JSON de exemplo funcional, sem dados secretos.
- [ ] Histórico e Undo testados.
- [ ] Dependências e instruções de instalação incluídas.
- [ ] `README.md` com instruções de execução.
- [ ] `manual_utilizador.typ` finalizado.
- [ ] `documentacao_tecnica.typ` finalizado.
- [ ] PDF do manual do utilizador exportado.
- [ ] PDF da documentação técnica exportado.
- [ ] Capturas de ecrã reais e legíveis.
- [ ] Testes principais aprovados.
- [ ] Guião de demonstração ensaiado.
- [ ] Confirmação dos ficheiros exigidos pelo professor para a entrega.

---

## 17. Primeiro passo recomendado

Começar por **Fase 1**, sem tentar implementar tudo de uma vez:

1. Criar a pasta do projeto e o `main.py`.
2. Criar o menu principal com a opção de sair.
3. Criar um `dados.json` simples com a estrutura proposta.
4. Implementar `carregar_dados()` e `guardar_dados()`.
5. Demonstrar que uma mudança guardada continua presente depois de fechar e voltar a abrir.

Só depois avançar para a gestão de estúdios. Assim, a persistência fica resolvida antes de começar o restante projeto.

---

**Fonte principal:** enunciado do Trabalho Prático de Algoritmos e Programação, 2026/2027 (Insert Coin).  
**Adaptação autorizada pelo docente, segundo indicação do aluno:** CSV → JSON.  
**Decisão de documentação:** dois ficheiros Typst, exportados posteriormente para PDF.
