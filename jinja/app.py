from flask import Flask, render_template

app = Flask(__name__)
cidade = "Brasília"
nome = "Sandro e Sinthia"
hoje = 2023
ano = 2006
autor = "Jorge Dias"


@app.route("/")
def hello():
    return """
    <h1>Welcome to Flask.</h1>
    <hr>
    <p> Veja uma lista de usuários <a href='users'>aqui</a> </p>
    <p> Veja o resultado do uso de expressões <a href='expressions'>aqui</a></p> 
    <p> Veja operadores condicionais:
        <ul>
            <li> <a href='conditionals/Apple'>Produtos da Apple</a></li>
            <li> <a href='conditionals/Microsoft'>Produtos da Microsoft</a></li>
        </ul> 
    """


@app.route("/users/")
def users():
    return render_template("users.html", name="Jorge")


dados = {
    "cidade": cidade,
    "nome": nome,
    "hoje": hoje,
    "ano": ano,
    "autor": autor,
}


@app.route("/expressions/")
def expressions():
    return render_template(
        "expressions.html",
        **dados,
    )


produtos = {
    "iPhone": "Apple",
    "iMac": "Apple",
    "iTunes": "Apple",
    "iPad": "Apple",
    "Azure": "Microsoft",
    "Office 365": "Microsoft",
    "Windows": "Microsoft",
    "Surface": "Microsoft",
}

todos_list = [("Lavar roupa.", True), ("Comprar remédio", False), ("Jogar bola", True)]


@app.route("/conditionals/<company>/")
def conditionals(company="Apple"):
    return render_template("conditionals.html", company=company)


@app.route("/loops/<company>/")
def loops(company="Apple"):
    return render_template("loops.html", company=company, produtos=produtos)


@app.route("/jinja/")
def todos():
    return render_template("jinja.html", tarefas=todos)


@app.route("/<string:todo>")
def todo_item(todo):
    for text, completed in todos_list:
        if text == todo:
            completed_text = "[x]" if completed else "[ ]"
            title = f"{completed_text} - {text}"
            return render_template(
                "inheritance.html", text=text, completed=completed_text, title=title
            )
    else:
        return render_template("not-found.html", text=todo, title="Not found")


if __name__ == "__main__":
    app.run(debug=True)
