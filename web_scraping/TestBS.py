from bs4 import BeautifulSoup
import requests

def SearchTag(soup):
    TagName = input("\nInsert Tag to search: ")
    Output = []
    check = False
    Attribute = input(f"\nDo you want to search {TagName} by attribute? (Y/N): ")
    if Attribute == "N" or Attribute == "n":
        All = input(f"\nDo you want to search all {TagName} tags? (Y/N): ")
        if All == "Y" or All == "y":
            Output = soup.find_all(TagName)
            check = True
        elif All == "N" or All == "n":
            Output = soup.find(TagName)
            check = True
        else:
            print("\nNon-existant choice")
    elif Attribute == "Y" or Attribute == "y":
        Attr = int(input("\nDo you want to search by:\n\t1) Class\n\t2) Id\n\nInsert choice: "))
        if Attr == 1:
            AttrType = "class"
            AttrName = input("\nInsert class name: ")
        elif Attr == 2:
            AttrType = "id"
            AttrName = input("\nInsert id name: ")
        if Attr == 1 or Attr == 2:
            All = input(f"\nDo you want to search all {TagName} tags? (Y/N): ")
            if All == "Y" or All == "y":
                Output = soup.find_all(TagName, {AttrType: AttrName})
                check = True
            elif All == "N" or All == "n":
                Output = soup.find(TagName, {AttrType: AttrName})
                check = True
    else:
        print("\nNon-existant choice")
    if check:
        print(Output, sep="\n")

while True:
    link = input("\nInsert link:  ")
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    print("\nChoose option")
    print("Option 1: Search by Tag (only one working)")
    print("Option 2: Search by Class")
    print("Option 3: Search by Id")
    print("Option 4: Search by Title")
    print("Option 0: Exit the program")
    choice = int(input())
    if choice == 0:
        break
    elif choice != 1 and choice !=2 and choice != 3 and choice != 4:
        print("\nNon-existent choice")
        continue
    elif choice == 1:
        SearchTag(soup)


#----

# weather_list = []
# class_list = soup.find_all("div", {"class": "containerInfoInfernalChart"})
# for container in class_list:
#     hour = container.find("time").get_text()

#     day = soup.find("a", {"class": "selectedDayOfWeek"}).find("span", {"class": "date"}).get_text()
#     temp = container.find("span", {"class": "replacedH5Temperature"}).get_text()
#     weather = container.find("div", {"class": "rowCentralInfo"}).find("img").get("alt")
#     end_p = container.find("div", {"class": "containerEndingInfo"}).find_all("p")
#     rain_type = end_p[0].find("img").get("alt")
#     rain = end_p[0].find("span").get_text()
#     rain = rain[:-1]
#     wind_type = end_p[1].find("img").get("alt")
#     wind_km = end_p[1].find("span").find_all("span")
#     wind_km_min = wind_km[0].get_text()
#     wind_km_max = wind_km[1].get_text()
#     wind_dir = end_p[2].find("span").get_text()

#     weather_list.append( info(hour, day, weather, temp, rain, rain_type, wind_dir, wind_km_min, wind_km_max, wind_type) )

# print values
# for obj in weather_list:
#     print()
#     obj.print_values()