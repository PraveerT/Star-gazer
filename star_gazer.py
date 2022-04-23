import pandas as pd

class Star:
    def __init__(self,data):
        self.id=data[0]
        self.hip=data[1]
        self.hd=data[2]
        self.hr=data[3]
        self.gl=data[4]
        self.bf=data[5]
        self.proper=data[6]
        self.ra=data[7]
        self.dec=data[8]
        self.dist=data[9]
        self.pmra=data[10]
        self.pmdec=data[11]
        self.rv=data[12]
        self.mag=data[13]
        self.absmag=data[14]
        self.spect=data[15]
        self.ci=data[16]
        self.x=data[17]
        self.y=data[18]
        self.z=data[19]
        self.vx=data[20]
        self.vy=data[21]
        self.vz=data[22]
        self.rarad=data[23]
        self.decrad=data[24]
        self.pmrarad=data[25]
        self.pmdecrad=data[26]
        self.bayer=data[27]
        self.flam=data[28]
        self.con=data[29]
        self.comp=data[30]
        self.comp_primary=data[31]
        self.base=data[32]
        self.lum=data[33]
        self.var=data[34]
        self.var_min=data[35]
        self.var_max=data[36]

    def __repr__(self):
        return str(self.id)

    def showinfo(self):
        return vars(self)

class Group:
    def __init__(self,data):
        content = pd.read_csv (data)   
        df = pd.DataFrame(content)
        self.rowdata=[x for x in df.to_numpy().tolist()]
        self.stars=[Star(stella) for stella in self.rowdata]

    def data(self,ids=all):
        if ids==all:
            return self.stars
        else:
            return [self.stars[x].showinfo() for x in ids]

        







