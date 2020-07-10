import MySQLdb

class FuncoesVisitante:
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

##################################################################################################################### SELECTs ############

    def consulMoradorToVisi(self, nomeMorador, cpfMorador):
        self.conecta()
        self.cursorSql = self.con.cursor()
        queryConsulMorToVisi="SELECT num_ap, bloco_ap, CASE status_pess WHEN TRUE THEN 'ATIVO' ELSE 'DESATIVADO' END status_pess, nome_pessoa, num_vaga_vei "\
                            "FROM tbl_pessoa p LEFT JOIN tbl_moradia m ON p.id_pessoa = m.tbl_pessoa_id_pessoa1 "\
                            "LEFT JOIN contatos_pessoa cp ON p.id_pessoa = cp.tbl_pessoa_id_pessoa "\
                            "LEFT JOIN tbl_contato c ON cp.tbl_contato_id_contato = c.id_contato "\
                            "WHERE nome_pessoa ='%s' OR cpf_pessoa='%s';" % (nomeMorador, cpfMorador)
        self.cursorSql.execute(queryConsulMorToVisi)
        print(queryConsulMorToVisi)
        result = self.cursorSql.fetchall()
        self.con.close()
        return result


##################################################################################################################### INSERTS ############
    def buscarIdMoradorToVisi(self, seuCpf):
        self.conecta()
        self.cursorSql = self.con.cursor()
        queryIdMorador ="SELECT id_pessoa FROM tbl_pessoa WHERE cpf_pessoa='%s';" % (seuCpf)
        self.cursorSql.execute(queryIdMorador)
        print(queryIdMorador)
        result = self.cursorSql.fetchall()
        self.con.close()
        return result

    def verificarVisiExiste(self, nomeVisi, idMorador):
        self.conecta()
        self.cursorSql = self.con.cursor()
        query ="SELECT * FROM tbl_pessoa JOIN agen_visi ON tbl_pessoa.id_pessoa = agen_visi.tbl_pessoa_id_pessoa JOIN "\
                        "visi_apt ON agen_visi.visi_apt_id_visi = visi_apt.id_visi WHERE "\
                        "id_pessoa='%s' and nome_visi='%s' " % (nomeVisi, idMorador)
        self.cursorSql.execute(query)
        print(query)
        result = self.cursorSql.fetchall()
        self.con.close()
        return result


    def insertVisi1(self, nomeVisi, rgVisi):
        self.conecta()
        cursorSql = self.con.cursor()
        query = "INSERT INTO visi_apt(nome_visi, rg_visi, dt_registro_visi) "\
                                    "VALUES('%s', '%s', NOW())" %  (nomeVisi, rgVisi)
        print(query)
        cursorSql.execute(query)
        self.con.commit()
        self.con.close()


    def idVisi(self, nomeVisi, rgVisi):
        self.conecta()
        self.cursorSql = self.con.cursor()
        query = "SELECT id_visi FROM visi_apt "\
                "WHERE nome_visi='%s' AND rg_visi='%s' " % (nomeVisi, rgVisi)
        self.cursorSql.execute(query)
        print(query)
        result = self.cursorSql.fetchall()
        self.con.close()
        return result

    def insertVisi2(self, idMorador, idVisi): # Esse insert é para caso não haja dias definidos
        self.conecta()
        cursorSql = self.con.cursor()
        query = "INSERT INTO agen_visi(tbl_pessoa_id_pessoa, visi_apt_id_visi)"\
                " VALUES(%s, %s);" %  (idMorador, idVisi)
        print(query)
        cursorSql.execute(query)
        self.con.commit()
        self.con.close()

    def insertVisi3(self, idMorador, idVisi, numDia): # Esse insert é para caso não haja dias definidos
        self.conecta()
        cursorSql = self.con.cursor()
        query = "INSERT INTO agen_visi(tbl_pessoa_id_pessoa, visi_apt_id_visi, data_visi, data_fim_visi) "\
                "VALUES(%s, %s, now(), now() + interval %s day)" %  (idMorador, idVisi, numDia)
        print(query)
        cursorSql.execute(query)
        self.con.commit()
        self.con.close()

