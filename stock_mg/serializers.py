from rest_framework import serializers
from stock_mg.models import StockReceive, StockIssue, totalinstock, totaloutstock

class StockReceiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockReceive
        fields = '__all__'

    """def clean_items(self):
        item = self.cleaned_data.get('item')
        if not item:
            raise serializers.ValidationError('This field is required')
        return item"""



class StockIssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockIssue
        fields =  '__all__'

class totalinstockSerializer(serializers.ModelSerializer):

    class Meta:
        model = totalinstock
        fields = '__all__'


class totaloutstockSerializer(serializers.ModelSerializer):

    class Meta:
        model = totaloutstock
        fields = '__all__'


"""class StockRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockRecord
        fields = '__all__'
"""



"""class ReorderLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = """
