# favorite movies collection
# Ask the user to enter their favorite movies (store them in a set).
# Since sets do not allow duplicates, check if a movie already exists before adding.
# Provide options to:
# Add a new movie
# Remove a movie
# Show all movies in the collection


def get_menu_choice():
    """Display menu and get user choice."""
    print("\n" + "-"*25)
    print("FAVORITE MOVIES COLLECTION")
    print("-"*25)
    print("1. Add a new movie")
    print("2. remove a movie")
    print("3. Display all movies")
    print("4. Exit")
    print("-"*25)

    
    choice = input("Choose an option (1-4): ").strip()
    return choice





def add_movie(movies):
   
    while True:
        movie_name = input("Enter the name of your movie (or type 'stop' to exit): ").strip()

        if movie_name.lower() == "stop":
            break
        elif movie_name in movies:
            print("⚠️ Your movie is already in the list")
        elif not movie_name:
            print("❌ The name can't be empty")
        else:
            movies.add(movie_name)
            print(f"✅ '{movie_name}' has been added to the list")

def rem_movie(movies):
    """Supprimer un film du set"""
    movierem = input("Enter the name of the movie you want to delete: ").strip()
    if movierem in movies:
        movies.remove(movierem)
        print(f"✅ '{movierem}' has been removed from the list")
    else:
        print("❌ The movie does not exist in the collection")

def display_movie(movies):

    if not movies :
        print("There is no movie in the collection")
    else:
        for i, movie in enumerate(movies, start=1):
         print(f"{i}. {movie}")

        
    
   


def main():
    movies = set()
    
    print("Welcome to tour favorite movies collection!")

    while True : 
            choice = get_menu_choice()

            if choice == "1" :
                add_movie(movies)
            elif choice == "2" :
                rem_movie(movies)
            elif choice =="3" :
                display_movie(movies)
            elif choice == "4":
                break

if __name__ == "__main__":
    main()