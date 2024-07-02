class GraphObj:
    def __init__(self, sid, gid):
        self.sid = sid
        self.gid = gid

    def enrich_from_graph(self, attrs):
        for k, v in attrs:
            if k in self.__dict__ and self.__dict__[k] is not None:
                continue
            self.__setattr__(k, v)
