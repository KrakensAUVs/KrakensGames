from classes import Consumers, Products, Orders      

cons_gen = Consumers()
prod_gen = Products()
orders_gen =  Orders()

cons_gen.populate()
cons_ids = cons_gen.id_list

prod_gen.populate()
prod_ids = prod_gen.id_list

orders_gen.populate(cons_ids, prod_ids)