import pandas
def sic2nacis(sicInput):
	if len(str(sicInput))>4:sicInput=str(sicInput)[:4]
	print sicInput
	ans=[]
	df = pandas.read_csv("app/sic2naicsDownloadedFinal.csv")
	for i in range(0, len(df["SIC"]) ) :
        # try:
            # temp=df2["SIC"][i]
            # if sicInput == df2["SIC"][i]:
                # print df2["NAICS"][i]
        # except KeyError:continue
		if str(sicInput) == df["SIC"][i]:
			print df["NAICS"][i]
			ans.append(df["NAICS"][i])
	if ans==[] :ans="no match for now"
	return ans

	
if __name__ == "__main__":
	sic2nacis(1522)