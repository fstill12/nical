import argparse
from teori import achord, Interval, Note


def valid_str(value: str) -> str:
    if any(char.isdigit() for char in value):
        raise argparse.ArgumentTypeError(f"""Kesalahan : Input {value} mengandung angka.
                                             Perbaiki : Hanya tangga nada kromatik yang diterima.""")
    return value

def run(args: argparse.ArgumentParser):
    try:
        kunci = args.tuts.title()
    except AttributeError:
        print("Kesalahan : perintah --tuts or -t adalah objek bertipe 'NoneType'")
    else:
        if args.verbose:
            if args.sharp:
                if args.minor:
                    print(f"akor {kunci} = {achord(note=Note.sharp, tuts=kunci, q=Interval.minor)}")
                elif args.mayor:
                    print(f"akor {kunci} = {achord(note=Note.sharp, tuts=kunci, q=Interval.minor)}")
                else:
                    print("Kesalahan : perintah --minor or m adalah objek bertipe 'NoneType'")
            elif args.flat:
                if args.mayor:
                    print(f"akor {kunci} = {achord(note=Note.flat, tuts=kunci, q=Interval.mayor)}")
                elif args.mayor:
                    print(f"akor {kunci} = {achord(note=Note.flat, tuts=kunci, q=Interval.mayor)}")
                else:
                    print("Kesalahan : perintah --mayor or -M adalah objek bertipe 'NoneType'")
            else:
                print("Kesalahan : perintah '--sharp' dan '-s' adalah objek bertipe 'NoneType'")
                print("Kesalahan : perintah '--flat' dan '-f' adalah objek bertipe 'NoneType'")
        else:
            if args.sharp:
                if args.minor:
                    print(f"akor {kunci} = {achord(note=Note.sharp, tuts=kunci, q=Interval.minor)}")
                elif args.mayor:
                    print(f"akor {kunci} = {achord(note=Note.sharp, tuts=kunci, q=Interval.minor)}")
                else:
                    print("Kesalahan : perintah --minor or m adalah objek bertipe 'NoneType'")
            elif args.flat:
                if args.mayor:
                    print(f"akor {kunci} = {achord(note=Note.flat, tuts=kunci, q=Interval.mayor)}")
                elif args.mayor:
                    print(f"akor {kunci} = {achord(note=Note.flat, tuts=kunci, q=Interval.mayor)}")
                else:
                    print("Kesalahan : perintah --mayor or -M adalah objek bertipe 'NoneType'")
            else:
                print("Kesalahan : perintah '--sharp' dan '-s' adalah objek bertipe 'NoneType'")
                print("Kesalahan : perintah '--flat' dan '-f' adalah objek bertipe 'NoneType'")

if __name__=="__main__":
    # Membuat objek parser
    parser = argparse.ArgumentParser(prog="Nical", description="Nical aplikasi membuat akor", allow_abbrev=False)
    parser.add_argument('--tuts', '-t', type=valid_str, help="Jenis tuts")
    parser.add_argument('--verbose', '-v', action="store_true")
    parser.add_argument('--mayor', '-M', action="store_true")
    parser.add_argument('--minor', '-m', action="store_true")
    parser.add_argument('--sharp', '-s', action="store_true")
    parser.add_argument('--flat', '-f', action="store_true")
    parser.set_defaults(func=run)
    # Mengurai argumen yang diberikan
    args = parser.parse_args()
    args.func(args)