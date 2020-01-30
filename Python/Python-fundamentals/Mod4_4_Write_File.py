# ASK 1
# CREATE A LOCAL FILE
# open in 'w' mode
# open inner_planets.txt in write mode 'w' to create a local file
# write the first four planets from the sun in earth's solar system (Mercury, Venus, Earth, Mars) on separate lines
# close the file and re-open in read mode 'r'
# use .read() to read the entire file contents
# print the entire file contents
# [ ] open planets.txt in write mode
# inner_plannets = open('inner_planets.txt', 'w')

# # [ ] write Mercury, Venus, Earth, Mars on separate lines
# inner_plannets.write("Mercury\nVenus\nEarth\nMars")

# # [ ] close the file and re-open in read mode
# inner_plannets.close()


# # [ ] use .read() to read the entire file contents
# new_plannets = open('inner_planets.txt', 'r')

# plannets = new_plannets.read()

# print(plannets)

# new_plannets.close()

# [ ] print the entire file contents and close the file
# TASK 2
# USING .SEEK(0) ON A LOCAL FILE IN WRITE PLUS READ MODE 'W+'
# open outer_planets.txt in 'w+' mode (write plus read)
outer_planets = open("outer_planets.txt", "w+")
# open outer_planets.txt in write plus read mode 'w+'
# write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines
outer_planets.write("(Jupiter\nSaturn\nUranus\nNeptune)")
# use .seek() to move the pointer to the start of the file
outer_planets.seek(0)
planets = outer_planets.read().strip("()\n")
print(planets)
# use .read() to read the entire file contents
# print the entire file contents and close the file
# [ ] open outer_planets.txt in write mode 'w+' 
outer_planets.close()

# [ ] write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines


# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents


# [ ] print the entire file contents and close the file


