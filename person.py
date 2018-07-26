# def build_person(first_name, last_name):
#     """사람에 관한 정보 딕셔너리를 반환합니다."""
#     person={'first':first_name, 'last':last_name}
#     return person

# musician=build_person('jin', 'yujung')
# print(musician)


def city_country(city, country):
    person={'ci':city, 'ct':country}
    return person

ci_country=city_country('Santiago', 'Chile')
for key, value in ci_country.items():
    print(value)