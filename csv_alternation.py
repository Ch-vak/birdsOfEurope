#Libraries
import pandas as pd 


def main():
	data = pd.read_csv('birdeasterneurope.csv', sep='\t')
	df = pd.DataFrame(data ,columns = ['species','countryCode','decimalLatitude','decimalLongitude','year'])
	df.to_csv("/home/cvakasir/mybirdproject/birdsOfEurope/new_data.csv")


if __name__ == "__main__":
	main()