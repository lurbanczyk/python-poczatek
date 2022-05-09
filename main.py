import ten

distance = float(input(("podaj dystans ")))
time = float(input('podaj czas w jakim pokonałes dystans '))

av_speed = ten.av_speed(distance, time)

print(f"twoja średnia prędkość to {av_speed}km/h")
