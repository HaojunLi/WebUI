from django.shortcuts import render
import psycopg2
from django.http import HttpResponse
# Create your views here.
def studyMasim(request):
    con = psycopg2.connect(
        host="masimdb.vmhost.psu.edu",
        database="masim",
        user="sim",
        password="sim")
    # cursor
    cur = con.cursor()
    # execute query
    sql = "SELECT studyid, CASE WHEN name IS NULL THEN 'Unassigned' ELSE name END, configs, replicates FROM " \
          "(SELECT studyid, s.name, COUNT(c.id) configs, COUNT(r.id) replicates " \
          "FROM sim.configuration c LEFT JOIN sim.replicate r ON r.configurationid = c.id LEFT JOIN sim.study s ON s.id = c.studyid GROUP BY studyid, s.name) iq"
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    # close the connection
    con.close()
    return render(request,"index.html",{"rows": rows, "link": "Masim"})

def studyBurkinaFaso(request):
    con = psycopg2.connect(
        host="masimdb.vmhost.psu.edu",
        database="burkinafaso",
        user="sim",
        password="sim")
    # cursor
    cur = con.cursor()
    sql = "SELECT studyid, CASE WHEN name IS NULL THEN 'Unassigned' ELSE name END, configs, replicates FROM " \
          "(SELECT studyid, s.name, COUNT(c.id) configs, COUNT(r.id) replicates " \
          "FROM sim.configuration c LEFT JOIN sim.replicate r ON r.configurationid = c.id LEFT JOIN sim.study s ON s.id = c.studyid GROUP BY studyid, s.name) iq"
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    con.close()
    return render(request,"index.html",{"rows": rows, "link": "BurkinaFaso"})

def studyMasimInsert(request):
    # When the user clicks "Submit" the form should check to see if a name was entered (i.e., more than 1 character), if it is valid then it is submitted to the server.
    name = request.GET["studyName"]
    # Here just switch the connection will be fine
    con = psycopg2.connect(
        host="localhost",
        database="LHJ",
        user="postgres",
        password="1234")
    # catch the error message
    try:
        cur = con.cursor()
        cur.execute("select * from study order by id")
        rows = cur.fetchall()
        cur.close()

        cur = con.cursor()
        # Get current database's current last ID
        lastID = rows[-1][0]
        sql = "insert into Study values (%s, %s)"
        cur.execute(sql, (str(lastID+1),name))
        con.commit()

        cur.close()
        con.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return HttpResponse("Hello")
    return HttpResponse("Success")