#  Gestor de Portfólio Pessoal

**Um software de console em Python para gerenciar os projetos pessoais.**
*Projeto desenvolvido para a disciplina de Raciocínio Computacional*

---

##  STATUS DO PROJETO 
**🚧 Em Desenvolvimento 🚧**

O projeto já possui seu menu principal interativo, a estrutura de repetição e a funcionalidade básica de `ADD`, `LIST`, `UPDATE`, `DELETE`, `ABOUT` e `QUIT` implementadas, além de criação de um arquivo de banco de dados `json` ao executar o comando `QUIT` e salvamento para persistência dos dados.
> **Destaque:** O sistema conta com **persistência de dados automática** (arquivo JSON) e **rastreabilidade** (histórico de alterações com data e hora).

---

## ⚙️ Funcionalidades

### Funcionalidades Implementadas
* [X] **Menu Principal:** Exibe um menu com todas as opções disponíveis.
* [X] **Persistência de Dados:** Salva e carrega automaticamente os dados em `portfolio.json`.
* [X] **Histórico de Auditoria:** Registra automaticamente data e hora de cada alteração (mudança de nome ou status) dentro do projeto.
* [X] **Comando `ADD`:** Permite cadastrar múltiplos projetos em sequência.
* [X] **Comando `LIST`:** Lista todos os projetos exibindo status e o histórico de mudanças.
* [X] **Comando `UPDATE`:** Atualiza nome ou status (Pendente/Concluído) de um projeto.
* [X] **Comando `DELETE`:** Exclui projetos permanentemente.
* [X] **Comando `ABOUT`:** Exibe as informações do autor.
* [X] **Comando `QUIT`:** Salva os dados e encerra a aplicação com segurança.
* [X] **Tratamento de Erros:** Mensagens amigáveis para entradas inválidas ou arquivos corrompidos.

### Funcionalidades Pendentes
* [ ] **Comando `STATS`:** Relatório estatístico (Total de projetos, % concluídos).
* [ ] **Comando `SEARCH`:** Busca projetos por palavras-chave.

---

## 💻 Como Usar

1.  Certifique-se de ter o **Python 3.10** (ou superior) instalado.
2.  Clone este repositório (ou baixe os arquivos).
3.  Navegue até o diretório do projeto:
    ```bash
    cd portfolio-manager-python
    ```
4.  Execute o script principal:
    ```bash
    python src/main.py
    ```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Biblioteca `json`** (para persistência de dados estruturada)
* **Biblioteca `os`** (para manipulação de sistema e limpeza de console)
* **Biblioteca `datetime`** (para carimbo de tempo no histórico)

---

## 👨‍💻 Autor

* **Filipe Vaz**
    *(Projeto da disciplina de Raciocínio Computacional)*

---


##  Declaração de Uso de IA

> Durante a preparação deste **arquivo README.md**, o autor usou **Gemini (Google)** para **auxiliar na estruturação, formatação e revisão do texto de documentação**. Após usar essa ferramenta, o autor revisou e editou o conteúdo conforme necessário e assume total responsabilidade pelo conteúdo.

---