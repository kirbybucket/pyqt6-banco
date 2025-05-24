import conexion as con

class HistorialData():

    def buscarPorFecha(self,fechaDesde,fechaHasta,tipo,documento):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        sql = """
        SELECT T.id as transaccion, D.*,T.verificado FROM transferencias T 
        INNER JOIN depositos D ON D.tipo=T.tipo AND D.documento=T.documento
        WHERE T.fecha_registro>='{}' and T.fecha_registro<='{}' and D.documento='{}' and D.tipo='{}'
        AND T.motivo=D.motivo AND T.monto=D.monto
        """.format(fechaDesde,fechaHasta,documento,tipo)
        print(sql)
        res = self.cursor.execute(sql)
        data = res.fetchall()
        return data