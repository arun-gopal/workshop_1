import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--film-name", help="Input the movie you want to review")
parser.add_argument("--stars", help="Input the review score")
args=parser.parse_args()
print(args.film_name)
print(args.stars)

with open("NewFile.txt", "a") as file:
    file.write(args.film_name + " " + args.stars + "\n")