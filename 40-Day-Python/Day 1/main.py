def calculate_can_chi_calendar(year: int) -> str:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer.")

    celestial_stems = [
        "Canh",
        "Tân",
        "Nhâm",
        "Quý",
        "Giáp",
        "Ất",
        "Bính",
        "Đinh",
        "Mậu",
        "Kỷ",
    ]
    terrestrial_branches = [
        "Thân",
        "Dậu",
        "Tuất",
        "Hợi",
        "Tý",
        "Sửu",
        "Dần",
        "Mão",
        "Thìn",
        "Tị",
        "Ngọ",
        "Mùi",
    ]

    stem_idx = year % 10
    branch_idx = year % 12

    if stem_idx < len(celestial_stems) and branch_idx < len(terrestrial_branches):
        stem = celestial_stems[stem_idx]
        branch = terrestrial_branches[branch_idx]
        return f"{stem} {branch}"

    # Return "Invalid year" if the year doesn't match any combination
    return "Invalid year"


if __name__ == "__main__":
    print(calculate_can_chi_calendar(2024))
    print(calculate_can_chi_calendar(2023))
    print(calculate_can_chi_calendar(1997))
