import csv


#################################################################
def main():

    with open('data.csv') as file:
        readerobject = csv.reader(file, delimiter=',',)

        count = 0

        # For every row in file
        for row in readerobject:

            # If we're on row 0, the headder row, just print the headder names, do not process.
            if count == 0:
                count += 1  # increase the count before exiting loop, so that we don't get stuck here forever.
                pass
                # print(row[0], row[1], row[2], row[3])

            # For all rows other than the headder row:
            else:

                # If column 4 value > 0.2, print some entries from that row
                if float(row[3]) > 0.2:
                    print("row # ", count, "       ", row[0], row[1], row[2], row[3], row[4], row[5])

                # if count > 4:
                #     break

                count += 1


#################################################################
if __name__ == "__main__":
    main()