from pwn import *
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = ""
while True:
    try:
        con = remote("challenge.ctf.games", 31260)
        for i in range(30):
            con.recvuntil(b"> ")
            request = con.recvline().decode()[:-1]
            request_name, request_date = request.split(" (")
            request_date = request_date[:-1]
            print(i+1, request_name, request_date)
            movie_list = str(tmdb.search_movie(request_name + " " + request_date[:4]))
            print(request_name + " " + request_date[:4])
            print(movie_list)
            movie_id = movie_list[movie_list.find("id:")+3: movie_list.find("[http]")]
            print(movie_id)
            movie = tmdb.get_movie(movie_id)
            actors = [str(person) for person in movie.data["cast"]]
            print("; ".join(actors).encode())
            con.sendline("; ".join(actors[:5]).encode())
        print(con.recvline())
        print(con.recvline())
        print(con.recvline())
        print(con.recvline())
        print(con.recvline())
        print(con.recvline())
        print(con.recvline())
    except:
        pass