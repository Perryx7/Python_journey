from random import choice

capital = "topeka"
bird = "western meadowlark"
flower ="sunflower"
song = "home on the range"


def randomfunfact() : 
    funfacts = [
        "herferbehferhieheeeerhberh",
        "dfhbvdfhbvjhbvjhbvdjhbvhfbv",
        "dfhbvhdfibvhdfbvhbvhdjbvhbvjhvf",
        "dfbjhbvhdjbvdhjbvhbvbvhdbvdlvbdv"

    ]


    index = choice("0123")

    print(funfacts[int(index)])


    if __name__ == "__main__" : 
     randomfunfact()