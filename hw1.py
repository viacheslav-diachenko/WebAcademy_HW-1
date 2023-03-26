def greet(name, greeting="Привіт"):
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    name = "Світ"
    print(greet(name))
    print(greet(name, "Вітаю"))