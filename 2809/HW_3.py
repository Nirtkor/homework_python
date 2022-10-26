from datetime import datetime, timedelta


def captain_records(entries, first_date):
    file = open('Captain_diary', 'w')
    try:
        for i in range(len(entries)):
            file.write((str(((datetime.strptime(first_date, "%d-%m-%Y"))
                        + timedelta(days=i)))[:11])
                        + str(entries[i]) + "\n")
    finally:
        file.close()
    return "Captain's diary is done"