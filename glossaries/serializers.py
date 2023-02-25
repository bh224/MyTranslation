from rest_framework.serializers import ModelSerializer
from glossaries.models import Category, Glossary

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields=(
            "pk",
            "name",
            "author",
        )
        read_only_fields = ['project', "author"]

    def __str__(self) -> str:
        return self.name
    
class GlossarySerializer(ModelSerializer):
    class Meta:
        model = Glossary
        fields=(
            "pk",
            "project",
            "category",
            "origin_word",
            "trans_word",
            "furigana",
            "details",
            "author",
        )
        read_only_fields = ['project', "category", "author"]
