import gspread



class GSheet():
    def __init__(self):
        print("GSheet init")
        gc = gspread.service_account('secrets.json')

        spreadsheet = gc.open('weather_private')

        # Get a worksheet by index
        # worksheet1 = spreadsheet.get_worksheet(0)

        # Get a worksheet by name 
        worksheet1 = spreadsheet.worksheet('2013')

        data = worksheet1.get_all_records()
        print(data)