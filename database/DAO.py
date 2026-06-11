from database.DB_connect import DBConnect
from model.airport import Airport
from model.rotta import Rotta


class DAO():

    @staticmethod
    def getTuttiAeroporti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)

        query = """
        select * from airports a 
        """
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(Airport(**row))


        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getTutteRotte(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)


        query = """SELECT T1.ORIGIN_AIRPORT_ID as a1, T1.DESTINATION_AIRPORT_ID as a2, COALESCE(T1.D, 0) + COALESCE(T2.D, 0) as totDistance, COALESCE(T1.N, 0) + COALESCE(T2.N, 0) as nVoli
                    FROM
                    (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                    FROM flights f
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T1
                    LEFT JOIN
                    (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                    FROM flights f
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T2
                    ON T1.ORIGIN_AIRPORT_ID = T2.DESTINATION_AIRPORT_ID AND T2.ORIGIN_AIRPORT_ID = T1.DESTINATION_AIRPORT_ID
                    WHERE T1.ORIGIN_AIRPORT_ID < T2.ORIGIN_AIRPORT_ID OR T2.ORIGIN_AIRPORT_ID IS NULL OR T2.DESTINATION_AIRPORT_ID IS NULL"""
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(Rotta(**row))


        cursor.close()
        cnx.close()
        return result
