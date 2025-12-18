import datetime

class PetCareChatbot:
    def __init__(self):
        self.pet_database = {
            "pişik": {
                "yemək": "Gündə 2 dəfə yüksək keyfiyyətli yem.",
                "su": "Həmişə təzə su.",
                "təmizlik": "Həftədə 2-3 dəfə dəsti, ayda bir hamam.",
                "sağlamlıq": "İllik veterinar yoxlaması.",
                "oyun": "Gündə 20-30 dəqiqə oyun."
            },
            "it": {
                "yemək": "Gündə 1-2 dəfə yaşa uyğun yem.",
                "su": "Su qabı həmişə dolu.",
                "təmizlik": "Həftədə bir dəfə hamam.",
                "sağlamlıq": "İllik veterinar yoxlaması.",
                "gəzintı": "Gündə 2 dəfə 20-30 dəqiqə."
            },
            "quş": {
                "yemək": "Xüsusi yem qarışığı, təzə tərəvəz.",
                "su": "Su hər gün təzələnməli.",
                "təmizlik": "Qəfəs həftədə 2 dəfə təmizlənməli.",
                "sağlamlıq": "Dimdik və dırnaq nəzarəti.",
                "əyləncə": "Qəfəsdə oyuncaqlar olmalı."
            },
            "balıq": {
                "yemək": "Gündə 1-2 dəfə az miqdarda yem.",
                "su": "Yüksək keyfiyyətli su, daimi filtr.",
                "təmizlik": "Akvarium 2-4 həftədə bir təmizlənməli.",
                "sağlamlıq": "Su parametrlərinin nəzarəti.",
                "mühit": "Gizlənmək üçün yerlər olmalı."
            }
        }
        
        self.problems = {
            "yemək yemir": {
                "səbəblər": ["Stress", "Xəstəlik", "Yeni mühit"],
                "həll yolları": [
                    "Veterinara müraciət",
                    "Yemək növünü dəyişin",
                    "Stressi aradan qaldırın"
                ]
            },
            "tük tökür": {
                "səbəblər": ["Mövsümi dəyişikliklər", "Qidalanma", "Stress"],
                "həll yolları": [
                    "Tez-tez dəsti edin",
                    "Qidasını yaxşılaşdırın",
                    "Veterinara müraciət edin"
                ]
            },
            "əhvalı pisdir": {
                "səbəblər": ["Xəstəlik", "Kədər", "Yalnızlıq"],
                "həll yolları": [
                    "Daha çox diqqət göstərin",
                    "Veterinara müraciət edin",
                    "Yeni oyuncaqlar verin"
                ]
            }
        }
        
        self.current_pet = None
    
    def start_chat(self):
        print("Ev Heyvanlarına Baxış Botuna Xoş Gəlmisiniz!")
        print("Əsas komandalar: 'heyvan seç', 'məlumat', 'problem', 'yemək tövsiyəsi', 'gündəlik qayğı', 'çıxış'")
        
        while True:
            user_input = input("\nSizin sorğunuz: ").lower()
            
            if user_input == 'çıxış':
                print("Sag olun!")
                break
            elif user_input == 'heyvan seç':
                self.select_pet()
            elif user_input == 'məlumat':
                self.get_pet_info()
            elif user_input == 'problem':
                self.solve_problem()
            elif user_input == 'yemək tövsiyəsi':
                self.get_food_recommendation()
            elif user_input == 'gündəlik qayğı':
                self.create_daily_care_plan()
            elif 'salam' in user_input:
                print("Salam! Kömək edə bilərəm?")
            else:
                print("Əsas komandalardan birini yazın.")
    
    def select_pet(self):
        print("\nHeyvan növləri:")
        for i, pet in enumerate(self.pet_database.keys(), 1):
            print(f"{i}. {pet.capitalize()}")
        
        while True:
            choice = input("\nHeyvan seçin: ").lower()
            
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(self.pet_database):
                    self.current_pet = list(self.pet_database.keys())[index]
                    break
            elif choice in self.pet_database:
                self.current_pet = choice
                break
            else:
                print("Yanlış seçim!")
        
        print(f"{self.current_pet.capitalize()} seçdiniz!")
    
    def get_pet_info(self):
        if not self.current_pet:
            print("Əvvəlcə heyvan seçin.")
            return
        
        print(f"\n{self.current_pet.capitalize()} üçün baxış tələbləri:")
        
        pet_info = self.pet_database[self.current_pet]
        for category, info in pet_info.items():
            print(f"\n{category.capitalize()}:")
            print(f"  {info}")
    
    def solve_problem(self):
        if not self.current_pet:
            print("Əvvəlcə heyvan seçin.")
            return
        
        print(f"\nProblemlər:")
        for i, problem in enumerate(self.problems.keys(), 1):
            print(f"{i}. {problem.capitalize()}")
        
        while True:
            choice = input("\nProblem seçin: ").lower()
            
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(self.problems):
                    selected_problem = list(self.problems.keys())[index]
                    self.show_problem_solution(selected_problem)
                    break
            elif choice in self.problems:
                self.show_problem_solution(choice)
                break
            else:
                print("Yanlış seçim!")
    
    def show_problem_solution(self, problem):
        print(f"\n{problem.capitalize()} üçün həll yolları:")
        
        problem_info = self.problems[problem]
        
        print("\nSəbəblər:")
        for cause in problem_info["səbəblər"]:
            print(f"- {cause}")
        
        print("\nHəll yolları:")
        for solution in problem_info["həll yolları"]:
            print(f"- {solution}")
    
    def get_food_recommendation(self):
        if not self.current_pet:
            print("Əvvəlcə heyvan seçin.")
            return
        
        print(f"\n{self.current_pet.capitalize()} üçün yemək tövsiyələri:")
        
        if self.current_pet == "pişik":
            print("- Yüksək proteinli quru yem")
            print("- Konservə edilmiş yaş yem")
            print("- Bişmiş toyuq")
        elif self.current_pet == "it":
            print("- Yaşa uyğun quru yem")
            print("- Konservə edilmiş yaş yem")
            print("- Bişmiş ət")
        elif self.current_pet == "quş":
            print("- Xüsusi yem qarışığı")
            print("- Təzə tərəvəzlər")
            print("- Meyvələr")
        elif self.current_pet == "balıq":
            print("- Növünə uyğun yem")
            print("- Canlı yem")
            print("- Bitki əsaslı yem")
    
    def create_daily_care_plan(self):
        if not self.current_pet:
            print("Əvvəlcə heyvan seçin.")
            return
        
        print(f"\n{self.current_pet.capitalize()} üçün gündəlik plan:")
        
        if self.current_pet == "pişik":
            print("07:00 - Səhər yeməyi")
            print("12:00 - Oyun vaxtı")
            print("18:00 - Axşam yeməyi")
            print("21:00 - Axşam oyunu")
        elif self.current_pet == "it":
            print("07:00 - Səhər gəzintisi")
            print("07:30 - Səhər yeməyi")
            print("18:00 - Axşam gəzintisi")
            print("18:45 - Axşam yeməyi")
        elif self.current_pet == "quş":
            print("08:00 - Yem və su təzələnməsi")
            print("12:00 - Təzə tərəvəz")
            print("18:00 - Axşam yeməyi")
            print("20:00 - Qəfəsi örtün")
        elif self.current_pet == "balıq":
            print("09:00 - Birinci yemləmə")
            print("19:00 - İkinci yemləmə")
            print("21:00 - İşıqları söndürün")

if __name__ == "__main__":
    chatbot = PetCareChatbot()
    chatbot.start_chat()
