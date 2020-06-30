import MySQLdb

class FuncoesMorador:
#######################################################################################################################################
    def __init__(self):
        self.con = ""

    def conecta(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.db = "bd_cond"
        self.port = 3306
        self.con = MySQLdb.connect(self.host, self.user, self.password, self.db, self.port)

##################################################################################################################### INSERTS ############
    def insertMorador(self, setsMorador):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertMorador = "INSERT INTO tbl_pessoa (cpf_pessoa, nome_pessoa, senha, nomeApelido, tipo_pessoa, data_nascimento)"\
                             " VALUES("'%s'");"   %   (setsMorador)
        print(queryInsertMorador)
        cursorSql.execute(queryInsertMorador)
        self.con.commit()
        self.con.close()

    def insertMoradia(self,setsMoradia):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertMoradia = "INSERT INTO tbl_moradia (num_ap, 	bloco_ap, 	tbl_pessoa_id_pessoa1, 	num_vaga_vei)"\
	                          " VALUES("'%s'");"  %  (setsMoradia)
        print(queryInsertMoradia)
        cursorSql.execute(queryInsertMoradia)
        self.con.commit()
        self.con.close()
    
    def insertVeiculo(self, setsVeiculo):# sempte use a forma de sets para fazer as funções ao inves de varios campo
        self.conecta()                  # Pois é a maneira que melhor funciona
        cursorSql = self.con.cursor()
        queryInsertVeiculo = "INSERT INTO tbl_veiculo (cor_vei, tipo_vei, modelo_vei, placa_vei, tbl_moradia_id_moradia)"\
                                " VALUES("'%s'");" %  (setsVeiculo)
        print(queryInsertVeiculo)
        cursorSql.execute(queryInsertVeiculo)
        self.con.commit()
        self.con.close()

    def insertContato(self, setsContatos):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertContato = "INSERT INTO tbl_contato (tel, email)"\
                                " VALUES("'%s'");" %  (setsContatos)
        print(queryInsertContato)
        cursorSql.execute(queryInsertContato)
        self.con.commit()
        self.con.close()

    def insertContatosPessoa(self, setsContatosPessoa): # Tabela que depedente de inserts anteriores
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertContatosPessoa = "INSERT INTO contatos_pessoa (tbl_contato_id_contato, tbl_pessoa_id_pessoa )"\
                                        " VALUES("'%s'");" %  (setsContatosPessoa)
        print(queryInsertContatosPessoa)
        cursorSql.execute(queryInsertContatosPessoa)
        self.con.commit()
        self.con.close()
   
##########################################################################################################################################

    def insertRfId(self, setsRfid):
        self.conecta()
        cursorSql = self.con.cursor()
        queryInsertRfid = "INSERT INTO tbl_rfid (reg_tag)"\
                                "VALUES("'%s'");" %  (setsRfid)# Aqui, nesse momento, só irei colocar o cod do tag
        print(queryInsertRfid)
        cursorSql.execute(queryInsertRfid)
        self.con.commit()
        self.con.close()

######################################################################### BUSCAR IDS ##########################################################
    def buscarIdMorador(self, vlrNome, vlrCpf):
        self.conecta()
        cursorSql = self.con.cursor()
        querySelectId = "SELECT id_pessoa FROM tbl_pessoa WHERE nome_pessoa='%s' AND cpf_pessoa='%s';" % (vlrNome, vlrCpf)
        cursorSql.execute(querySelectId)
        print(querySelectId)
        result = cursorSql.fetchall()
        self.con.close()
        return result

    def buscarIdMoradia(self, vlrIdMorador, vlrNumApt):
        self.conecta()
        cursorSql = self.con.cursor()
        querySelectId = "SELECT id_moradia FROM tbl_moradia JOIN tbl_pessoa ON "\
                        "tbl_moradia.tbl_pessoa_id_pessoa1 = tbl_pessoa.id_pessoa WHERE id_pessoa = %s AND bloco_ap = '%s' " % (vlrIdMorador, vlrNumApt)
        cursorSql.execute(querySelectId)
        print(querySelectId)
        result = cursorSql.fetchall()
        self.con.close()
        return result

    def buscarIdContato(self, vlrTelefone, vlrEmail):
        self.conecta()
        cursorSql = self.con.cursor()
        querySelectId = "SELECT id_contato FROM tbl_contato WHERE tel = '%s' AND email = '%s' ;" % (vlrTelefone, vlrEmail)
        cursorSql.execute(querySelectId)
        print(querySelectId)
        result = cursorSql.fetchall()
        self.con.close()
        return result


#Para inserir dados na tabela  


    def atualizarMoradores(self, newDataNasc, newNumApt, newBloco, newTipoMorador, newTel, newEmail, newApelido, newSenha, newVaga, newStatus, newTipoVei, newModelo, newCorVei, newPlaca, cpfMorador):
        self.conecta()
        cursorSql = self.con.cursor()
        queryAtualizacao = "UPDATE tbl_pessoa JOIN tbl_moradia ON tbl_pessoa.id_pessoa = tbl_moradia.tbl_pessoa_id_pessoa1 JOIN tbl_veiculo ON tbl_moradia.id_moradia = tbl_veiculo.tbl_moradia_id_moradia "\
		                    "JOIN contatos_pessoa ON tbl_pessoa.id_pessoa = contatos_pessoa.tbl_pessoa_id_pessoa JOIN tbl_contato ON contatos_pessoa.tbl_contato_id_contato = tbl_contato.id_contato "\
		                    " SET data_nascimento ='%s', num_ap =%s, bloco_ap ='%s', tipo_pessoa ='%s', tel ='%s', email ='%s', nomeApelido ='%s', senha ='%s', num_vaga_vei= %s, status_pess = %s, tipo_vei ='%s', "\
                            "modelo_vei ='%s', cor_vei ='%s', placa_vei ='%s' WHERE cpf_pessoa='%s';" % (newDataNasc, newNumApt, newBloco, newTipoMorador, newTel, newEmail, newApelido, newSenha, newVaga, newStatus, newTipoVei, newModelo, newCorVei, newPlaca, cpfMorador)
        
        print(queryAtualizacao)
        cursorSql.execute(queryAtualizacao)
        self.con.commit()
        self.con.close()
