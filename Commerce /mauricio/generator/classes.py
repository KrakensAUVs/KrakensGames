import random

def generate_pos(size, init = 0):
    return random.randrange(init, size)

class BaseGen:
    def __init__(self):
        self._ids = []

    def _unique_id(self) -> int:
        if not self._ids:
            id_ = generate_pos(50, 1)
        else:
            last = self._ids[-1]
            id_ = generate_pos(last+50, last)

        self._ids.append(id_)
        return id_
    
    @property
    def id_list(self):
        return self._ids

class Consumers(BaseGen):

    __first_names = ["Carlos", "Antônio", "Adriano", "Émerson", "Nicolas", "Gilmar","Fernando", "Rafael", "Valdomiro", "Kléber", "Isabela", "Janaína", "Carina", "Poliane", "Fabiana", "Taís", "Beatriz", "Heloísa", "Elaine", "Nicole"]
    __last_names = ["Velho", "Medeiros", "Paim", "Nazário", "Machado", "Leal", "Ito", "de Salles", "Farias", "Braz", "Assis", "Pedroso", "Carmo", "Quadros", "Vaz", "Paschoal", "Vargas", "Braga", "Lima", "da Cruz", "Cavalcanti", "da Silva", "Pacheco", "Correia", "Lobo", "Arruda", "Gimenes", "da Cunha", "Oliveira", "Barroso", "Damasceno", "Gimenes", "Fraga", "Ruiz", "Falcão", "Machado", "Simões", "Lopes", "Monteiro", "Silveira"]
    __ages = ["18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"]
    __ceps = ["83305-500", "68371-360", "36081-770", "54786-220", "72872-385", "77415-862", "65042-240", "44044-257", "91360-160", "49072-600", "83221-160", "64211-140", "72901-718", "50900-230"]

    def __init__(self, max: int = 1000) -> None:
        super().__init__()
        self.__NUMBER_CONSUMERS = max

    def populate(self) -> None:
        print("populating consumers...")
        consumers = open("consumers.csv", "w")
        consumers.write("id, name, age, CEP, wallet\n")
        for i in range(self.__NUMBER_CONSUMERS):
            id_ = self._unique_id()
            name = f'{self.__get_first()} {self.__get_last()}'
            if bool(random.getrandbits(1)):
                name = f'{name} {self.__get_last()}'

            age = self.__ages[generate_pos(len(self.__ages))]
            cep = self.__ceps[generate_pos(len(self.__ceps))]
            wallet =  round(random.uniform(10, 5000),2)
            consumers.write(f'{id_}, {name}, {age}, {cep}, {wallet}\n')
        consumers.close()

    def __get_first(self) -> str:
        return self.__first_names[generate_pos(len(self.__first_names))]

    def __get_last(self) -> str:
        return self.__last_names[generate_pos(len(self.__last_names))]

class Products(BaseGen):
    __produtos = ["battery", "bateria", "batteries", "power supply", "led lights", "battery charger", "trash can", "car battery", "fluke", "laser", "kabel", "multimeter", "led strip", "carregador iphone", "switch controller", "fichario", "bateria carro", "arduino", "bateria de carro", "led rgb", "camera", "câmera", "moto g10", "polaroid", "s20 fe", "nikon", "camera canon", "instax", "camera fotografica", "moto g9", "camera polaroid", "instax mini", "câmera fotográfica", "papel de parede cinza", "monitor ultrawide", "ipad", "moto g9 plus", "motorola g10", "moto g10 plus", "notebook samsung i7", "samsung s20 fe", "papel de parede branco", "moto g 10", "camera de segurança wifi", "instax mini 11", "vinho", "chocolate", "cerveja", "whisky", "gin", "queijo", "bebedouro", "jack daniels", "vodka", "mercado livre", "malbec", "dolce gusto", "espumante", "doces", "cacau show", "pasta", "carrefour", "cafeteira", "heineken", "morango", "leite condensado", "cortina para sala", "açúcar", "barra de chocolate", "leite ninho"]

    def populate(self) -> None:
        print("populating products...")
        products = open("products.csv", "w")
        products.write("id, name, serial_number, amount, price\n")
        for prod in self.__produtos:
            id_ = self._unique_id()
            amount = generate_pos(1000)
            price =  round(random.uniform(10, 2000),2)
            products.write(f'{id_}, {prod}, {self.__serial_number()}, {amount}, {price}\n')
        products.close()

    
    def __serial_number(self) -> str:
        return '-'.join([str(generate_pos(10000, 1000)) for i in range(4)])
    
class Orders(BaseGen):
    def __init__(self, n_cons: int = 1000) -> None:
        super().__init__()
        self.__NUMBER_CONSUMERS = n_cons

    def populate(self, consumers_ids: list, products_ids: list) -> None:
        print("populating orders...")
        orders = open("orders.csv", "w")
        orders.write("id, consumer_id, product_id, amount\n")
        random.shuffle(consumers_ids)
        for cons_id in consumers_ids:
            for n in range(random.randrange(1,8)):
                product_id = products_ids[generate_pos(len(products_ids))]
                amount = generate_pos(10)
                order_id = self._unique_id()
                orders.write(f'{order_id}, {cons_id}, {product_id}, {amount}\n')
        orders.close()