import MySQLdb
print('Conecting...')
conn = MySQLdb.connect(user='', passwd='', host='localhost', port=3306)


conn.commit()

criar_tabelas = '''SET NAMES latin1;
    DROP DATABASE IF EXISTS CRUD;
    CREATE DATABASE `crud` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `crud`;
    CREATE TABLE `students` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(255) NOT NULL,
      `email` varchar(255) NOT NULL,
      `phone` varchar(255) NOT NULL,
      PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO crud2.students (id, name, email, phone) VALUES (%s, %s, %s, %s)',
      [            (1, 'Tiago', 'tiago221@gmail.com', '99999999999'),            
       (2, 'Elias', 'elias221@gmail.com', '99999999999'),            
       (3, 'Bárbara', 'barbara221@gmail.com', '99999999999'),            
       (4, 'João', 'joao@gmail.com', '88888888888'),            
       (5, 'Maria', 'maria@gmail.com', '77777777777'),            
       (6, 'Pedro', 'pedro@gmail.com', '66666666666'),            
       (7, 'Lucas', 'lucas@gmail.com', '55555555555'),            
       (8, 'Ana', 'ana@gmail.com', '44444444444'),            
       (9, 'Júlia', 'julia@gmail.com', '33333333333'),            
       (10, 'Rafael', 'rafael@gmail.com', '22222222222')      ])


cursor.execute('select * from crud.students')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

conn.commit()
cursor.close()
