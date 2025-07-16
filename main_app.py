import geometry_calculator
import greetings
import math_utils
import list_utils
import number_generator

if __name__ == "__main__":
    print("\n\033[36mWillkommen zu meiner eigenen Modul-Anwendung!\033[0m\n")
    # Geometry Calculator
    try:
        seite_a = float(input("Gebe die Länge von Seite A an: "))
        seite_b = float(input("Gebe die Länge von Seite B an: "))

        print(f"Die Hypotenuse des Dreiecks ist {geometry_calculator.calculate_hypotenuse(seite_a, seite_b):.2f} Einheiten lang.")

    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")

    # Greetings
    greetings.say_hello("Efrahim")

    # Math Utils
    print(f"2 + 4 = {math_utils.add(2, 4)}")
    print(f"10 - 3 = {math_utils.subtract(10, 3)}")
    print(f"3 * 5 = {math_utils.multiply(3, 5)}")
    print(f"9 / 2 = {math_utils.divide(9, 2)}")
    print(f"9 // 2 = {math_utils.divide(9, 2, isIntegerDivision=True)}")
    print(f"2⁵ = {math_utils.pow(2, 5)}")
    print(f"3. Wurzel aus 81 = {math_utils.root(81, 3)}")

    # List Utils
    liste = ["a", "a", "b", "c", "d", "e", "e"]
    print(liste)
    neue_liste = list_utils.remove_duplicates(liste)
    print(neue_liste)


    # Number Generator
    # Generiere eine Liste mit 10 Zufallszahlen zwischen 1 und 50.
    numbers = number_generator.generate_random_numbers(10, 1, 50)
    print(numbers)

    # Finde höchsten Wert
    print(list_utils.find_max(numbers))
