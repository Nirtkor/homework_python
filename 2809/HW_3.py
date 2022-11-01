from datetime import datetime, timedelta


def captain_records(entries, first_date):
    with open('Captain_diary', 'w') as opened_file:
        try:
            for i in range(len(entries)):
                opened_file.write(
                    (str((datetime.strptime(first_date, "%d-%m-%Y")) + timedelta(days=i)))[:11]
                            + str(entries[i]) + "\n"
                )
        except:
            return "Something is wrong with the records, try again with different data"

    return "Captain's diary is done"

print(captain_records(['я нашел ром', 'ром заканчивается', 'ром закончился'], "01-01-2007"))