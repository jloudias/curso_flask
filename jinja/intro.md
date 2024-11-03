# Introdução ao Flask
### Primeiros passos.

- instalação é simples 
  - `from flask import Flask`
  - `app=Flask(__name__)`
- execução
  - designa o arquivo inicial
    ```
    set FLASK_APP=app.py 
    set FLASK_DEBUG=1
    flask run
    ```
  - falsa main() no arquivo inicial
    ```
    if __name__ == "__main__":
        app.run(debug=True)
    ```
### Templates

- criar pasta 'templates'
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x) é a linguagem de template
- importar biblioteca 'render_template'
- criar .html na pasta templates
- chamar com render_template, passando nome e variáveis
- recomenda-se passar dicionários (usar **)
- variavéis são assinaladas por {{ nome }}