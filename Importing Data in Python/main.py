file = open('moby_dick.txt' , mode='r')

print(file.read())

print(file.closed)

file.close()

print(file.closed)

with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

import numpy as np

file = 'digits.csv'

digits = np.loadtxt(file , delimiter=',')

print(digits)

im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

import numpy as np

file = 'digits_header.txt'

data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])

print(data)

file = 'seaslug.txt'

data = np.loadtxt(file, delimiter='\t', dtype=str)

print(data[0])

data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

print(data_float[9])

plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

file = 'titanic.csv'

d = np.recfromcsv(file,delimiter=',',names=True,dtype=None)

print(d[:3])

import pandas as pd 

file = 'titanic.csv'

df = pd.read_csv(file)

print(df.head())

file = 'digits.csv'

data = pd.read_csv(file, nrows=5, header=None)

data_array = data.values

print(type(data_array))

import matplotlib.pyplot as plt

file = 'titanic_corrupt.txt'

data = pd.read_csv(file, sep='\t', comment='

print(data.head())

pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

import pickle

with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

print(d)

print(type(d))

import pandas as pd

file = 'battledeath.xlsx'

xl = pd.ExcelFile(file)

print(xl.sheet_names)

df1 = xl.parse('2004')

print(df1.head())

df2  = xl.parse(0)

print(df2.head())

df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

print(df1.head())

df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country'])

print(df2.head())

from sas7bdat import SAS7BDAT 

with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

print(df_sas.head())

pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

import pandas as pd

df = pd.read_stata('disarea.dta')

print(df.head())

pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()

import numpy as np
import h5py

file = 'LIGO_data.hdf5'

data = h5py.File(file, 'r')

print(type(data))

for key in data.keys():
    print(key)

group = data['strain']

for key in group.keys():
    print(key)

strain = data['strain']['Strain'].value

num_samples = 10000

time = np.arange(0, 1, 1/num_samples)

plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

import scipy.io

mat = scipy.io.loadmat('albeck_gene_expression.mat')

print(type(mat))

print(mat.keys())

print(type(mat['CYratioCyt']))

print(np.shape(mat['CYratioCyt']))

data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')

from sqlalchemy import create_engine

engine = create_engine('sqlite:///Chinook.sqlite')

from sqlalchemy import create_engine

engine = create_engine('sqlite:///Chinook.sqlite')

table_names = engine.table_names()

print(table_names)

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

con = engine.connect()

rs = con.execute("SELECT * FROM Album")

df = pd.DataFrame(rs.fetchall())

con.close()

print(df.head())

with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

print(len(df))

print(df.head())

engine = create_engine('sqlite:///Chinook.sqlite')

with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee WHERE EmployeeId >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.head())

engine = create_engine('sqlite:///Chinook.sqlite')

with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee ORDER BY BirthDate")
    df = pd.DataFrame(rs.fetchall())

    
    df.columns = rs.keys()

print(df.head())

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query("SELECT * FROM Album", engine)

print(df.head())

with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

print(df.equals(df1))

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query(
    "SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate",
    engine
)

print(df.head())

with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.head())

df = pd.read_sql_query(
    "SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",
    engine
)

print(df.head())