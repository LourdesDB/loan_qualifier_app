# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(data):
    """Saves data to a CSV file.

    Args:
        data (list of lists): list of lists we want to save in a CSV file.

    Returns:
        Writes data in the CSV file
    """
    # Set the output header
    header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]

    # Set the output file path
    output_path = Path("data\qualifying_loans.csv")

    with open(output_path,'w') as file:
        csvwriter = csv.writer(file, lineterminator='\n')
        csvwriter.writerow(header)
        for loan in data:
            csvwriter.writerow(loan)