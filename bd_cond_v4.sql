DROP DATABASE bd_cond;
CREATE database bd_cond;
USE bd_cond;

-- -----------------------------------------------------
-- Table bd_cond.tbl_pessoa
-- -----------------------------------------------------
CREATE TABLE tbl_pessoa (      #desktop
  id_pessoa INT(11) NOT NULL AUTO_INCREMENT,
  cpf_pessoa VARCHAR(14) UNIQUE NOT NULL, #cpf  Todas as idades, a parti de zeroa anos, são obrigatorios por causa de uma lei de 2019
  nome_pessoa VARCHAR(89) NOT NULL,
  senha VARCHAR(20),# Para uso do Login
  nomeApelido VARCHAR(20) UNIQUE /*NOT NULL*/, # Para uso do Login SOMENTE MAIORES DE 18 ANOS PODEM fazer o login, tirar essa opção de não moradores e proprietários
  dt_reg DATETIME DEFAULT NOW() NOT NULL, # Dia que a pessoa foi registrada
  status_pess BOOLEAN DEFAULT TRUE NOT NULL,
  data_nascimento VARCHAR (10),#Aqui teria a data de nascimento 99/99/9999
  tipo_pessoa ENUM('Proprietário', 'Morador', 'Dependente') DEFAULT 'Proprietário' NOT NULL, #TIPOS DE 'MORADORES' se for proprietário ele pode entrar assim como o morador
  PRIMARY KEY (id_pessoa));
  ALTER TABLE tbl_pessoa ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table bd_cond.tbl_contato
-- -----------------------------------------------------
CREATE TABLE tbl_contato (				#DESKTOP
  id_contato INT(11) NOT NULL AUTO_INCREMENT,
  tel VARCHAR(22) NOT NULL,
  email VARCHAR(46), 
  PRIMARY KEY (id_contato));
  ALTER TABLE tbl_contato ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table bd_cond.tbl_moradia
-- -----------------------------------------------------
CREATE TABLE tbl_moradia ( # Tabela moradia tem que ter dados inseridos APÓS da tbl_Pessoa para fazer ligação     #DESKTOP
  id_moradia INT(11) NOT NULL AUTO_INCREMENT,
  num_ap INT(11) NOT NULL, # Numero apartamento 
  bloco_ap ENUM('A', 'B', 'C', 'D') NOT NULL, # Numero do Bloco, Mas nesse caso não nomeamos com o numero E LETRA, pois isso vai de cliente a cliente
  tbl_pessoa_id_pessoa1 INT(11) NOT NULL UNIQUE, #Como não pode existir id duplicada de morador, muito menos duplicada, coloquei unique pra evitar isso 
  num_vaga_vei INT(11) NOT NULL, #Numero da vaga do Carro, tem que ser o mesmo numero do apt, mas somente para apresentar no tcc
  PRIMARY KEY (id_moradia),
  INDEX fk_tbl_moradia_tbl_pessoa1_idx (tbl_pessoa_id_pessoa1 ASC));
  ALTER TABLE tbl_moradia ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table bd_cond.tbl_veiculo
-- -----------------------------------------------------
CREATE TABLE tbl_veiculo (
  id_veiculo INT(11) NOT NULL AUTO_INCREMENT,
  placa_vei VARCHAR(7) NOT NULL UNIQUE,
  tipo_vei ENUM('Carro', 'Moto', 'Outros'),
  modelo_vei VARCHAR(15) NOT NULL,
  cor_vei VARCHAR(20) NOT NULL,
  tbl_moradia_id_moradia INT(11) NOT NULL ,
  PRIMARY KEY (id_veiculo),
  INDEX fk_tbl_veiculo_tbl_moradia1_idx (tbl_moradia_id_moradia ASC));
  ALTER TABLE tbl_veiculo ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table bd_cond.visi_apt
-- -----------------------------------------------------
CREATE TABLE visi_apt (							#WEB / DESKTOP 
  id_visi INT(11) NOT NULL AUTO_INCREMENT,
  nome_visi VARCHAR(90) NOT NULL,
  dt_registro_visi DATETIME NOT NULL,
  rg_visi VARCHAR(12),# Esse campo só pode ser preenchido opcionalmente pelo Desktop ou WEB
  PRIMARY KEY (id_visi),
  INDEX rg_visiUNIQUE (rg_visi ASC));
  ALTER TABLE visi_apt ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table bd_cond.contatos_pessoa
-- -----------------------------------------------------
CREATE TABLE contatos_pessoa (# Isso é para que uma pessoa tenha varios numeros e um numero dependendo da situação tenha varias pessoas #DESKTOP
  tbl_contato_id_contato INT(11) NOT NULL,
  tbl_pessoa_id_pessoa INT(11) NOT NULL,
  PRIMARY KEY (tbl_contato_id_contato, tbl_pessoa_id_pessoa),#Nao implementar esse banco sem que tenhamos colocado essas ligações em uma constraint
  INDEX fk_tbl_contato_has_tbl_pessoa_tbl_pessoa1_idx (tbl_pessoa_id_pessoa ASC),
  INDEX fk_tbl_contato_has_tbl_pessoa_tbl_contato_idx (tbl_contato_id_contato ASC));
  ALTER TABLE contatos_pessoa ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table bd_cond.agendamento_visitas
-- -----------------------------------------------------
CREATE TABLE agen_visi (#WEB / DESKTOP
  tbl_pessoa_id_pessoa INT(11) NOT NULL,
  visi_apt_id_visi INT(11) NOT NULL,
  data_visi date,
  data_fim_visi date,
  autorizado BOOLEAN DEFAULT TRUE,
  PRIMARY KEY (tbl_pessoa_id_pessoa, visi_apt_id_visi),#Nao implementar esse banco sem que tenhamos colocado essas ligações em uma constraint
  INDEX fk_tbl_pessoa_has_visi_apt_visi_apt1_idx (visi_apt_id_visi ASC),
  INDEX fk_tbl_pessoa_has_visi_apt_tbl_pessoa1_idx (tbl_pessoa_id_pessoa ASC));
  ALTER TABLE agen_visi ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table bd_cond.tbl_biometria
-- -----------------------------------------------------
CREATE TABLE tbl_biometria (
  id_bio INT(11) NOT NULL AUTO_INCREMENT,
  amz_img BLOB NOT NULL,
  dt_tp_reg TIMESTAMP NOT NULL,
  c_img VARCHAR(45) NOT NULL,
  PRIMARY KEY (id_bio));
  ALTER TABLE tbl_biometria ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table bd_cond.pessoa_biometria
-- -----------------------------------------------------
  -- -----------------------------------------------------
CREATE TABLE pessoa_biometria ( #DESKTOP
  tbl_pessoa_id_pessoa INT(11) NOT NULL,
  tbl_biometria_id_bio INT(11) NOT NULL,
  PRIMARY KEY (tbl_pessoa_id_pessoa, tbl_biometria_id_bio),#Nao implementar esse banco sem que tenhamos colocado essas ligações em uma constraint
  INDEX fk_tbl_pessoa_has_tbl_biometria_tbl_biometria1_idx (tbl_biometria_id_bio ASC) ,
  INDEX fk_tbl_pessoa_has_tbl_biometria_tbl_pessoa1_idx (tbl_pessoa_id_pessoa ASC));
  ALTER TABLE pessoa_biometria ENGINE = InnoDB;
  
-- -----------------------------------------------------
-- Table bd_cond.tbl_rfid
-- -----------------------------------------------------
CREATE TABLE tbl_rfid ( 
  id_tag INT(11) NOT NULL AUTO_INCREMENT, #Id da mesma
  reg_tag VARCHAR(15) NOT NULL, #Registro da Tag
  data_hora_reg DATETIME NOT NULL, # Hora do registro da Entrada
  status_tag BOOLEAN DEFAULT TRUE NOT NULL, # Verifica se está ativo ou não
  PRIMARY KEY (id_tag));
  ALTER TABLE tbl_rfid ENGINE = InnoDB;