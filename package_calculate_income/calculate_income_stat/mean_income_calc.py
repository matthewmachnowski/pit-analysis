from .load_data_people import load_people
import pandas as pd


def mean_inc_gm(file1, file2):
    df = file1
    data_lud = load_people.load_gm(file2)
    df = df.join(data_lud["ludnosc"], how='inner')
    df = mean_calc(df)
    return df


def mean_inc_pow(file1, file2):
    df = file1
    data_lud = load_people.load_pow(file2)
    df = df.join(data_lud["ludnosc"], how='inner')
    df = mean_calc(df)
    return df


def mean_inc_woj(file1, file2):
    df = file1
    data_lud = load_people.load_woj(file2)
    df['kod'] = df.index
    df.reset_index(drop=True, inplace=True)
    df = pd.concat([df, data_lud["ludnosc"]], axis=1)
    mean_calc(df)
    df = mean_calc(df)
    df.set_index('kod', inplace=True)
    return df


def mean_calc(data):
    data['sredni-doch-opod'] = (data["dochod-2020"] / (0.6 * data["ludnosc"] * 0.17))
    return data