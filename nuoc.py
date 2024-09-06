import requests

def get_country_info(country_name):
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    data = response.json()
    
    for country in data:
        if country.get("name", {}).get("common", "").lower() == country_name.lower() or country.get("name", {}).get("official", "").lower() == "people's republic of china":
            return {
                "Tên đầy đủ": country.get("name", {}).get("common", "Không có thông tin"),
                "Tên chính thức": country.get("name", {}).get("official", "Không có thông tin"),
                "Thủ đô": country.get("capital", ["Không có thông tin"])[0],
                "Dân số": country.get("population", "Không có thông tin"),
                "Diện tích": country.get("area", "Không có thông tin"),
                "Khu vực": country.get("region", "Không có thông tin"),
                "Tiểu khu": country.get("subregion", "Không có thông tin"),
                "Tiền tệ": ', '.join([currency for currency in country.get("currencies", {}).keys()]),
                "Ngôn ngữ": ', '.join([lang for lang in country.get("languages", {}).values()]),
                "Biên giới": ', '.join(country.get("borders", [])),
                "Múi giờ": ', '.join(country.get("timezones", [])),
                "Tên miền quốc gia": ', '.join(country.get("topLevelDomain", [])),
                "Biểu ngữ": country.get("flags", {}).get("png", "Không có thông tin"),
                "Mã ISO 3166-1": country.get("cca2", "Không có thông tin")
            }
    
    return None

country_name = input("Nhập tên quốc gia: ")
info = get_country_info(country_name)

if info:
    for key, value in info.items():
        print(f"{key}: {value}")
else:
    print("Không tìm thấy thông tin cho quốc gia này.")

