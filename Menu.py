from Program import GraphProgram

class Menu:
    def __init__(self, program):
        self.program = program

    def show_menu(self):
        print()
        print("--------------------------------")
        print("""
MENU
1) Guardar el grafo en archivo .GRAPHML""")

        self.get_menu_answer()

    def get_menu_answer(self):
        option = input("Opción: ")
        print()

        if option == "1":
            print("-----------Create GRAPHML-----------")
            print()
            self.program.save_graph()
            self.show_menu()