import pandas as pd
import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt
import sys

# Enter the start file number and end file number in the input screen
# Example if you want to analyse from file 3 to file 10 you have to enter "3 10" (without the quotes ofc)
csv_number = list(map(int, input("Enter the range of files you wish to analyse: ").split(" ")))
# If you want to start analysis from somewhere in the middle
mid_break = int(input("Enter the index from which u wish to analyse: "))

for file_no in range(csv_number[0], csv_number[1] + 1):

    # Change the download_dir to the directory where you saved your excel sheet in
    # input_dir = "{folder directory in your pc}" + "\\StarData_" + str(file_no) + ".csv"
    # Note that you have to only change the text in the { } brackets, below is an example of my input_dir
    input_dir = "C:\\Users\\advi\\Downloads" + "\\StarData_" + str(file_no) + ".csv"
    print(f"Analysing File-{file_no}")

    # Change the output_dir to the directory where you want the figures to be saved
    # Below is an example of my output_dir:
    output_dir = "D:\\test export"

    # Note that we skip the first 4 rows from any of the excel sheets as they are not important
    df = pd.read_csv(input_dir, skiprows=4)

    for i in range(mid_break, df.shape[0] if file_no == csv_number[0] else df.shape[0]):

        starstr = "TIC " + str(df.iloc[i][0])
        print(f"Analysing index - {i}")

        try:
            initial = lk.search_lightcurve(starstr)  # Searching the data for the a given "starstr"
            rows = len(initial)
        except KeyboardInterrupt:
            sys.exit(print(f"Last file analysed is - {file_no}, on index {i}"))
        except:
            print(f"{starstr}[all] skipped")
            continue

        # This is the program to analyse each subset data of a particular "starstr"
        for row in range(rows):

            try:
                file1 = initial[row].download(quality_bitmask="default").remove_nans()
                temporary_file = file1.remove_outliers(sigma=4).flatten()
            except KeyboardInterrupt:
                sys.exit(print(f"Last file analysed is - {file_no}, on index {i}"))
            except:
                print(f"{starstr}[{rows}] skipped")
                continue

            # We use two seperate files to be analysed, as a result we get 2 figures for every subset
            # This is because the "to_periodogram" function does not do a good job in finding the accurate time period
            # The method we use does not guarentee a 100% accuracy either
            periodogram_file_1 = temporary_file.to_periodogram(method="bls")
            periodogram_file_2 = temporary_file.to_periodogram(method="bls", period=np.arange(1, 16, 0.01))

            time_period_file1 = periodogram_file_1.period_at_max_power
            time_period_file2 = periodogram_file_2.period_at_max_power

            final_file_1 = temporary_file.fold(period=time_period_file1)
            final_file_2 = temporary_file.fold(period=time_period_file2)

            final_file_1.scatter()
            plt.savefig(output_dir + "\\" + starstr + f"[{row}][normal][index {i}].png")  # Plot 1

            final_file_2.scatter()
            plt.savefig(output_dir + "\\" + starstr + f"[{row}][arange][index {i}].png")  # Plot 2
            plt.close('all')  # This is important to include otherwise the system might crash
