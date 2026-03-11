
class LimiteEmprestimosExcedido(Exception):
    pass

class LivroIndisponivel(Exception):
    pass

class Livro:
    def __init__(self, isbn, titulo, autor, disponivel=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

class Usuario:
    def __init__(self, matricula, nome, limite):
        self.matricula = matricula
        self.nome = nome
        self.livros_emprestados = []
        self.limite = limite

    def pegar_emprestado(self, livro):
        if len(self.livros_emprestados) >= self.limite:
            raise LimiteEmprestimosExcedido("Limite de empréstimos atingido")

        if not livro.disponivel:
            raise LivroIndisponivel("Livro não está disponível")

        livro.emprestar()
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)

class Aluno(Usuario):
    def __init__(self, matricula, nome):
        super().__init__(matricula, nome, 3)

class Professor(Usuario):
    def __init__(self, matricula, nome):
        super().__init__(matricula, nome, 5)

class Biblioteca:
    def __init__(self):
        self.acervo = []
        self.usuarios_cadastrados = []

    def cadastrar_usuario(self, usuario):
        self.usuarios_cadastrados.append(usuario)

    def registrar_emprestimo(self, matricula, isbn):
        usuario = None
        livro = None

        for u in self.usuarios_cadastrados:
            if u.matricula == matricula:
                usuario = u

        for l in self.acervo:
            if l.isbn == isbn:
                livro = l

        if usuario and livro:
            usuario.pegar_emprestado(livro)

    def consultar_livros_emprestados(self):
        for usuario in self.usuarios_cadastrados:
            print(f"\nUsuário: {usuario.nome}")
            for livro in usuario.livros_emprestados:
                print(f"- {livro.titulo}")

biblioteca = Biblioteca()

biblioteca.acervo.append(Livro("LIV001", "Titulo 1", "Autor 1"))
biblioteca.acervo.append(Livro("LIV002", "Titulo 2", "Autor 2"))
biblioteca.acervo.append(Livro("LIV003", "Titulo 3", "Autor 3"))
biblioteca.acervo.append(Livro("LIV004", "Titulo 4", "Autor 4"))
biblioteca.acervo.append(Livro("LIV005", "Titulo 5", "Autor 5"))

aluno1 = Aluno("ALUNOXX1", "Nome 1")
aluno2 = Aluno("ALUNOXX2", "Nome 2")
professor1 = Professor("PROFXX1", "Professor")

biblioteca.cadastrar_usuario(aluno1)
biblioteca.cadastrar_usuario(aluno2)
biblioteca.cadastrar_usuario(professor1)

try:
    biblioteca.registrar_emprestimo("ALUNOXX1", "LIV001")
    biblioteca.registrar_emprestimo("ALUNOXX1", "LIV002")
    biblioteca.registrar_emprestimo("PROFXX1", "LIV003")

except Exception as erro:
    print(erro)

try:
    biblioteca.registrar_emprestimo("ALUNOXX2", "LIV001")
except Exception as erro:
    print("Erro", erro)
biblioteca.consultar_livros_emprestados()