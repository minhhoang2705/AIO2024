def calculate_can_chi_calendar(year: int) -> str:
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi"]
    for i in range(0, len(can)):
        for j in range(0, len(chi)):
            if year % 10 == i and year % 12 == j:
                result = can[i] + " " + chi[j]
                return result
    return result

if __name__ == "__main__":
    print(calculate_can_chi_calendar(2024))
    print(calculate_can_chi_calendar(2023))
    print(calculate_can_chi_calendar(1997))