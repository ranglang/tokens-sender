import csv


class TokensFileManager:
    data_file = None
    lines = []
    current_line_number = None


    def __init__(self, _data_file):
        self.data_file = _data_file
        self.read_csv()


    def read_csv(self):
        with open(self.data_file, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                line = {
                    'address': row[0],
                    'amount': row[1],
                    'status': row[2],
                    'transaction_id': row[3],
                }
                self.lines.append(line)


    def get_last_line(self):
        self.current_line_number = 0
        for line in self.lines:
            self.current_line_number += 1
            if line['status'].strip() == '':
                return line

        return None


    def write_csv(self):
        with open(self.data_file, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in self.lines:
                line_listed = [line['address'], line['amount'], line['status'], line['transaction_id']]
                writer.writerow(line_listed)


if __name__ == "__main__":
    manager = TokensFileManager('data.csv')
    print (manager.get_last_line())
    manager.write_csv()
