from services.movie_services import MovieServices
from services.movie_analysis_services import MovieAnalysis
movie_service = MovieServices()
movies_analysis = MovieAnalysis()


def start_menu():
    while True:
        print(f"""
1. Movie Services
2. Movie Analysis
0. Exit
              """)
        choice = input("choose an option : ")
        if choice == "1":
            print(f"""
1. add movie
2. delete movie
3. search movie
4. update movie
5. search movie by genre
6. set movie as done
0. Exit          
                 """)
            if choice == "1":
                title= input("enter title : ")
                genre = input("enter genre : ")
                director = input("enter director : ")
                year = int(input("enter year : "))
                done = input("have you watched this movie (yes/no) : )")
                rating = int(input("enter your rating(/10) : "))
                if done.strip().lower() == "yes":
                    done = True
                elif done.strip().lower() == "no":
                    done = False
                else:
                    print("wrong data")
                result =  movie_service.add_movie(
                    title = title,
                    genre = genre,
                    director = director,
                    year = year,
                    done = done,
                    rating = rating,
                )
                if result:
                    print("movie has been added succesfully ! ")
                else:
                    print("something went wrong")
                
            elif choice == "2":
                title= input("enter title : ")
                director = input("enter director : ")
                year = int(input("enter year : "))
                result = movie_service.delete_movie(title = title,
                                                    director = director,
                                                    year = year)
                if result:
                        print("movie has been delete succesfully ! ")
                else:
                        print("something went wrong")
            elif choice == "3":
                title= input("enter title : ")
                director = input("enter director : ")
                year = int(input("enter year : "))
                result = movie_service.search_movie(title = title,
                                                    director = director,
                                                    year = year)
                if result:
                    print(result)
                else:
                    print("something went wrong")
            elif choice == "4":
                title = input("enter current title : ")
                year = int(input("enter current year : "))
                director = input("enter current director :")
                new_title = input("enter new title (leave empty if nessecary) : ")
                new_year = int(input("enter new year (leave empty if nessecary) : "))
                new_director = input("enter new director (leave empty if nessecary) : ")
                new_rating = input("enter new rating (leave empty if nessecary) : ")
                result = movie_service.update_movie(title = title,
                                                    year = year,
                                                    director = director,
                                                    new_director=new_director,
                                                    new_title=new_title,
                                                    new_rating=new_rating,
                                                    new_year=new_year)
                if result:
                    print("movie has been updated succesfully ! ")
                else:
                    print("something went wrong")
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "0":
                break
            else:
                print("incorrect choice")