import sys
import random
from faker import Faker
import pyjokes
import cowsay

def excuse():
    fake = Faker()
    buzzword = random.choice([
        "blockchain database", "AI powered mainframe", "cloud native kubarnetes", "production microservice", "legacy COBOL router", "quantam firewall"
    ])

    joke = pyjokes.get_joke()

    templates = [
        f"Listeen, servers are imploded bcz of {joke}",
        f"Critical failure! {buzzword} is down. because {joke}",
        f"Sorry boss!!!! {fake.company()} servers are burned. all I can say is: {joke}"
    ]

    # print("function")

    cowsay.cow(random.choice(templates))

    # print("1")

def main(exctype, value, traceback):
    print(f"CRASH DETECTED: {exctype.__name__}: {value}\n")

    excuse()

sys.excepthook = main
