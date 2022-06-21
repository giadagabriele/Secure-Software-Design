from rest_framework import serializers

from folderApp.models import ObjectOnDB


class ObjectOnDBSerializer(serializers.ModelSerializer):
    variable_1 = serializers.CharField()
    variable_2 = serializers.CharField()
    variable_3 = serializers.CharField()
    variable_4 = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    variable_5 = serializers.TimeField(format="%H:%M", input_formats=['%H:%M', 'iso-8601'])
    #cost = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        fields = ('variable_1', 'variable_2', 'variable_3', 'variable_4', 'variable_5')
        model = ObjectOnDB