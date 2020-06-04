import pandas
class mychatserver:
    def getResponse(self,request):
        df = pandas.read_json('chatbotdata')
        df1 = df['response'][df['request'] == request]
        return df1







