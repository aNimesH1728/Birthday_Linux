import sys
from ascii_art import cake,wish
from wish_generator import generate_wish

if __name__=="__main__":
    if(len(sys.argv)<2):
        print("Usage ./greeter.py <Name> [traits]")
        sys.exit(1)
    
    name=sys.argv[1]
    traits=" ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""

    cake()
    wish()

    try:
        bday_wish=generate_wish(name,traits)
        print(bday_wish)
    except Exception as e:
        print(f"Error Generating the wish : {e}")
    
