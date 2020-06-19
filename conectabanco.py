import MySQLdb


class ConectaBanco:
    def __init__(self):
        self.con = ""

    def conecta(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.db = "bd_cond"
        self.port = 3306
        self.con = MySQLdb.connect(self.host, self.user, self.password, self.db, self.port)


    def insertMorador(self, setsMorador):
        self.conecta()
        cursorSql = self.con.cursor()
        query = "INSERT INTO tbl_pessoa(cpf_pessoa, nome_pessoa, senha, nomeApelido, tipo_pessoa)"\
                "VALUES("'%s'")" %(setsMorador)#Todos os valores inseridos para usuarios estaos nesse Sets
        print(query)
        cursorSql.execute(query)
        self.con.commit()
        self.con.close()

    def selectMoradorToMoradia(self, setNomeMorador, setCpf):
        self.conecta()
        cursorSql = self.con.cursor()
        query = "SELECT id_pessoa FROM tbl_pessoa WHERE nome_pessoa='%s' and cpf_pessoa='%s';" %(setNomeMorador, setCpf)
        print(query)
        cursorSql.execute(query)
        result = cur.fetchall()
        self.con.close()
        print(result)
        return result

    def cadastroMorador():
        self.conecta()
        cursorSql = self.con.cursor()
        query = "BEGIN;\
                    SELECT id_pessoa FROM tbl_pessoa WHERE nome_pessoa='%s' and cpf_pessoa='%s';" %(setNomeMorador, setCpf)


    def insertMoradia(self, numAp, bloco, morador, numVaga):
        self.conecta()
        cursorSql = self.con.cursor()
        query = "INSERT INTO tbl_moradia(num_ap, 		bloco_ap, 		tbl_pessoa_id_pessoa1, 	num_vaga_car)"\
                "VALUES(%s,'%s','%s', %s)" %(numAp, bloco, morador, numVaga)#Todos os valores inseridos para usuarios estaos nesse Sets
        print(query)
        cursorSql.execute(query)
        self.con.commit()
        self.con.close()
    
    

