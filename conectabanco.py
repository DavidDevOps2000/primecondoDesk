import MySQLdb


class ConectaBanco:
    def __init__(self):
        self.con = ""

    def conecta(self):
        host = "localhost"
        user = "root"
        password = ""
        db = "bd_cond"
        port = 3306
        self.con = MySQLdb.connect(host, user, password, db, port)


    def insertMorador(self, setsMorador):
        self.conecta()
        cursorSql = self.con.cursor()
        query = "INSERT INTO tbl_pessoa(cpf_pessoa, nome_pessoa, senha, nomeApelido, tipo_pessoa)"\
                "VALUES("'%s'")" %(setsMorador)#Todos os valores inseridos para usuarios estaos nesse Sets
        print(query)
        cursorSql.execute(query)
        self.cursorSql.commit()
        self.cursorSql.close()

