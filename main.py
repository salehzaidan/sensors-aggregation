#!/usr/bin/env python
import argparse
import json
import pandas as pd


def nest(d: dict) -> dict:
    # https://stackoverflow.com/a/50932879
    result = {}
    for key, value in d.items():
        target = result
        for k in key[:-1]:
            target = target.setdefault(k, {})
        target[key[-1]] = value
    return result


def df_to_nested_dict(df: pd.DataFrame) -> dict:
    # https://stackoverflow.com/a/50930860
    d = df.to_dict(orient="index")
    return {k: nest(v) for k, v in d.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate sensors data to its statistics (min, max, median, and mean).")
    parser.add_argument("input", type=argparse.FileType("r"), help="Input sensors data in JSON")
    parser.add_argument("output", type=argparse.FileType("w"), help="Output aggregated sensors data in JSON")
    args = parser.parse_args()

    data = json.load(args.input)
    df = pd.json_normalize(data, "array")

    columns = ["temperature", "humidity"]
    agg_features = ["min", "max", "median", "mean"]
    df_agg = df.groupby("roomArea")[columns].agg(agg_features)

    json.dump(df_to_nested_dict(df_agg), args.output)


if __name__ == "__main__":
    main()
