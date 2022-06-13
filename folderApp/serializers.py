from rest_framework import serializers

from folderApp.models import ObjectOnDB


class ObjectOnDBSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('variable_1', 'variable_2', 'variable_3', 'variable_4', 'variable_5')
        model = ObjectOnDB
