# -*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
# # plt.plot([2, 4, 6, 8, 10, 12, 14], [2, 5, 7, 8, 8, 8,0])
# plt.show()
import dateutil
from numpy.core.fromnumeric import var
import pymonetdb
from datetime import datetime, date, time
from dateutil.parser import parse
import pandas as pd
import os, sys
import string
import numpy as np
from matplotlib.pylab import plt
import matplotlib.pyplot
import pylab
import statistics
from dateutil import parser
from psutil._common import bytes2human

from functions.AbstractWf import isValid

connection = pymonetdb.connect(username="monetdb", password="monetdb", hostname="localhost", database="voc")


# removepipe = connection.cursor()
# removepipe.arraysize = 1000
# removepipe.execute('select execution_datetime from data_transformation_execution where data_transformation_id = 4 limit 7')
# list = removepipe.fetchall()

# select_times = connection.cursor()
# select_times.execute('select execution_datetime from data_transformation_execution where (id >2)')
# list = select_times.fetchall()
# print(list)
# id = 2

# for i in list:
#     horario_datetime = datetime.strptime(i[0], '%Y-%m-%d %H:%M:%S')
#     update_table = connection.cursor()
#     update_table.execute(f'UPDATE data_transformation_execution SET execution_datetime_end = \'{horario_datetime}\' WHERE id = {id}')
#     id = id+2
#     connection.commit()

# update_table = connection.cursor()
# update_table.execute('UPDATE data_transformation_execution SET program_id = 5 WHERE ((data_transformation_id = 6) AND (id >= 1) and (id <= 1163));')
# # update_table.fetchall()
# update_table.description
# connection.commit()

# update_table = connection.cursor()
# update_table.execute('UPDATE data_transformation_execution SET program_id = 4 WHERE ((data_transformation_id = 6) AND (id >= 1163) and (id <= 2326));')
# # update_table.fetchall()
# update_table.description
# connection.commit()

# update_table = connection.cursor()
# update_table.execute('UPDATE data_transformation_execution SET program_id = 6 WHERE ((data_transformation_id = 6) AND (id >= 2326) and (id <= 3489));')
# # update_table.fetchall()
# update_table.description
# connection.commit()

# update_table = connection.cursor()
# update_table.execute('UPDATE data_transformation_execution SET program_id = 4 WHERE ((data_transformation_id = 12) AND (id >= 3489) and (id <= 4652));')
# # update_table.fetchall()
# update_table.description
# connection.commit()

# update_table = connection.cursor()
# update_table.execute('UPDATE data_transformation_execution SET program_id = 5 WHERE ((data_transformation_id = 12) AND (id >= 4652) and (id <= 5815));')
# # update_table.fetchall()
# update_table.description
# connection.commit()

# update_table = connection.cursor()
# update_table.execute('UPDATE data_transformation_execution SET program_id = 6 WHERE ((data_transformation_id = 12) AND (id >= 5815) and (id <= 6978));')
# # update_table.fetchall()
# update_table.description
# connection.commit()

def time_average(ontoexpline, ontology_program, program_id):
    print("Calculando media de tempo: ", ontology_program, program_id)
    data_transformation_times = connection.cursor()
    data_transformation_times.execute(
        'select execution_datetime, execution_datetime_end from data_transformation_execution where program_id = %s ;' % (program_id))
    data_transformation_times = data_transformation_times.fetchall()
    print("***", data_transformation_times)

    time_total = datetime.strptime("0:00:00", '%H:%M:%S')
    average = datetime.strptime("0:00:00", '%H:%M:%S')
    qtd_times = 0
    interval_list = []

    for i in data_transformation_times:
        # print(i[0])
        time1 = datetime.strptime(str(i[0]), '%Y-%m-%d %H:%M:%S')
        time2 = datetime.strptime(str(i[1]), '%Y-%m-%d %H:%M:%S')
        interval = time2 - time1
        if (interval):
            print("interval: ", interval)
            print("time1: ", time1)
            print("time2: ", time2)
            time_total = time_total + interval
            interval_list.append(interval)
            # qtd_times+=1

    print("total time: ", time_total)
    print("qtds: ", qtd_times)

    # calculando a média de tempo do programa --> mandar pra ontoexpline na data property median_execution_time
    print("Media: ", statistics.median(interval_list))


    average = dateutil.parser.parse(str(statistics.median(interval_list)))
    print("=====> ",average.replace(microsecond=0))
    #reasoner da problema se nao tirar os microssegundos do datetime:
    ontology_program.timeAverage = average.replace(microsecond=0)
    print(ontology_program)
    ontoexpline.save(file="ontologies/ontoexpline.owl", format="rdfxml")



def find_min_max_time(program='mrbayes'):
    executed_program = connection.cursor()
    executed_program.execute('select id from program where (name = \'' + program + '\') ;')
    id_program = executed_program.fetchall()
    print("id: ", int(id_program[0][0]))
    id = id_program[0][0]

    data_transformation_times = connection.cursor()
    data_transformation_times.execute(
        'select execution_datetime, execution_datetime_end from data_transformation_execution where ((data_transformation_id = 26) and (dataflow_execution_id = 586) and (program_id = %s)) ;' % (
            id))
    lista = data_transformation_times.fetchall()
    print(len(lista))

    time_total = datetime.strptime("0:00:00", '%H:%M:%S')
    interval_list = []

    for i in lista:
        # print(i[0])
        time1 = datetime.strptime(str(i[0]), '%Y-%m-%d %H:%M:%S')
        time2 = datetime.strptime(str(i[1]), '%Y-%m-%d %H:%M:%S')
        interval = time2 - time1
        if (interval):
            print("interval: ", interval)
            print("time1: ", time1)
            print("time2: ", time2)
            time_total = time_total + interval
            interval_list.append(interval)

    print("total time: ", time_total)

    # calculando a média de tempo do programa --> mandar pra ontoexpline na data property median_execution_time
    print("min time: ", min(interval_list))
    print("max time: ", max(interval_list))


def alter_telemetry():
    data_transformation = connection.cursor()
    data_transformation.execute(
        'select id, execution_datetime, execution_datetime_end from data_transformation_execution;')
    data_transformation = data_transformation.fetchall()

    telemetry = connection.cursor()
    telemetry.execute('select id, captured_timestamp, dt_execution_23  from telemetry;')
    telemetry = telemetry.fetchall()

    t = connection.cursor()
    t.execute('select * from telemetry where id >= 3318 and id < 3324;')
    t = t.fetchall()
    print(t)

    for f in telemetry:
        print(f[0], '\n')
        for i in data_transformation:
            # print(f[1])
            telemetry_time = parser.parse(f[1])
            dt_initial_time = parser.parse(i[1])

            # dt_final_time = parser.parse(i[2])

            # print(telemetry_time)
            # print(f[0])

            if ((telemetry_time >= dt_initial_time) and (telemetry_time <= i[2])):
                print("id da dt_execution: ", i[0], " telemetria", telemetry_time, " está no intervalo", i[1], i[2])

                up_telemetry = connection.cursor()
                up_telemetry.execute('UPDATE telemetry SET dt_execution_23 = %s WHERE (id = %s);' % (i[0], f[0]))
                # up_telemetry.fetchall()
                up_telemetry.description
                connection.commit()


def select_implementers_execution(data_transformation):
    implementers_execution = connection.cursor()
    implementers_execution.execute(
        'select id, program_id from data_transformation_execution where data_transformation_id = %s;' % data_transformation)
    implementers_execution = implementers_execution.fetchall()
    # print(implementers_execution)
    return implementers_execution


def find_data_tranformation_telemetry_metrics(data_transformation):
    implementers_execution = select_implementers_execution(data_transformation)
    scputimes_user = []
    scputimes_idle = []
    scputimes_steal = []

    # finding global data transformation CPU metrics
    for i in implementers_execution:
        id = i[0]
        select_telemetry = connection.cursor()
        select_telemetry.execute('select id from telemetry where dt_execution_23 = %s;' % id)
        select_telemetry = select_telemetry.fetchall()

        for telemetry in select_telemetry:
            telemetry_cpu = connection.cursor()
            telemetry_cpu.execute(
                'select scputimes_user, scputimes_idle, scputimes_steal from telemetry_cpu where telemetry_id = %s; ' % telemetry)
            telemetry_cpu = telemetry_cpu.fetchall()

            # print("**** ", telemetry_cpu[0][0])
            scputimes_user.append(float(telemetry_cpu[0][0]))
            scputimes_idle.append(float(telemetry_cpu[0][1]))
            scputimes_steal.append(float(telemetry_cpu[0][2]))

    print("cpu telemetry number: ", len(scputimes_user))
    print("CPU user - transformation ", data_transformation, ": ", sum(scputimes_user) / len(scputimes_user))
    print("CPU idle - transformation ", data_transformation, ": ", sum(scputimes_idle) / len(scputimes_idle))
    print("CPU steal - transformation ", data_transformation, ": ", sum(scputimes_steal) / len(scputimes_steal))


def find_program_telemetry_metrics(program, ontoexpline):
    #program é um objeto ontológico
    program_name = program.name


    # program0= "mrbayes"
    implementer = connection.cursor()
    implementer.execute(f'select id from program where name = \'{program_name}\';')
    implementer = implementer.fetchall()
    print("** select do implementer: ", implementer[0])
    program_id = implementer[0][0]
    time_average(ontoexpline, program, program_id)

    implementer_executions = connection.cursor()
    implementer_executions.execute(
        'select id, program_id from data_transformation_execution where program_id = %s;' % program_id)
    implementer_executions = implementer_executions.fetchall()

    #tempo de cpu
    scputimes_user = []
    scputimes_idle = []
    scputimes_steal = []

    #uso de RAM
    svmem_total = []
    svmem_available = []
    svmem_used = []

    #uso de disco
    sdiskio_read_bytes = []
    sdiskio_write_bytes = []
    sdiskio_busy_time = []

    # finding global data transformation CPU metrics
    for i in implementer_executions:
        id = i[0]
        select_telemetry = connection.cursor()
        select_telemetry.execute('select id from telemetry where dt_execution_23 = %s;' % id)
        select_telemetry = select_telemetry.fetchall()

        for telemetry in select_telemetry:
            telemetry_cpu = connection.cursor()
            telemetry_cpu.execute(
                'select scputimes_user, scputimes_idle, scputimes_steal from telemetry_cpu where telemetry_id = %s; ' % telemetry)
            telemetry_cpu = telemetry_cpu.fetchall()

            # print("**** ", telemetry_cpu[0][0])
            scputimes_user.append(float(telemetry_cpu[0][0]))
            scputimes_idle.append(float(telemetry_cpu[0][1]))
            scputimes_steal.append(float(telemetry_cpu[0][2]))

            telemetry_memory = connection.cursor()
            telemetry_memory.execute(
                'select svmem_total, svmem_available, svmem_used from telemetry_memory where telemetry_id = %s; ' % telemetry)
            telemetry_memory = telemetry_memory.fetchall()

            # print("**** ", telemetry_cpu[0][0])
            svmem_total.append(float(telemetry_memory[0][0]))
            svmem_available.append(float(telemetry_memory[0][1]))
            svmem_used.append(float(telemetry_memory[0][2]))

            telemetry_disk = connection.cursor()
            telemetry_disk.execute(
                'select sdiskio_read_bytes, sdiskio_write_bytes, sdiskio_busy_time from telemetry_disk where telemetry_id = %s; ' % telemetry)
            telemetry_disk = telemetry_disk.fetchall()

            # print("**** ", telemetry_cpu[0][0])
            sdiskio_read_bytes.append(float(telemetry_disk[0][0]))
            sdiskio_write_bytes.append(float(telemetry_disk[0][1]))
            sdiskio_busy_time.append(float(telemetry_disk[0][2]))

    print("cpu telemetry number: ", len(scputimes_user))
    print("CPU user - program ", program, " (median): ", (sum(scputimes_user) / len(scputimes_user)))
    print("CPU idle - program ", program, " (median): ", (sum(scputimes_idle) / len(scputimes_idle)))
    print("CPU steal - program ", program, " (median): ", bytes2human(sum(scputimes_steal) / len(scputimes_steal)))
    print("--------------------------------------")
    print("memory telemetry number: ", len(scputimes_user))
    print("svmem_total - program ", program, " (median): ", bytes2human((sum(svmem_total) / len(svmem_total))))
    print("svmem_available - program ", program, " (median): ", bytes2human((sum(svmem_available) / len(svmem_available))))
    print("svmem_used - program ", program, " (median): ", bytes2human(sum(svmem_used) / len(svmem_used)))
    program.averageMemoryUsage = bytes2human(sum(svmem_used) / len(svmem_used))

    print("--------------------------------------")
    print("disk telemetry number: ", len(sdiskio_read_bytes))
    print("sdiskio_read_bytes - program ", program, " (median): ", bytes2human((sum(sdiskio_read_bytes) / len(sdiskio_read_bytes))))
    print("sdiskio_write_bytes - program ", program, " (median): ",
          bytes2human((sum(sdiskio_write_bytes) / len(sdiskio_write_bytes))))
    print("sdiskio_busy_time - program ", program, " (median): ", bytes2human(sum(sdiskio_busy_time) / len(sdiskio_busy_time)))

    program.averageDiskBusyTime = bytes2human(sum(sdiskio_busy_time) / len(sdiskio_busy_time))
    program.averageDiskWriteBytes = bytes2human((sum(sdiskio_write_bytes) / len(sdiskio_write_bytes)))
    program.averageDiskReadBytes = bytes2human((sum(sdiskio_write_bytes) / len(sdiskio_write_bytes)))

    ontoexpline.save(file="ontologies/ontoexpline.owl", format="rdfxml")

# find_data_tranformation_telemetry_metrics()
# find_program_telemetry_metrics()
# alter_telemetry()
# calculate_median_execution_time()
# find_min_max_time()