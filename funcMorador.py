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


    def buscarPessoaMoradia(self, nomePessoa, cpfMorador): # Aqui 
        self.conecta()
        cursorSql = self.con.cursor()
        querySelectId = "SELECT id_pessoa, id_moradia FROM tbl_pessoa "\
                        "LEFT JOIN tbl_moradia ON tbl_pessoa.id_pessoa = tbl_moradia.tbl_pessoa_id_pessoa1 "\
                        "WHERE nome_pessoa='%s' AND cpf_pessoa='%s';" % (nomePessoa, cpfMorador)
        cursorSql.execute(querySelectId)
        print(querySelectId)
        result = cursorSql.fetchall()
        self.con.close()
        return result


################################################################################################################## UPDATES ##########################################

    def consulMoradorUpdate(self, nomeMorador, cpfMorador):
        self.conecta()
        self.cursorSql = self.con.cursor()
        consultMoradorQuery="SELECT data_nascimento, num_ap, bloco_ap, tipo_pessoa, tel, email, nomeApelido, "\
                            "senha, num_vaga_vei, status_pess, tipo_vei, modelo_vei, cor_vei, placa_vei, nome_pessoa "\
                            "FROM tbl_pessoa p LEFT JOIN tbl_moradia m ON p.id_pessoa = m.tbl_pessoa_id_pessoa1 "\
                            "LEFT JOIN tbl_veiculo v ON m.id_moradia = v.tbl_moradia_id_moradia "\
                            "LEFT JOIN contatos_pessoa cp ON p.id_pessoa = cp.tbl_pessoa_id_pessoa "\
                            "LEFT JOIN tbl_contato c ON cp.tbl_contato_id_contato = c.id_contato "\
                            "WHERE nome_pessoa ='%s' OR cpf_pessoa='%s';" % (nomeMorador, cpfMorador)

        self.cursorSql.execute(consultMoradorQuery)
       # print(consultMoradorQuery)
        result = self.cursorSql.fetchall()
        self.con.close()
        return result


#Para inserir dados na tabela  


    def atualizarMoradores(self, newDataNasc, newNumApt, newBloco, newTipoMorador, newTel, newEmail, newApelido, newSenha, newVaga, newStatus, newTipoVei, newModelo, newCorVei, newPlaca, newNomeMorador, nomeMorador, cpfMorador):
        self.conecta()
        cursorSql = self.con.cursor() #Usei LEFT JOIN, pois para atualizar campos nulos em varias tabelas, tem que usar o Left, pois ele trás e atualiza as mesmas, e evita o erro que de 'funcionar' a query sem alterar nada
        queryAtualizacao =  "UPDATE tbl_pessoa p LEFT JOIN tbl_moradia m ON p.id_pessoa = m.tbl_pessoa_id_pessoa1 "\
                            "LEFT JOIN tbl_veiculo v ON m.id_moradia = v.tbl_moradia_id_moradia "\
                            "LEFT JOIN contatos_pessoa cp ON p.id_pessoa = cp.tbl_pessoa_id_pessoa "\
                            "LEFT JOIN tbl_contato c ON cp.tbl_contato_id_contato = c.id_contato "\
                            "SET data_nascimento ='%s', num_ap =%s, bloco_ap ='%s', tipo_pessoa ='%s', tel ='%s', "\
                            "email ='%s', nomeApelido ='%s', "\
                            "senha ='%s', num_vaga_vei= %s, status_pess = %s, tipo_vei ='%s', "\
                            "modelo_vei ='%s', cor_vei ='%s', placa_vei ='%s', nome_pessoa ='%s' "\
                            "WHERE nome_pessoa ='%s' OR cpf_pessoa='%s';" % (newDataNasc, newNumApt, newBloco, newTipoMorador, newTel, newEmail, newApelido, newSenha, newVaga, newStatus, newTipoVei, newModelo, newCorVei, newPlaca, newNomeMorador, nomeMorador, cpfMorador)
        
        print(queryAtualizacao)
        cursorSql.execute(queryAtualizacao)
        self.con.commit()
        self.con.close()

    
    def temCpf(self, verificarCPF):
        self.conecta()
        cursorSql = self.con.cursor()
        querySelectCpf = "SELECT * FROM tbl_pessoa WHERE cpf_pessoa = '%s';" % (verificarCPF)
        cursorSql.execute(querySelectCpf)
        print(querySelectCpf)
        result = cursorSql.fetchall()
        self.con.close()
        return result


    def temApelido(self, verificarApelido):
        self.conecta()
        cursorSql = self.con.cursor()
        querySelectApelido = "SELECT * FROM tbl_pessoa WHERE nomeApelido = '%s';" % (verificarApelido)
        cursorSql.execute(querySelectApelido)
        print(querySelectApelido)
        result = cursorSql.fetchall()
        self.con.close()
        return result

    def temPlaca(self, verificarPlaca):
        self.conecta()
        cursorSql = self.con.cursor()
        querySelecVei = "SELECT * FROM tbl_veiculo WHERE  placa_vei = '%s';" % (verificarPlaca)
        cursorSql.execute(querySelecVei)
        print(querySelecVei)
        result = cursorSql.fetchall()
        self.con.close()
        return result

#################################################################################################################################################################
def atualizarMoradores(self, newDataNasc, newNumApt, newBloco, newTipoMorador, newTel, newEmail, newApelido, newSenha, newVaga, newStatus, newTipoVei, newModelo, newCorVei, newPlaca, newNomeMorador, nomeMorador, cpfMorador):
        self.conecta()
        cursorSql = self.con.cursor() #Usei LEFT JOIN, pois para atualizar campos nulos em varias tabelas, tem que usar o Left, pois ele trás e atualiza as mesmas, e evita o erro que de 'funcionar' a query sem alterar nada
        queryAtualizacao =  "UPDATE tbl_pessoa p LEFT JOIN tbl_moradia m ON p.id_pessoa = m.tbl_pessoa_id_pessoa1 "\
                            "LEFT JOIN tbl_veiculo v ON m.id_moradia = v.tbl_moradia_id_moradia "\
                            "LEFT JOIN contatos_pessoa cp ON p.id_pessoa = cp.tbl_pessoa_id_pessoa "\
                            "LEFT JOIN tbl_contato c ON cp.tbl_contato_id_contato = c.id_contato "\
                            "SET data_nascimento ='%s', num_ap =%s, bloco_ap ='%s', tipo_pessoa ='%s', tel ='%s', "\
                            "email ='%s', nomeApelido ='%s', "\
                            "senha ='%s', num_vaga_vei= %s, status_pess = %s, tipo_vei ='%s', "\
                            "modelo_vei ='%s', cor_vei ='%s', placa_vei ='%s', nome_pessoa ='%s' "\
                            "WHERE nome_pessoa ='%s' OR cpf_pessoa='%s';" % (newDataNasc, newNumApt, newBloco, newTipoMorador, newTel, newEmail, newApelido, newSenha, newVaga, newStatus, newTipoVei, newModelo, newCorVei, newPlaca, newNomeMorador, nomeMorador, cpfMorador)
        
        print(queryAtualizacao)
        cursorSql.execute(queryAtualizacao)
        self.con.commit()
        self.con.close()