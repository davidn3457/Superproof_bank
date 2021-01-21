import csv
import os


def budget():
    # path for data
    csvpath = os.path.join("Resources/budget_data.csv")
    csvpath_results = "analysis/budget_data.txt"

    # Variables definition
    total_months = 0
    total_profit_loss = 0
    prev_profit_loss = 0
    profit_loss_change = 0
    max_increase = ["", 0]
    max_decrease = ["", 9999999]

    profit_loss_changes = []

    # Open file
    with open(csvpath) as csvfile:
        reader = csv.DictReader(csvfile)
        # loop to find total months and profit losses
        for row in reader:
            total_months = total_months + 1
            total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
            print(row)

            # Check changes
            if row['Date'] == 'Jan-2010':
                profit_loss_change = int(row["Profit/Losses"]) - int(row["Profit/Losses"])
            else:
                profit_loss_change = int(row["Profit/Losses"]) - int(past_row["Profit/Losses"])
                # Add to the profit_loss_changes list
                profit_loss_changes.append(profit_loss_change)
            print(profit_loss_change)
            past_row = row


            # Reset the value of prev_profit_loss to the complete row
            prev_profit_loss = int(row["Profit/Losses"])
            print(prev_profit_loss)

            # Find max increase and drecrease
            if (profit_loss_change > max_increase[1]):
                max_increase[1] = profit_loss_change
                max_increase[0] = row["Date"]

            if (profit_loss_change < max_decrease[1]):
                max_decrease[1] = profit_loss_change
                max_decrease[0] = row["Date"]


        # Obtain profit average
        profit_loss_avg = sum(profit_loss_changes) / len(profit_loss_changes)

        # Print results
        print("Financial Analysis")
        print("___________________________")
        print("Total Months: " + str(total_months))
        print("Total: " + "$" + str(total_profit_loss))
        print("Average Change: " + "$" + str(round(profit_loss_avg, 2)))
        print("Greatest Increase: " + str(max_increase[0]) + " ($" + str(max_increase[1]) + ")")
        print("Greatest Decrease: " + str(max_decrease[0]) + " ($" + str(max_decrease[1]) + ")")

        # Output in txt
        with open(csvpath_results, "w") as txt_file:
            txt_file.write("Total Months: " + str(total_months) + "\n")
            txt_file.write("Total: " + str(total_profit_loss) + "\n")
            txt_file.write("Average Change: " + str(profit_loss_avg) + "\n")
            txt_file.write("Greatest Increase: " + str(max_increase[0]) + " ($" + str(max_increase[1]) + ")\n")
            txt_file.write("Greatest Decrease: " + str(max_decrease[0]) + " ($" + str(max_decrease[1]) + ")\n")


if __name__ == '__main__':
    budget()
