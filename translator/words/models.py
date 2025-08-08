from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TranslatedWord(models.Model):
    just_word = models.CharField(max_length=100)
    convert_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='converts', null=True, blank=True)

    def __str__(self):
        return f'{self.just_word} - {self.convert_word}'


class Examples(models.Model):
    example_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='examples', null=True, blank=True)
    expression = models.TextField(null=True, blank=True)
    expression_eng = models.TextField(null=True, blank=True)
