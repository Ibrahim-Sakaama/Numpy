import pymysql

# connection = pymysql.connect(user="root")
# #il faut creer un curseur. Le curseur va executer les requetes
# cur = connection.cursor()
# #creation d'une database
# cur.execute('CREATE DATABASE my_db')

#creation d'un tableau
#execute code above first then comment it

# connection = pymysql.connect(host="localhost",user="root",database="my_sql")
# cur = connection.cursor()
# cur.execute('create table etudiants(id int , prenom varchar(20) , nom varchar(20) , moyenne float , payment boolean)')

#insertion des donnes


# connection = pymysql.connect(host="localhost",user="root",database="my_db")
# cur = connection.cursor()
# cur.execute('insert into etudiants values(1 , "mohamed", "rami" , 12.33 , true)')
# cur.execute('insert into etudiants values(2 , "sami", "mahjoub" , 9.33 , true)')
# cur.execute('insert into etudiants values(3 , "nacer", "amin" , 16.45 , true)')
# cur.execute('insert into etudiants values(4 , "zeineb", "ali" , 10.02 , true)')
# cur.execute('insert into etudiants values(5 , "mahmoud", "rjab" , 6.88 , true)')
# #to commit insertions
# connection.commit()


#to update

# connection = pymysql.connect(host="localhost",user="root",database="my_db")
# cur = connection.cursor()
# cur.execute('UPDATE etudiants SET moyenne = 1.66 WHERE id = 4')
# #to commit update
# connection.commit()


# to insert data manually with input method(au clavier)


# connection = pymysql.connect(host="localhost",user="root",database="my_db")
# for i in range(4):
#     _id = input('donner if\n')
#     _prenom = input('donner prenom\n')
#     _nom = input('donner le nom\n')
#     _moy = input('donner moyenne\n')
#     _pay = input('paiement "0" ou "1"\n')

#     cur = connection.cursor()
#     querry = 'insert into etudiants (id,prenom,nom,moyenne,paiement) values (%s %s %s %s %s)'
#     cur.execute(querry,(_id,_prenom,_nom,_moy,_pay))

#     connection.commit()

    #deleting
# connection = pymysql.connect(host="localhost",user="root",database="my_db")
# _id = input('donner id à supprimer')
# cur = connection.cursor()
# querry = 'delete from etudiants where id = %s'
# cur.execute(querry,_id)
# connection.commit()

#select method

connection = pymysql.connect(host="localhost",user="root",database="my_db")
cur = connection.cursor()

cur.execute('select * from etudiants')
print("{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||".format('id','prenom','nom','moyenne','paiement'))

#fetchall() ==> to stock all data under cur.execute
for row in cur.fetchall():
    print("{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||".format(row[0],row[1],row[2],row[3],row[4]))


#Select(with condition)

cur.execute('select * from etudiants where moyenne >10')
print("{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||".format('id','prenom','nom','moyenne','paiement'))

for row in cur.fetchall():
    print("{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||".format(row[0],row[1],row[2],row[3],row[4]))

connection.close()




