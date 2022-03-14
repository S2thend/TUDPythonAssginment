def opSelect():
    while True:
        try:
            op = int(input("Enter op number to exec(i.e. enter 1 to perform 1.Find all..):"))
            if op == 1 or op == 2 or op == 3:
                return op
            else:
                print("Wrong Input, Only 1 or 2 or 3 allowed, try again")

        except ValueError:
            print("Wrong Input, Please Try again")


def main():
    try:
        file = open("movie_list.txt","r")
    except IOError:
        print("Can't read file movie_list.txt in current directory")
        return 0

    db = dict()
    for line in file:
        starring = line.split(", ")
        for i in range(1,len(starring)):
            movie_tuple = ( starring[i].split(" (")[0], starring[i].split(" (")[1].replace(")","").strip())
            try:
                db[movie_tuple].add(starring[0])
            except:
                db[movie_tuple] = set()
                db[movie_tuple].add(starring[0])

    file.close()

    print(db)
                
    print("Choose the operation to perform:")
    print("1.Find all the actors in those movies")
    print("2.Find the common actors in the two movies")
    print("3.Find the actors who are in either of the movies but not both")

    op = opSelect()

    while True:
        movie_n1 = input("Enter 1st Movie Name:")
        movie_y1 = input("Enter year of production for 1st movie:")
        if (movie_n1,movie_y1) in db:
            break
        else:
            print("Movie not exit in db, try agian")

    while True:
        movie_n2 = input("Enter 2nd Movie Name:")
        movie_y2 = input("Enter year of production for 2nd movie:")
        if (movie_n2,movie_y2) in db:
            break
        else:
            print("Movie not exit in db, try agian")

    if op == 1:
        print(db[(movie_n1,movie_y1)] | db[(movie_n2,movie_y2)])
    if op == 2:
        print(db[(movie_n1,movie_y1)] & db[(movie_n2,movie_y2)])
    if op == 3:
        print(db[(movie_n1,movie_y1)] ^ db[(movie_n2,movie_y2)])

    return 

main()



