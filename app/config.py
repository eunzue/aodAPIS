import psycopg2

BANCO_DATOS_CONEXION_BBDD="host='localhost' dbname='aragopedia_banco_datos'  port='5432' user='user_banco_datos' password='c0nt4453na'"

def conexion():
	return psycopg2.connect(BANCO_DATOS_CONEXION_BBDD)
