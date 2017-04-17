import csv
import Tkinter
from collections import Counter
from matplotlib import pyplot as plt
MY_FILE="my_file.csv"
def parse(raw_file,delimiter):
	"""parses a raw csv file in a json line object"""
	opened_file=open(raw_file)
	csv_data=csv.reader(opened_file,delimiter=delimiter)
	parsed_data=[]
	fields=csv_data.next()
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	opened_file.close()
	return parsed_data

def visualize_days():
    """Visualize data by day of week"""
    data_file = parse(MY_FILE, ",")
    # Returns a dict where it sums the total values for each key.
    # In this case, the keys are the DaysOfWeek, and the values are
    # a count of incidents.
    counter = Counter(item["3.75"] for item in data_file)
    #print counter
    # Separate out the counter to order it correctly when plotting.
    data_list = [counter["3.75"],
                 counter["3.52"],
                 counter["3.20"],
                 counter["3.48"],
                 ]
    day_tuple = tuple(["3.75", "3.52", "3.20", "3.48"])

    # Assign the data to a plot
    plt.plot(data_list)

    # Assign labels to the plot
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the plot!
    plt.savefig("Days.png")

    # Close figure
    plt.clf()

def main():
    visualize_days()

if __name__ == "__main__":
    main()