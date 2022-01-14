"""Money generator module"""
ef generateMoney():
    """Return money generated"""
    value = input('How much would you like to generate?\n')
    print("Generating $$$...")
    try:
        int(value)
        print("You have generated $" + value)
    except:
        print("Huh? Unable to generate that...")

if __name__ == "__main__":
    generateMoney()
