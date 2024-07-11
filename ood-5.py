print("*** Rabbit & Turtle ***")
input_data = input("Enter Input : ").strip()
d, Vr, Vt, Vf = map(int, input_data.split())

t = d / (Vt - Vr)

distance_fly = Vf * t

print(f"{distance_fly:.2f}")