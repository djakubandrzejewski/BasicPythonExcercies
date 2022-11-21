class OgraniczonaLista(list):
    def append(self, item):
        if len(OgraniczonaLista) < 30:
            super().append(str(item))
