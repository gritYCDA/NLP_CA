from django.db import models

class Review(models.Model): # Our database model is called Task
    # POSITIVE = 0
    # NEGATIVE = 1
    # NEUTRAL = 2
    #
    # HAPPY = 0
    # ANGRY = 1
    # EXCITED = 2
    # SAD = 3
    # BORED = 4
    # AFRAID = 5
    # DISGUST = 6
    #
    # SENT_CHOICES = ( # We create a tuple of status choices
    #     (POSITIVE, 'Positive'),
    #     (NEGATIVE, 'Negative'),
    #     (NEUTRAL, 'Neutral')
    # )
    #
    # EMO_CHOICES = (
    #     (HAPPY, 'Happy'),
    #     (ANGRY, 'Angry'),
    #     (EXCITED, 'Excited'),
    #     (SAD, 'Sad'),
    #     (BORED, 'Board'),
    #     (AFRAID, 'Afraid'),
    #     (DISGUST, 'Disgust')
    # )

    # description = models.CharField(max_length=255) # The tasks description is limited to 255 characters
    # status = models.IntegerField(choices=STATUS_CHOICES, default=TODO) # The task's status, default status = TODO

    # file_name = models.CharField(max_length=255)
    # file_content = models.TextField()
    reviewtext = models.TextField()
    sentsum = models.CharField(max_length=255)
    pos = models.FloatField()
    neut = models.FloatField()
    neg = models.FloatField()
    emosum = models.CharField(max_length=255)
    happy = models.FloatField()
    angry = models.FloatField()
    excited = models.FloatField()
    sad = models.FloatField()
    bored = models.FloatField()
    afraid = models.FloatField()
    disgust = models.FloatField()
    keyword1 = models.CharField(max_length=255)
    keyword2 = models.CharField(max_length=255)
    keyword3 = models.CharField(max_length=255)
