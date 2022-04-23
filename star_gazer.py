import pandas as pd

data = pd.read_csv (r'Other\Star_gazer\hygdata_v3.csv\hygdata_v3.csv')   
df = pd.DataFrame(data)
print (df)
print (df.iloc[0][0])

class Star:
    def __init__(self,rowdata):
        self.id=rowdata[0]
        self.hip=rowdata[1]
        self.hd=rowdata[2]
        self.hr=rowdata[3]
        self.gl=rowdata[4]
        self.bf=rowdata[5]
        self.proper=rowdata[6]
        self.ra=rowdata[7]
        self.dec=rowdata[8]
        self.dist=rowdata[9]
        self.pmra=rowdata[10]
        self.pmdec=rowdata[11]
        self.rv=rowdata[12]
        self.mag=rowdata[13]
        self.absmag=rowdata[14]
        self.spect=rowdata[15]
        self.ci=rowdata[16]
        self.x=rowdata[17]
        self.y=rowdata[18]
        self.z=rowdata[19]
        self.vx=rowdata[20]
        self.vy=rowdata[21]
        self.vz=rowdata[22]
        self.rarad=rowdata[23]
        self.decrad=rowdata[24]
        self.pmrarad=rowdata[25]
        self.pmdecrad=rowdata[26]
        self.bayer=rowdata[27]
        self.flam=rowdata[28]
        self.con=rowdata[29]
        self.comp=rowdata[30]
        self.comp_primary=rowdata[31]
        self.base=rowdata[32]
        self.lum=rowdata[33]
        self.var=rowdata[34]
        self.var_min=rowdata[35]
        self.var_max=rowdata[36]


    def __repr__(self):
        return str(self.id)
    def showinfo(self):
        return vars(self)



Mystars=[]
for stella in range(len(df)):
    Mystars.append(Star(df.iloc[stella]))

print (Mystars)
print (Mystars[0].showinfo())





