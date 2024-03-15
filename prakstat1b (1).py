#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

#buat dataframe
df = pd.read_clipboard()
print(df)


# In[3]:


df


# In[5]:


import pandas as pd
# 10 data teman
teman = [
    ["Almakius Felix Bariq Hekopung", "laki - laki", 2023, 173, 60, "Jakarta Timur"],
    ["April lesa farsilis", "perempuan", 2023, 154, 35, "Cirebon"],
    ["fernando junior auparay", "laki - laki", 2023, 175, 40, "Jakarta pusat"],
    ["Yeza Sabillah Abbas", "perempuan", 2023, 160, 40, " Jakarta Barat"],
    ["syahrul arifin", "laki - laki", 2023, 175, 100, "Bekasi Timur"],
    ["Reyhan arnas", "laki - laki", 2023, 168, 60, "Kebon jeruk"],
    ["Rayhan Doni Pramana", "laki - laki", 2023, 172, 45, "Jakarta Timur"],
    ["lisna hidayanti", "perempuan", 2023, 155, 60, "Cawan"],
    ["rachel azzahra putri lukito", "perempuan", 2023, 168, 35, "cibubur"],
    ["Naswa Aulia", "perempuan", 2023, 156, 15, " Jakarta Utara"]
]

# Menggabungkan data teman dengan DataFrame yang sudah ada
df_teman = pd.DataFrame(teman, columns=["nama lengkap", "gender", "angkatan", "tinggi badan", "waktu perjalanan / menit", "wilayah tinggal"])
df = pd.concat([df, df_teman], ignore_index=True)


# Simpan DataFrame ke dalam file CSV dan XLSX
df.to_csv("data_teman.csv", index=False)
df.to_excel("data_teman.xlsx", index=False)


# In[6]:


df = pd.read_csv("data_teman.csv")


# In[7]:


df


# In[8]:


df = pd.read_excel("data_teman.xlsx")


# In[9]:


df


# In[10]:


ringkasan_statistik= df.describe()

print(ringkasan_statistik)


# In[ ]:




