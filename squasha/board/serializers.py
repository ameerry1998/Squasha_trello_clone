from rest_framework import serializers
from board.models import Board, Column, Ticket


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('title','Description','ImageUrl','CreatedAt')
