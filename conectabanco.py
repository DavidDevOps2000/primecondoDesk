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

############################################################################################ INSERTS ########
    def insertMorador(self, setsMorador):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertMorador = "INSERT INTO tbl_pessoa (cpf_pessoa, nome_pessoa, senha, nomeApelido, tipo_pessoa)"\
                             "VALUES("'%s'");"   %   (setsMorador)
        print(queryInsertMorador)
        cursorSql.execute(queryInsertMorador)
        self.con.commit()
        self.con.close()


    def insertMoradia(self, setsMoradia):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertMoradia = "INSERT INTO tbl_moradia (num_ap, 	bloco_ap, 	tbl_pessoa_id_pessoa1, 	num_vaga_car)"\
	                          "VALUES("'%s'");"  %  (setsMoradia)
        print(queryInsertMoradia)
        cursorSql.execute(queryInsertMoradia)
        self.con.commit()
        self.con.close()
    
    def insertVeiculo(self, setsVeiculo):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertVeiculo = "INSERT INTO  tbl_veiculo (cor_vei, marca_vei, modelo_vei, num_vaga, placa_vei, tbl_moradia_id_moradia)"\
                                "VALUES("'%s'");" %  (setsVeiculo)
        print(queryInsertVeiculo)
        cursorSql.execute(queryInsertVeiculo)
        self.con.commit()
        self.con.close()

    def insertContato(self, setsContato):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertContato = "INSERT INTO tbl_contato (tel, email)"\
                                "VALUES("'%s'");" %  (setsContato)
        print(queryInsertContato)
        cursorSql.execute(queryInsertContato)
        self.con.commit()
        self.con.close()

    def insertRfId(self, setsRfid):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertRfid = "INSERT INTO tbl_contato (tel, email)"\
                                "VALUES("'%s'");" %  (setsRfid)
        print(queryInsertRfid)
        cursorSql.execute(queryInsertRfid)
        self.con.commit()
        self.con.close()

    def insertBiometria(self, setsBiometria):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertBiometria = "INSERT INTO tbl_biometria (amz_img, dt_tp_reg, 	c_img )"\
                                        "VALUES("'%s'");" %  (setsBiometria)
        print(queryInsertBiometria)
        cursorSql.execute(queryInsertBiometria)
        self.con.commit()
        self.con.close()

    def insertPessoaBiometria(self, setsPessoaBiometria): # Tabela que depedente de inserts anteriores
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertPessoaBiometria = "INSERT INTO pessoa_biometria	(tbl_pessoa_id_pessoa,	tbl_biometria_id_bio)"\
                                        "VALUES("'%s'");" %  (setsPessoaBiometria)
        print(queryInsertPessoaBiometria)
        cursorSql.execute(queryInsertPessoaBiometria)
        self.con.commit()
        self.con.close()

    def insertContatosPessoa(self, setsContatosPessoa): # Tabela que depedente de inserts anteriores
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertContatosPessoa = "INSERT INTO tbl_contatos_pessoa (tbl_contato_id_contato, tbl_contatos_pessoa)"\
                                        "VALUES("'%s'");" %  (setsContatosPessoa)
        print(queryInsertContatosPessoa)
        cursorSql.execute(queryInsertContatosPessoa)
        self.con.commit()
        self.con.close()
############################################################################################ FIM DE INSERTS ##########








    def selectNomeLivroEmprestado(self, setNomeLivroEmprestado):
        self.conecta()
        cur = self.con.cursor()
        query = "select nome_livro from tbl_livros join Livro_Emprestimo on livro_emprestimo.fk_" \
                "livro = tbl_livros.codigo_livro where fk_emprestimo='%s';" % (setNomeLivroEmprestado)
        print(query)
        cur.execute(query)
        result = cursorSql.fetchall()
        self.con.close()
        print(result)
        return result



        return result


        
    def insertMorador(self, setsMorador):
        self.conecta()
        cursorSql = self.con.cursor()
        query = "INSERT INTO tbl_pessoa(cpf_pessoa, nome_pessoa, senha, nomeApelido, tipo_pessoa)"\
                "VALUES("'%s'")" %(setsMorador)#Todos os valores inseridos para usuarios estaos nesse Sets
        print(query)
        cursorSql.execute(query)
        self.con.commit()
        self.con.close()

