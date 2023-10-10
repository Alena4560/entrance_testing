from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_list


def products_dataframe():
    spark = SparkSession.builder.appName('ProductCategory').getOrCreate()

    products = spark.createDataFrame([
        ('Продукт A', 'Категория 1'),
        ('Продукт B', 'Категория 1'),
        ('Продукт C', 'Категория 2'),
        ('Продукт D', 'Категория 3'),
    ], ['Product', 'Category'])

    result = products.groupBy('Product').agg(collect_list('Category').alias('Categories'))
    products_without_categories = products.filter(~col('Product').isin(result.select('Product')))
    final_result = result.union(products_without_categories.select('Product', col('Category').cast('array<string>').alias('Categories')))
    final_result.show(truncate=False)


if __name__ == '__main__':
    products_dataframe()
