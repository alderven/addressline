import re
import argparse

masks = [r"(?P<name>^\D+) (?P<number>.*)",   # "Musterstrasse 45", "Blaufeldweg 123B", "Am Bächle 23" etc.
         r"(?P<number>^\d+) (?P<name>.*)",   # "4, rue de la revolution", "200 Broadway Av"
         r"(?P<name>^.*) (?P<number>No.*)"]  # "Calle 39 No 1540"


def addressline(input_str):

    output = [None, None]
    tmp_str = input_str.replace(',', '')

    for mask in masks:
        m = re.search(mask, tmp_str)
        try:
            output = [m.group('name'), m.group('number')]
        except AttributeError:
            continue

    print('Addressline converted: "{}" -> "{}, {}"'.format(input_str, output[0], output[1]))
    return set(output)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Addressline Utility')
    parser.add_argument('-a', '--address', help='Address string', required=True)
    args = parser.parse_args()
    addressline(args.address)
