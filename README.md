# SpecialisterneUge4
Put dine MySQL oplysninger i config.txt og kør database_init.py. ADVARSEL: database_init.py sletter databaserne med navnene i config.txt hvis de eksisterer.
Derefter kan du køre crud_tests.py eller skrive dine egne queries ved at give en instance af CRUD fra crud_opreations.py en MySQLConnection fra mysql_connection.py med navnet på den database du vil lave operationer på.