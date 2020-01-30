#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
weather = open('mean_temp.txt', 'a+')
weather.write("Rio de Janeiro,Brazil,30.0,18.0\n")
weather.seek(0)
headings = weather.readline().strip()
print(headings)
city_list = weather.readline().split(',')
line = weather.readline()
while line:
    string = line.split(',')
    print(city_list[0].title(), "of", string[0], city_list[2], "is", string[2], "Celcius")
    line = weather.readline()
weather.close()