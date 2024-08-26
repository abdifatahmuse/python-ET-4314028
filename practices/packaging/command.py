from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--output', '-o', required=True, help='The Destination file for output')

args = parser.parse_args()

print(args.output)