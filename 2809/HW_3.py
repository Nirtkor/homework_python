from datetime import datetime, timedelta


def captain_records(entries, first_date):
    file = open('Captain_diary', 'w')
    try:
        for i in range(len(entries)):
            file.write(
                (str((datetime.strptime(first_date, "%d-%m-%Y")) + timedelta(days=i)))[:11]
                        + str(entries[i]) + "\n"
            )
    except:
        return "Something is wrong with the records, try again with different data"
    finally:
        file.close()
    return "Captain's diary is done"