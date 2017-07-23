import sys
from tokens_file_manager import TokensFileManager
import address_validator
import eth

if __name__ == '__main__':

    manager = TokensFileManager('data.csv')
    result = manager.get_last_line()

    if not result:
        print('Nothing to do')
    else:
        address, amount = result

        print('csv line #{}: trying to send {} tokens to {}'.format(manager.current_line_number, amount, address))
        print('Press Enter to proceed')
        sys.stdin.readline()

        if not address_validator.check(address):
            raise Exception('ETH address is not valid')

        amount = float(amount)

        if amount <= 0:
            raise Exception('Invalid amount')

        if amount > 12000:
            raise Exception('Seems too big amount')

        eth.send_tokens(address, amount)

        # finally write to file
        manager.write_csv()