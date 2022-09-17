from pydub import AudioSegment
import argparse


def get_args():
    # python sap.py --type=merge -f c.mp3 d.mp3
    # python sap.py --type=cut -f a.m4a -t 0 13 16 20
    # python sap.py --type=cut -f a.m4a -t 0 13 51 -1
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        type=str,
        default="merge",
        choices=["merge", "cut"],
    )
    parser.add_argument(
        "-f",
        "--files",
        nargs='+',
        default=[],
        help="The lists of audio files that needs to be cut or merged."
             "If --type=cut, number of files must be 1."
             "For exmample, -f a.mp3 b.mp3",
    )
    parser.add_argument(
        "-t",
        "--time_intervals",
        nargs='+',
        default=[0, -1],
        help="Only used when --type=cut. The time period that needs to be cut. Unit: second."
             "For example, -t 0 14 17 28 means [0, 14] merged on [17, 28]."
             "By the way, -1 means the end.",
    )
    parser.add_argument(
        "-o",
        "--output_type",
        type=str,
        default="mp3",
        help="('mp3', 'wav', 'raw', 'ogg' or other ffmpeg/avconv supported files)",
    )
    return parser.parse_args()


args = get_args()
if args.type == "merge":
    print("hint: --files must be a list of str.")
    assert len(args.files) >= 1
    assert isinstance(args.files[0], str)
    output_file = AudioSegment.from_file(args.files[0])
    for i, f in enumerate(args.files):
        if i == 0:
            continue
        output_file = output_file + AudioSegment.from_file(f)

    output_file.export("./export." + args.output_type, format=args.output_type)
    print("./export." + args.output_type + " has been exported.")

elif args.type == "cut":
    print("hint: --files must be a list of str. But the length of list is 1.")
    assert len(args.files) == 1, "If --type=cut, number of files must be 1."
    assert isinstance(args.files[0], str)
    input_file = AudioSegment.from_file(args.files[0])

    interval_len = len(args.time_intervals)
    assert interval_len % 2 == 0
    assert interval_len >= 2

    args.time_intervals = [int(x) for x in args.time_intervals]

    for i in range(1, interval_len, 2):
        if args.time_intervals[i] == -1:
            args.time_intervals[i] = len(input_file) // 1000

    output_file = input_file[args.time_intervals[0] * 1000: args.time_intervals[1] * 1000]
    for i in range(2, interval_len, 2):
        output_file += input_file[args.time_intervals[i] * 1000: args.time_intervals[i + 1] * 1000]

    output_file.export("./export." + args.output_type, format=args.output_type)
    print("./export." + args.output_type + " has been exported.")

else:
    print("Please choose the correct type.")
