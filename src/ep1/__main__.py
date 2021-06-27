if __name__ == "__main__":
    try:
        while True:
            test = input("Do you want to test the QR_algorithm(1) or QR_fatoration(0): ")
            if (test == "1"):
                test_qr_algorithm()
                print("\n")
            elif (test == "0"):
                test_qr_fatoration()
                print("\n")
            else:
                print(" your input isn't valid \nplease, try again\n")

    except KeyboardInterrupt:
        print("\nBetter luck next time")
    pass
