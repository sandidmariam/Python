#!/usr/bin/env python
# coding: utf-8

# In[3]:


import findspark
findspark.init('/home/mariam/Desktop/spark-3.3.0-bin-hadoop3')
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Linear_Regression_Project').getOrCreate()
df = spark.read.csv('file:///home/mariam/Downloads/Python-and-Spark-for-Big-Data-master/Spark_for_Machine_Learning/Linear_Regression/cruise_ship_info.csv',inferSchema=True,header=True)


# In[7]:


df.describe()


# In[8]:


df.show()


# In[9]:


df.printSchema()


# In[10]:


df.head(1)[0]


# In[11]:


df.groupBy('Cruise_line').count().show()


# In[12]:


from pyspark.ml.feature import StringIndexer


# In[15]:


indexer = StringIndexer(inputCol='Cruise_line',outputCol='cruise_cat')
indexed = indexer.fit(df).transform(df)
indexed.head(3)


# In[16]:


from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler


# In[17]:


indexed.columns


# In[21]:


assembler = VectorAssembler(inputCols=['Age',
 'Tonnage',
 'passengers',
 'length',
 'cabins',
 'passenger_density',
 'cruise_cat'],outputCol='features')


# In[22]:


output = assembler.transform(indexed)


# In[23]:


output.select('features','crew').show()


# In[24]:


final_data = output.select(['features','crew'])


# In[25]:


train_data,test_data = final_data.randomSplit([0.7,0.3])


# In[26]:


train_data.describe().show()


# In[27]:


from pyspark.ml.regression import LinearRegression


# In[28]:


ship_lr = LinearRegression(labelCol='crew')


# In[29]:


trained_ship_model = ship_lr.fit(train_data)


# In[30]:


ship_results=trained_ship_model.evaluate(test_data)


# In[31]:


ship_results.rootMeanSquaredError


# In[32]:


train_data.describe().show()


# In[33]:


ship_results.r2


# In[34]:


ship_results.meanSquaredError


# In[36]:


ship_results.meanAbsoluteError


# In[37]:


from pyspark.sql.functions import corr


# In[39]:


df.select(corr('crew','passengers')).show()


# In[ ]:




