from pyspark import SparkContext, SparkConf

def main():
    # conf = SparkConf().setAppName("VisibilityAverage")
    # sc = SparkContext(conf=conf)
    sc= SparkContext(appName= 'Visibility')
# Load the NCDC records from a text file
    records = sc.textFile("/user/hadoop/input_2/*-99999-*")

# Filter out records with missing values and bad quality values
    filtered_records = records.filter(lambda line: "999999" not in line and any(qual in line for qual in ["0", "1", "4", "5", "9"]))

# Create key-value pairs of (station_id, (visibility, 1))
    station_visibility = filtered_records.map(lambda line: (line[4:10], (float(line[78:84]), 1)))

# Reduce by key to calculate the sum of visibility and count for each station
    station_sum_count = station_visibility.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

# Calculate the average visibility for each station
    station_average = station_sum_count.map(lambda a: a[0] / a[1])

    station_average.saveAsTextFile('/user/hadoop/output_2/output_q2.txt')
    
    sc.stop()


if  __name__ == '__main__':
    main()