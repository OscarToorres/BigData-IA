from pyspark.sql.functions import unix_timestamp, date_format, col, when
from pyspark.ml import Pipeline
from pyspark.ml import PipelineModel
from pyspark.ml.feature import RFormula
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.mllib.evaluation import BinaryClassificationMetrics
from pyspark.ml.evaluation import BinaryClassificationEvaluator

trips = spark.read.csv('yellow_tripdata_2018-11.csv',header=True,inferSchema=True)

trips.printSchema()

type(trips)

trips.createOrReplaceTempView('taxi_trips')

spark.sql('''SELECT date(tpep_pickup_datetime) as date, count(tpep_pickup_datetime) as num_viajes 
FROM taxi_trips 
WHERE HOUR(tpep_pickup_datetime) BETWEEN 00 AND 01 
GROUP BY date 
ORDER BY date ASC''').show()