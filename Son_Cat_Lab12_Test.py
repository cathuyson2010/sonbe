from Son_Cat_Lab12_FileProcessor import FileProcessor

FileProcessor.merge('sample1.txt', 'sample2.txt', 'result.txt')
print('Merge function executed.')

FileProcessor.copy('sample1.txt', 2)
print('Copy function executed.')

FileProcessor.convert_to_csv('result.txt', 'output.csv')
print('Convert to CSV function executed.')

FileProcessor.file_statistics('result.txt')