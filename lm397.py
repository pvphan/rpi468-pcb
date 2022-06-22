
def main():
    V_S = 5.0
    R1 = 1000000
    R2 = 10000
    R3 = 500000
    V_T1 = ((V_S * R2) / (((R1 * R3) / (R1 + R3)) + R2))
    V_T2 = V_S * ((R2 * R3) / (R2 + R3)) / (R1 + ((R2 * R3) / (R2 + R3)))
    print(f"V_T1 = {V_T1:0.4f}")
    print(f"V_T2 = {V_T2:0.4f}")


if __name__ == "__main__":
    main()
