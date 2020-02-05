import sqlite3

class parse_ranker():
    db = None
    current_buyer = None
    current_year = None
    buyers_queue = None
    year_queue = None
    conn = None
    
    def __init__(self,db):
        self.db = db
        self.conn = sqlite3.connect(db)
        self.buyers_queue = [buyer[0].encode('utf-8') for buyer in self.fextract('buyers',2)]
        self.mainloop()    
    
    def fextract(self,info,limit=None):
        if info == "buyers":
            if limit:
                return self.query("SELECT DISTINCT companyname FROM BUYERFIRMS LIMIT " + str(limit) + ";")
            else:
                return self.query("SELECT DISTINCT companyname FROM BUYERFIRMS;")
        else:
            return self.query("SELECT DISTINCT year FROM BUYERFIRMS WHERE BUYERFIRMS.companyname = \"" + self.current_buyer + "\" ORDER BY year asc;")


    def mainloop(self):
        for buyers in self.buyers_queue:
            self.current_buyer = buyers.decode('utf-8')
            self.year_queue = self.fextract('years'))

#     We will get the assets in the three related tables in and ordered set
    def getAssets(self):
        pass
#     We will get the shares in the three related tables in and ordered set
    def getShare(self):
        pass
#     We will get the sales in the three related tables in and ordered set
    def getSales(self):
        pass
    def populate(self):
        pass

    def query(self,query):
        cur = self.conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return data

if __name__ == '__main__':
    pr = parse_ranker("FactsetLong.db")


