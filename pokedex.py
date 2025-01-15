import mysql.connector
import time
from unidecode import unidecode

class Menu():
    def __init__(self):
        self.linhasCima = '~'*10
        self.linhasBaixo = '~'*29
    
    def menu1(self):
        print(f"{self.linhasCima} POKÉDEX {self.linhasCima}\n (1) - Iniciar\n (2) - Sair \n {self.linhasBaixo}")
        response = input('Digite o número da opção escolhida: ') 
        return response
    
    def menu2(self):
        print(f"{self.linhasCima} Buscar {self.linhasCima}\n (1) - Listar pokemons\n (2) - Numero da pokédex\n (3) - Nome do pokémon\n (4) - Tipo do pokémon\n (5) - Lendários\n {self.linhasBaixo}")
        response = input('Digite o número da opção escolhida: ')
        return response

    def escolha2(self,resp,pkdx):
        match resp:
            case '1':
                pkdx.listar_pokemons()
            
            case '2':
                pkdx.buscar_pokemon_por_numero_pokedex()
            case '3':
                pkdx.buscar_pokemon_por_nome()    
            case '4':
                pkdx.buscar_pokemon_por_tipo()    
                
            case '5':
                pkdx.buscar_se_lendario() 
            
            case _:
                print('Opção inválida!')
                

        
class Pokedex:
    def __init__(self, bd):
        self.pokemons = []
        query = "SELECT * FROM pokemon;"
        bd.cursor.execute(query)
        result = bd.cursor.fetchall()
        for pokemon in result:
            self.pokemons.append(pokemon) if None not in pokemon else 0
    
    def buscar_pokemon_por_numero_pokedex(self):
        numero_pokedex = input("Digite o número da pokédex do pokémon desejado: ")
        for pokemon in self.pokemons:
            if pokemon[0] == int(numero_pokedex):
                print(f"-=-=-=-=-= Número pokedex: {pokemon[0]} =-=-=-=-=-\n")
                print(f"Nome: {pokemon[1]}")
                print(f"Tipo: {pokemon[2]}")
                print(f"Descrição: {pokemon[3]}")
                print(f"Altura: {pokemon[4]}")
                print(f"Peso: {pokemon[5]}")
                print(f"Habilidades: {pokemon[6]}")
                print(f"É lendário?: ",end = "")
                print("Sim") if pokemon[7] == True else print("Não")
        
    def buscar_pokemon_por_nome(self):
        nome = input("Digite o nome do pokémon a ser buscado: ")
        for pokemon in self.pokemons:
            if nome.lower() in pokemon[1].lower() :
                print(f"-=-=-=-=-= Número pokedex: {pokemon[0]} =-=-=-=-=-\n")
                print(f"Nome: {pokemon[1]}")
                print(f"Tipo: {pokemon[2]}")
                print(f"Descrição: {pokemon[3]}")
                print(f"Altura: {pokemon[4]}")
                print(f"Peso: {pokemon[5]}")
                print(f"Habilidades: {pokemon[6]}")
                print(f"É lendário?: ",end = "")
                print("Sim") if pokemon[7] == True else print("Não")
                
    def buscar_pokemon_por_tipo(self):
        while True:
            tipos = ["Fogo","Água","Elétrico","Psíquico","Terrestre",
                 "Planta","Lutador", "Pedra", "Normal", "Gelo","Fada"
                 ,"Venenoso","Inseto","Dragão", "Voador","Fantasma","Metal"]
            print(f"{'~'*10} Lista dos tipos {'~'*10}")
            i = 1
            try: 
                for tipo_print in tipos:
                    print(f'({i}) - {tipo_print}')
                    i += 1
                tipo = int(input("Digite o tipo para buscar: "))  
                for pokemon in self.pokemons:
            
                    if tipos[tipo-1].lower() in unidecode(pokemon[2].lower()):
                        print(f"-=-=-=-=-= Número pokedex: {pokemon[0]} =-=-=-=-=-\n")
                        print(f"Nome: {pokemon[1]}")
                        print(f"Tipo: {pokemon[2]}")
                        print(f"Descrição: {pokemon[3]}")
                        print(f"Altura: {pokemon[4]}")
                        print(f"Peso: {pokemon[5]}")
                        print(f"Habilidades: {pokemon[6]}")
                        print(f"É lendário?: ",end = "")
                        print("Sim") if pokemon[7] == True else print("Não")
                
                
                
            except (ValueError, IndexError):
                print("Tente novamente com o valor correto!")
                continue
            break
        
    def buscar_se_lendario(self):
        while True:
            print(f"{'~'*10} Filtrar lendários {'~'*10}\n (1) - Mostrar lendários\n (2) - Mostrar não-lendários")
            response = input('Digite o número da opção escolhida: ')
            if response == "1":
                response = 1
                break
            elif response == "2":
                response = 0
                break
            else:
                print("Digite o valor correto. ")
                continue
            
        for pokemon in self.pokemons:
            if response == int(pokemon[7]):
                print(f"-=-=-=-=-= Número pokedex: {pokemon[0]} =-=-=-=-=-\n")
                print(f"Nome: {pokemon[1]}")
                print(f"Tipo: {pokemon[2]}")
                print(f"Descrição: {pokemon[3]}")
                print(f"Altura: {pokemon[4]}")
                print(f"Peso: {pokemon[5]}")
                print(f"Habilidades: {pokemon[6]}")
                print(f"É lendário?: ",end = "")
                print("Sim") if pokemon[7] == True else print("Não")
                
           

    def listar_pokemons(self):
        pagina_escolhida = 0
        paginas = len(self.pokemons) // 50
        i = 0
        while True:
            
            try:
                if i == pagina_escolhida + 51:
                    pagina_escolhida = (int(input(f'Digite o número da página: ({pagina_escolhida/50+1:,.0f}/{paginas}) ( outro caractere para sair):\n '))-1) * 50
                    i = pagina_escolhida
                        
                print(f"-=-=-=-=-= Número pokedex: {self.pokemons[i][0]} =-=-=-=-=-\n")
                print(f"Nome: {self.pokemons[i][1]}")
                print(f"Tipo: {self.pokemons[i][2]}")
                print(f"Descrição: {self.pokemons[i][3]}")
                print(f"Altura: {self.pokemons[i][4]}")
                print(f"Peso: {self.pokemons[i][5]}")
                print(f"Habilidades: {self.pokemons[i][6]}")
                print(f"É lendário?: ",end = "")
                print("Sim") if self.pokemons[i][7] == True else print("Não")
                i += 1
            except (IndexError, ValueError):
                break            

    
        
class BancoDeDados:
    def __init__(self, host="localhost", usuario="root", senha="root", db_name="pokedex"):
        # Conecta ao banco de dados MySQL
        self.__conn = mysql.connector.connect(
            host=host,
            user=usuario,
            password=senha,
            database=db_name
        )
        self.cursor = self.__conn.cursor()
        
        @property
        def conn(self):
            return self.__conn
        
        @conn.setter
        def conn(self,conn):
            self.__conn = conn
            
    def fechar_conexao(self):
        self.conn.close()

bd = BancoDeDados()
pokedex = Pokedex(bd)
menu = Menu()

while True:    
    response = menu.menu1()
    match response:
        case '1':
            response = menu.menu2()
            menu.escolha2(response,pokedex)
        case '2':
            print('Você esolheu sair...')
            
            break

bd.fechar_conexao()       
