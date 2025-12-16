notebook = {}
def create_note():
    global notebook
    header = input("Header: ")
    text = input("Text: ")
    notebook[header] = text
    print()
    
    def read_notes():
        global notebook
        
        if not notebook:
            print("Заметок нет.\n")
            return
        
        header_to_read = input("\nWhich note to read?\n\n>")
        if header_to_read in notebook:
            print(f"\n{notebook[header_to_read]}\n")
        else:
            print("\nТакой заметки нет\n")
            
            def delete_note():
                global notebook
                
                if not notebook:
                    print("Заметок нет.\n")
                    return
                headers = ", ".join(notebook.keys())
                print(headers)
                
                header_to_delete = input("\nWhiechnote to delete?\n\n> ")
                
                if header_to_delete in notebook:
                    notebook.pop(header_to_delete)
                    print(f"\nNote {header_to_delete} removed\n")
                else:
                    print("\nТакой заметки нет \n")
                    
                    def main():
                        while True:
                            print("[1] - Create a new note. [2] - Read all notes. [3] - Delete entry. [4] - Exit.\n")
                            
                            choice = input("> ")
                            print()
                            
                            if choice == "1":
                                create_note()
                            elif choice == "2":
                                read_notes()
                            elif choice == "3":
                                delete_note()
                            elif choice == "4":
                                print("Выход из программы.")
                                break
                            else:
                                print("Неверный выбор. Пожалуйста, выберите от 1 до 4.\n")
                                
                                if __name__ == "__main__":
                                    main()